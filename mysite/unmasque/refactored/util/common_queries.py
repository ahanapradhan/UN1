def drop_table(tab):
    return f"drop table if exists {tab};"


def alter_table_rename_to(tab, retab):
    return f"Alter table {tab} rename to {retab};"


def alter_view_rename_to(tab, retab):
    return f"Alter view {tab} rename to {retab};"


def create_table_like(tab, ctab):
    return f"Create table {tab} (like {ctab});"


def create_table_as_select_star_from(tab, fromtab):
    return f"Create table {tab} as select * from {fromtab};"


def get_row_count(tab):
    return f"select count(*) from {tab};"


def get_star(tab):
    return f"select * from {tab};"


def get_star_from_except_all_get_star_from(tab1, tab2):
    return f"(select * from {tab1} except all select * from {tab2})"


def get_restore_name(tab):
    return f"{tab}_restore"


def get_min_max_ctid(tab):
    return f"select min(ctid), max(ctid) from {tab};"


def drop_view(tab):
    return f"drop view if exists {tab};"


def get_tabname_1(tab):
    return f"{tab}1"


def get_tabname_4(tab):
    return f"{tab}4"


def get_tabname_un(tab):
    return f"{tab}_un"


def get_tabname_nep(tab):
    return f"{tab}_nep"


def create_view_as_select_star_where_ctid(mid_ctid1, start_ctid, view, tab):
    _start_citd = str(start_ctid)
    _end_ctid = str(mid_ctid1)
    return f"create view {view} as select * from {tab} where ctid >= '{_start_citd}' and ctid <= '{_end_ctid}';"


def create_table_as_select_star_from_ctid(end_ctid, start_ctid, tab, fromtab):
    _start_citd = str(start_ctid)
    _end_ctid = str(end_ctid)
    return f"create table {tab} as select * from {fromtab} where ctid >= '{_start_citd}' and ctid <= '{_end_ctid}';"


def get_ctid_from(min_or_max, tabname):
    return f"select {min_or_max}(ctid) from {tabname};"


def truncate_table(table):
    return f"Truncate Table {table};"


def insert_into_tab_attribs_format(att_order, esc_string, tab):
    return f"INSERT INTO {tab} {att_order}  VALUES {esc_string}"


def update_tab_attrib_with_value(attrib, tab, value):
    str_value = str(value)
    return f"UPDATE {tab}  SET {attrib}={str_value};"
