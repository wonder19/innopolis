"""Программа валидации и записи json файла в Базу Данных."""
import json
import os
import re

import jsonschema
import psycopg2


class Config:
    """Database config."""

    DATABASE_HOST = "127.0.0.1"
    DATABASE_USERNAME = "postgres"
    DATABASE_PASSWORD = "1"
    DATABASE_PORT = "5432"
    DATABASE_NAME = "database_json"


class Database:
    """PostgreSQL Database class."""

    def __init__(self) -> None:
        """Create new connection."""
        self.host = Config.DATABASE_HOST
        self.username = Config.DATABASE_USERNAME
        self.password = Config.DATABASE_PASSWORD
        self.port = Config.DATABASE_PORT
        self.database = Config.DATABASE_NAME
        self.conn = None

    def connect(self) -> None:
        """Create Connection to a Postgres database."""
        if self.conn is None or self.conn.closed == 1:
            try:
                self.conn = psycopg2.connect(host=self.host,
                                             user=self.username,
                                             password=self.password,
                                             port=self.port,
                                             database=self.database,
                                             )
                print('Connection to Database is opened successfully.')
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error while connecting to Database", error)

    def table_creation(self) -> None:
        """Create new Tables in DataBase."""
        self.connect()
        table_name1 = 'goods'
        table_name2 = 'shops_goods'
        try:
            self.conn.autocommit = True
            cursor = self.conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS goods "
                           "(id INTEGER PRIMARY KEY NOT NULL, "
                           "name VARCHAR(255) NOT NULL, "
                           "package_height float NOT NULL, "
                           "package_width float NOT NULL)")
            self.conn.commit()
            print("Table", table_name1,
                  "is created successfully in PostgreSQL.")
            cursor.execute("CREATE TABLE IF NOT EXISTS shops_goods "
                           "(id SERIAL PRIMARY KEY NOT NULL,"
                           "id_good INTEGER NOT NULL,"
                           "location VARCHAR(255) NOT NULL, "
                           "amount integer NOT NULL,"
                           "FOREIGN KEY (id_good) REFERENCES goods (id))")
            self.conn.commit()
            print("Table", table_name2,
                  "is created successfully in PostgreSQL.")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table: ", error)
        finally:
            if (self.conn):
                self.conn.close()
                # print("PostgreSQL connection is closed")

    def list_parametr(self, param: str) -> list:
        """Return list of id after select."""
        self.connect()
        list_param = ()
        try:
            list_parametr = []
            self.conn.autocommit = True
            cursor = self.conn.cursor()
            if param == 'id':
                cursor.execute("Select id from goods")
                list_param = cursor.fetchall()
        except(Exception):
            print('No info in table')
            list_parametr = None
        for id_tuple in list_param:
            list_parametr.append(id_tuple[0])
        return list_parametr

    def insert_into_goods(self, parsed_string: dict) -> None:
        """Create new row in table goods."""
        table_name1 = 'goods'
        for key in parsed_string:
            if key == "id":
                id = int(parsed_string[key])
                parametr = key
            elif key == "name":
                name = parsed_string[key]
            elif key == "package_params":
                package_params = parsed_string[key]
                for item in parsed_string[key]:
                    if item == "height":
                        package_height = package_params[item]
                    else:
                        package_width = package_params[item]
        good_id_list = self.list_parametr(parametr)
        self.connect()
        try:
            self.conn.autocommit = True
            cursor = self.conn.cursor()
            if id in good_id_list:
                cursor.execute("Update goods set name = %s, "
                               "package_height=%s, "
                               "package_width=%s "
                               "where id = %s",
                               (name, package_height, package_width, id))
                self.conn.commit()
                print("UPDATE", table_name1,
                      "finished successfully in PostgreSQL.")
            else:
                cursor.execute("INSERT INTO goods "
                               "(id, name, package_height, package_width) "
                               "VALUES (%s, %s, %s, %s)",
                               (id, name, package_height, package_width))
                self.conn.commit()
                print("INSERT INTO", table_name1,
                      "finished successfully in PostgreSQL.")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while INSERT INTO: ", error)
        finally:
            if (self.conn):
                self.conn.close()
                # print("PostgreSQL connection is closed")

    def insert_into_shops_goods(self, parsed_string: dict) -> None:
        """Create or update new row in table shops_goods."""
        table_name2 = 'shops_goods'
        for key in parsed_string:
            if key == "id":
                id_good = int(parsed_string[key])
            elif key == "location_and_quantity":
                for item in parsed_string[key]:
                    for obj in item:
                        if obj == "location":
                            location = item[obj]
                        else:
                            amount = item[obj]
                    try:
                        self.connect()
                        self.conn.autocommit = True
                        cursor = self.conn.cursor()
                        cursor.execute("Select * from shops_goods "
                                       "where id_good=%s and location=%s ",
                                       (id_good, location))
                        select = cursor.fetchall()
                        if len(select) > 0:
                            for item in select:
                                id = item[0]
                            cursor.execute("Update shops_goods "
                                           "set amount = %s where id=%s",
                                           (amount, id))
                            self.conn.commit()
                            print("Update", table_name2,
                                  "finished successfully in PostgreSQL.")
                        else:
                            cursor.execute("INSERT INTO shops_goods "
                                           "( id_good, location, amount) "
                                           "VALUES ( %s, %s, %s)",
                                           (id_good, location, amount))
                            self.conn.commit()
                            print("INSERT INTO", table_name2,
                                  "finished successfully in PostgreSQL.")
                    except (Exception, psycopg2.DatabaseError) as error:
                        print("Error while INSERT INTO: ", error)
                    finally:
                        if (self.conn):
                            self.conn.close()
                            # print("PostgreSQL connection is closed")


class File:
    """Create new file class."""

    def __init__(self, file_path: str) -> None:
        """Create new file objet for parsing."""
        self.file_path = os.path.join(os.path.dirname(__file__), file_path)
        try:
            self.file = open(file_path, 'r')
            print("ok")
        except (Exception, TypeError) as err:
            print(err)

    def file_parser(self) -> dict:
        """Create dictionary from file."""
        try:
            parsed_file = json.load(self.file)
            print(parsed_file)
            return parsed_file
        except (Exception) as error:
            print(error)


def input_file_fun(type_of_file: str) -> str:
    """Input file name function."""
    scheme_regex = "(?<=)txt"
    json_regex = "(?<=)json"
    input_path = None
    while input_path is None:
        if type_of_file == 'scheme':
            input_file = input("Input name of scheme file from "
                               "Homework DB directory ")
        else:
            input_file = input("Input name of json file from "
                               "Homework DB directory ")
        if len(input_file) == 0:
            print('input nothing')
            input_path = None
        else:
            if re.search(scheme_regex, input_file) is not None:
                input_path = input_file
            elif re.search(json_regex, input_file) is not None:
                input_path = input_file
            else:
                print('not a file name')
                input_path = None
    return input_path


class SchemeFile(File):
    """Create new child class for schema."""


pass


class JsonFile(File):
    """Create new child class for json."""

    def validate_json(self, parsed_json: dict, parsed_scheme: dict) -> bool:
        """Validate json before insert into DataBase."""
        try:
            valid = jsonschema.validate(parsed_json, parsed_scheme)
            print(valid)
            return True
        except(Exception):
            return False


def exit_function() -> bool:
    """Close program or continue."""
    list_of_answer = ['y', 'n']
    answer = input("Please input y for continue, and n for exit ")
    if len(answer) <= 0:
        exit_function()
    if answer in list_of_answer:
        if answer == 'y':
            return True
        else:
            return False
    else:
        print("Please input y or n")
        exit_function()


if __name__ == '__main__':
    serv = Database()
    serv.connect()
    serv.table_creation()
    answer = True
    while answer is True:
        scheme_path = input_file_fun('scheme')
        if scheme_path:
            scheme = SchemeFile(scheme_path)
        json_path = input_file_fun('json')
        if json_path:
            json_file = JsonFile(json_path)
        parsed_scheme = scheme.file_parser()
        parsed_json = json_file.file_parser()
        valid = json_file.validate_json(parsed_json, parsed_scheme)
        if valid:
            serv.insert_into_goods(parsed_json)
            serv.insert_into_shops_goods(parsed_json)
        else:
            print("Json is invalid, try new one")
        answer = exit_function()
