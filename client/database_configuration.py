# -*- coding: utf-8 -*-


class DatabaseConfiguration(object):
    def __init__(self, database_dict=None):

        if database_dict and "type" in database_dict:
            self.type = database_dict["type"]
        else:
            self.type = None

        if database_dict and "name" in database_dict:
            self.name = database_dict["name"]
        else:
            self.name = None

        if database_dict and "fqdn" in database_dict:
            self.host = database_dict["fqdn"]
        else:
            self.host = None

        if database_dict and "port" in database_dict:
            self.port = database_dict["port"]
        else:
            self.port = -1

        if database_dict and "username" in database_dict:
            self.username = database_dict["username"]
        else:
            self.username = None

        if database_dict and "password" in database_dict:
            self.password = database_dict["password"]
        else:
            self.password = None

        if database_dict and "version" in database_dict:
            self.version = database_dict["version"]
        else:
            self.version = None
