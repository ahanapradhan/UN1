import configparser
from pathlib import Path

from mysite.unmasque.src.util.constants import DATABASE_SECTION, HOST, PORT, USER, PASSWORD, SCHEMA, DBNAME, \
    SUPPORT_SECTION


def parse_config_field(config_object, field, section, field_name):
    try:
        field = config_object.get(section, field_name)
    except KeyError:
        print("hostname not found in config. Using default config!")
    return field


class Config:
    def __init__(self):
        # default values
        self.index_maker = "create_indexes.sql"
        self.pkfk = "pkfkrelations.csv"
        self.schema = "public"
        self.dbname = "tpch"
        self.port = "5432"
        self.password = "postgres"
        self.user = "postgres"
        self.host = "localhost"

    def parse_config(self):
        config_file_path = Path(__file__).parent.parent.parent.parent
        config_file = (config_file_path / "config.ini").resolve()
        config_object = configparser.ConfigParser()
        with open(config_file, "r") as file_object:
            config_object.read_file(file_object)

            database_field_names = [HOST, PORT, USER, PASSWORD, DBNAME, SCHEMA]
            database_fields = [self.host, self.port, self.user, self.password, self.dbname, self.schema]
            for i in range(len(database_fields)):
                parse_config_field(config_object, database_fields[i], DATABASE_SECTION, database_field_names[i])

            support_field_names = ["pkfk", "index_maker"]
            support_fields = [self.pkfk, self.index_maker]
            for i in range(len(support_fields)):
                parse_config_field(config_object, support_fields[i], SUPPORT_SECTION, support_field_names[i])

