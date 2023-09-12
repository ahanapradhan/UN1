import copy

from ...src.util import constants


def create_zero_time_profile():
    return ElapsedTime(constants,
                       constants,
                       constants,
                       constants,
                       constants,
                       constants,
                       constants,
                       constants,
                       constants,
                       constants)


class ElapsedTime:
    clause_keys = ["From Clause:",
                   "Correlated Sampling:",
                   "View Minimization:",
                   "Where Clause:",
                   "Projection:",
                   "Group BY:",
                   "Aggregation:",
                   "Order by:",
                   "Limit:",
                   "Number of Times Executable called: "
                   ]
    t_sampling = 0
    t_view_min = 0
    t_where_clause = 0
    t_projection = 0
    t_groupby = 0
    t_aggregate = 0
    t_orderby = 0
    t_limit = 0

    executable_call_count = 0
    t_from_clause = 0

    display_string = ''

    def __init__(self,
                 fc,
                 cs2,
                 vm,
                 wc,
                 pj,
                 gb,
                 agg,
                 ob,
                 lm,
                 app):
        self.t_from_clause += fc.local_elapsed_time
        self.t_sampling += cs2.local_elapsed_time
        self.t_view_min += vm.local_elapsed_time
        self.t_where_clause += wc.local_elapsed_time
        self.t_projection += pj.local_elapsed_time
        self.t_groupby += gb.local_elapsed_time
        self.t_aggregate += agg.local_elapsed_time
        self.t_orderby += ob.local_elapsed_time
        self.t_limit += lm.local_elapsed_time
        self.executable_call_count = app.method_call_count

    def update_for_from_clause(self, t_u):
        self.t_from_clause += t_u

    def update_for_where_clause(self, t_u):
        self.t_where_clause += t_u

    def update_for_projection(self, t_u):
        self.t_projection += t_u

    def update_for_group_by(self, t_u):
        self.t_groupby += t_u

    def update_for_aggregate(self, t_u):
        self.t_aggregate += t_u

    def update_for_order_by(self, t_u):
        self.t_orderby += t_u

    def update_for_limit(self, t_u):
        self.t_limit += t_u

    def update_for_cs2(self, t_u):
        self.t_sampling += t_u

    def update_for_view_minimization(self, t_u):
        self.t_view_min += t_u

    def update_for_app(self, t_u):
        self.executable_call_count += t_u

    def update(self, other_profile):
        self.t_sampling += other_profile.t_sampling
        self.t_view_min += other_profile.t_view_min
        self.t_where_clause += other_profile.t_where_clause
        self.t_projection += other_profile.t_projection
        self.t_groupby += other_profile.t_groupby
        self.t_aggregate += other_profile.t_aggregate
        self.t_orderby += other_profile.t_orderby
        self.t_limit += other_profile.t_limit
        self.executable_call_count = other_profile.executable_call_count

    def print(self):
        max_len = len(max(self.clause_keys, key=len)) + 1
        keys_tabs = []
        for key in self.clause_keys:
            tabs = max_len - len(key)
            keys_tabs.append(tabs)

        times = self.get_times()

        self.display_string += "\n--------------Extraction Time per Module in the Pipeline------------------:"
        i = 0
        while i < len(self.clause_keys):
            if i == len(self.clause_keys) - 1:
                self.display_string += str("\n" +
                                           self.clause_keys[i] + " " + ' ' * (
                                                   max_len - len(self.clause_keys[i])) + " " +
                                           str(round(times[i])))
            else:
                self.display_string += str("\n" +
                                           self.clause_keys[i] + " " + ' ' * (
                                                   max_len - len(self.clause_keys[i])) + " " +
                                           str(round(times[i] * 1000)) + " ms.")
            i += 1

        print(self.display_string)

    def get_json_display_string(self):
        self.print()
        ds = copy.deepcopy(self.display_string)
        ds = ds.replace("\n", "<br>")
        return ds

    def get_times(self):
        times = [self.t_from_clause,
                 self.t_sampling,
                 self.t_view_min,
                 self.t_where_clause,
                 self.t_projection,
                 self.t_groupby,
                 self.t_aggregate,
                 self.t_orderby,
                 self.t_limit,
                 self.executable_call_count]
        return times
