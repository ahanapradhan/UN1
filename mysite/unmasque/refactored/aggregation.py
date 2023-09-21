import ast
import copy
import math

from ..refactored.abstract.GenerationPipeLineBase import GenerationPipeLineBase
from ..refactored.util.utils import is_number, get_val_plus_delta, get_dummy_val_for, get_format, \
    get_char, isQ_result_empty
from ..src.util.constants import SUM, AVG, MIN, MAX, COUNT, COUNT_STAR
from ..src.util.constants import min_int_val, max_int_val


def get_k_value_for_number(a, b):
    if a == b:
        k_value = 1
        if a == 2:
            k_value = 2
        agg_array = [SUM, k_value * a + b, AVG, a, MIN, a, MAX, a, COUNT, k_value + 1]
    else:
        constraint_array = [0, a, b, a - 1, b - 1]
        if a != 0:
            constraint_array.append((a - b) / a)
        if a != 1:
            constraint_array.append((1 - b) / (a - 1))
        if (a - 2) ** 2 - (4 * (1 - b)) >= 0:
            constraint_array.append(((a - 2) + math.sqrt((a - 2) ** 2 - (4 * (1 - b)))) / 2)
        k_value = 2
        while k_value in constraint_array:
            k_value = k_value + 1
        avg = round((k_value * a + b) / (k_value + 1), 2)
        if avg / int(avg) == 1:
            avg = int(avg)
        agg_array = [SUM, k_value * a + b, AVG, avg, MIN, min(a, b), MAX, max(a, b), COUNT, k_value + 1]
    return k_value, agg_array


def get_k_value(attrib, attrib_types_dict, filter_attrib_dict, groupby_key_flag, tabname):
    if groupby_key_flag and ('int' in attrib_types_dict[(tabname, attrib)]
                             or 'numeric' in attrib_types_dict[(tabname, attrib)]):
        a = b = 3
        k_value = 1
        agg_array = [SUM, k_value * a + b, AVG, a, MIN, a, MAX, a, COUNT, k_value + 1]
    elif (tabname, attrib) in filter_attrib_dict.keys():
        if ('int' in attrib_types_dict[(tabname, attrib)]
                or 'numeric' in attrib_types_dict[(tabname, attrib)]):
            # PRECISION TO BE TAKEN CARE FOR NUMERIC
            a = filter_attrib_dict[(tabname, attrib)][0]
            b = min(filter_attrib_dict[(tabname, attrib)][0] + 1, filter_attrib_dict[(tabname, attrib)][1])
            if a == 0:  # swap a and b
                a = b
                b = 0
            k_value, agg_array = get_k_value_for_number(a, b)
        elif 'date' in attrib_types_dict[(tabname, attrib)]:
            date_val = filter_attrib_dict[(tabname, attrib)][0]
            a = get_format('date', date_val)
            date_val_plus_1 = get_val_plus_delta('date', date_val, 1)
            b = get_format('date', min(date_val_plus_1, filter_attrib_dict[(tabname, attrib)][1]))
            k_value = 1
            agg_array = [MIN, min(a, b), MAX, max(a, b)]
            a = ast.literal_eval(a)
            b = ast.literal_eval(b)
        else:
            # string filter attribute
            if '_' in filter_attrib_dict[(tabname, attrib)]:
                a = filter_attrib_dict[(tabname, attrib)].replace('_', 'a')
                b = filter_attrib_dict[(tabname, attrib)].replace('_', 'b')
            else:
                a = filter_attrib_dict[(tabname, attrib)].replace('%', 'a', 1)
                b = filter_attrib_dict[(tabname, attrib)].replace('%', 'b', 1)
            a = a.replace('%', '')
            b = b.replace('%', '')
            k_value = 1
            agg_array = [MIN, min(a, b), MAX, max(a, b)]
    else:
        if 'date' in attrib_types_dict[(tabname, attrib)]:
            a = get_format('date', get_dummy_val_for('date'))
            b = get_format('date', get_val_plus_delta('date', get_dummy_val_for('date'), 1))
            k_value = 1
            agg_array = [MIN, min(a, b), MAX, max(a, b)]
        elif ('int' in attrib_types_dict[(tabname, attrib)]
              or 'numeric' in attrib_types_dict[(tabname, attrib)]):
            # Combination which gives all different results for aggregation
            a = 5
            b = 8
            k_value = 2
            agg_array = [SUM, 18, AVG, 6, MIN, 5, MAX, 8, COUNT, 3]
        else:
            # String data type
            a = get_char(get_dummy_val_for('char'))
            b = get_char(get_val_plus_delta('char', get_dummy_val_for('char'), 1))
            k_value = 1
            agg_array = [MIN, min(a, b), MAX, max(a, b)]
    return a, agg_array, b, k_value


class Aggregation(GenerationPipeLineBase):
    def __init__(self, connectionHelper,
                 global_key_attributes,
                 global_attrib_types,
                 core_relations,
                 filter_predicates,
                 global_all_attribs,
                 join_graph,
                 projected_attribs,
                 has_groupby,
                 groupby_attribs,
                 dependencies,
                 solution,
                 param_list):
        super().__init__(connectionHelper, "Aggregation",
                         core_relations,
                         global_all_attribs,
                         global_attrib_types,
                         join_graph,
                         filter_predicates)
        self.global_aggregated_attributes = None
        self.global_key_attributes = global_key_attributes
        self.global_projected_attributes = projected_attribs
        self.has_groupby = has_groupby
        self.global_groupby_attributes = groupby_attribs
        self.dependencies = dependencies
        self.solution = solution
        self.param_list = param_list

    def doExtractJob(self, query, attrib_types_dict, filter_attrib_dict):
        # AsSUMing NO DISTINCT IN AGGREGATION

        self.global_aggregated_attributes = [(element, '') for element in self.global_projected_attributes]
        if not self.has_groupby:
            return False

        for i in range(len(self.core_relations)):
            tabname = self.core_relations[i]
            attrib_list = copy.deepcopy(self.global_all_attribs[i])
            for attrib in attrib_list:
                # check if it is a key attribute
                key_list = next((elt for elt in self.global_join_graph if attrib in elt), [])

                # Attribute Filtering
                if attrib in self.global_groupby_attributes:
                    continue

                l = 0
                result_index_list = []
                for j, dep in enumerate(self.dependencies):
                    for i in dep:
                        if attrib in i:
                            result_index_list.append(j)
                            break

                groupby_key_flag = False
                if attrib in self.global_key_attributes and attrib in self.global_groupby_attributes:
                    groupby_key_flag = True

                for result_index in result_index_list:
                    a, agg_array, b, k_value = get_k_value(attrib, attrib_types_dict, filter_attrib_dict,
                                                           groupby_key_flag, tabname)

                    self.truncate_core_relations()
                    temp_vals = []

                    # For this table (tabname) and this attribute (attrib), fill all tables now
                    for j in range(len(self.core_relations)):
                        tabname_inner = self.core_relations[j]
                        attrib_list_inner = self.global_all_attribs[j]

                        insert_rows = []

                        no_of_rows = k_value + 1 if tabname_inner == tabname else 1
                        key_path_flag = any(val in key_list for val in attrib_list_inner)
                        if tabname_inner != tabname and key_path_flag:
                            no_of_rows = 2

                        att_order = '('
                        flag = False
                        for k in range(no_of_rows):
                            insert_values = []

                            for attrib_inner in attrib_list_inner:
                                if not flag:
                                    att_order += attrib_inner + ","
                                if (attrib_inner == attrib or attrib_inner in key_list) and k == no_of_rows - 1:
                                    insert_values.append(b)
                                elif attrib_inner == attrib or attrib_inner in key_list:
                                    insert_values.append(a)
                                elif 'date' in attrib_types_dict[(tabname_inner, attrib_inner)]:
                                    # check for filter
                                    if (tabname_inner, attrib_inner) in filter_attrib_dict.keys():
                                        date_val = filter_attrib_dict[(tabname_inner, attrib_inner)][0]
                                    else:
                                        date_val = get_val_plus_delta('date', get_dummy_val_for('date'), 2)
                                    insert_values.append(ast.literal_eval(get_format('date', date_val)))
                                elif 'int' in attrib_types_dict[(tabname_inner, attrib_inner)] or 'numeric' in \
                                        attrib_types_dict[(tabname_inner, attrib_inner)]:
                                    # check for filter
                                    if (tabname_inner, attrib_inner) in filter_attrib_dict.keys():
                                        number_val = filter_attrib_dict[(tabname_inner, attrib_inner)][0]
                                    else:
                                        number_val = get_dummy_val_for('int')
                                    insert_values.append(get_format('int', number_val))
                                else:
                                    # check for filter
                                    if (tabname_inner, attrib_inner) in filter_attrib_dict.keys():
                                        plus_val = filter_attrib_dict[(tabname_inner, attrib_inner)].replace('%', '')
                                    else:
                                        plus_val = get_char(get_val_plus_delta('char', get_dummy_val_for('char'), 2))
                                    insert_values.append(plus_val)
                            insert_rows.append(tuple(insert_values))
                            flag = True

                        print("Attribute Ordering: ", att_order)
                        print("Rows: ", insert_rows)
                        temp_vals.append(insert_rows)
                        self.insert_attrib_vals_into_table(att_order, attrib_list_inner, insert_rows, tabname_inner)

                    # print("Debug", self.dependencies, result_index)
                    if len(self.dependencies[result_index]) > 1:
                        # print("Temp values", temp_vals)
                        s = 0
                        mi = max_int_val
                        ma = min_int_val
                        av = 0
                        temp_ar = []
                        local_sol = self.solution[result_index]
                        for ele in self.dependencies[result_index]:
                            local_tabname = ele[0]
                            local_attrib = ele[1]
                            local_attrib_index = self.global_all_attribs[
                                self.core_relations.index(local_tabname)].index(local_attrib)
                            vals_sp = temp_vals[self.core_relations.index(local_tabname)]
                            l = []
                            for row in vals_sp:
                                l.append(row[local_attrib_index])
                            temp_ar.append((local_attrib, tuple(l)))
                        for i in range(no_of_rows):
                            inter_val = []
                            eqn = 0
                            for j in range(len(self.dependencies[result_index])):
                                inter_val.append(int(temp_ar[j][1][i]))
                            ele = 1
                            n = len(self.dependencies[result_index])
                            for j in range(n, len(self.param_list[result_index])):
                                ele = int(j / n)
                                # coeff[0][j] = coeff[0][(j-n)]*coeff[0][(j+ele)%n]
                                inter_val.append(inter_val[(j - n)] * inter_val[(j + ele) % n])
                            inter_val.append(1)
                            print("Intermediate Values of all", inter_val)
                            for j, val in enumerate(inter_val):
                                eqn += (val * local_sol[j][0])
                            s += eqn
                            mi = eqn if eqn < mi else mi
                            ma = eqn if eqn > ma else ma
                        av = (s / no_of_rows)
                        # print("Temp Array", temp_ar)
                        # print("SUM, AV, MIN, MAX", s, av, mi, ma)
                        agg_array = [SUM, s, AVG, av, MIN, mi, MAX, ma, COUNT, no_of_rows]
                    new_result = self.app.doJob(query)
                    if isQ_result_empty(new_result):
                        print('some error in generating new database. Result is empty. Can not identify aggregation')
                        return False
                    elif len(new_result) > 2:
                        continue

                    self.analyze(agg_array, self.global_projected_attributes[result_index], new_result, result_index)

        for i in range(len(self.global_projected_attributes)):
            if self.global_projected_attributes[i] == '':
                self.global_aggregated_attributes[i] = ('', COUNT_STAR)

        return True

    def analyze(self, agg_array, attrib, new_result, result_index):
        new_result = list(new_result[1])
        new_result = [x.strip() for x in new_result]
        check_value = 0
        if is_number(new_result[result_index]):
            check_value = round(float(new_result[result_index]), 2)
            if check_value / int(check_value) == 1:
                check_value = int(check_value)
        else:
            check_value = str(new_result[result_index])
        j = 0
        while j < len(agg_array) - 1:
            if check_value == agg_array[j + 1]:
                self.global_aggregated_attributes[result_index] = (str(attrib), agg_array[j])
                break
            j = j + 2
