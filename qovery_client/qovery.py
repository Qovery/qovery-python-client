# -*- coding: utf-8 -*-
import base64
import json
import os

from qovery_client.database_configuration import DatabaseConfiguration


class Qovery(object):

    def __init__(self, configuration_file=None):
        self._ENV_JSON_B64 = "QOVERY_JSON_B64"
        self._ENV_IS_PRODUCTION = "QOVERY_IS_PRODUCTION"
        self._ENV_BRANCH_NAME = "QOVERY_BRANCH_NAME"

        self._configuration_file = configuration_file

        self.configuration = self._get_configuration_from_environment_variable(self._ENV_JSON_B64)
        if not self.configuration:
            self.configuration = self._get_configuration_from_file(configuration_file)

    @staticmethod
    def _get_configuration_from_environment_variable(environment_variable):
        if not environment_variable:
            return None

        b64_json = os.getenv(environment_variable)
        if not b64_json:
            return None

        json_string = base64.b64decode(b64_json)
        return json.loads(json_string)

    @staticmethod
    def _get_configuration_from_file(file):
        if not file:
            return None

        try:
            json_string = file.read()
            file.close()

            return json.loads(json_string)
        except OSError:
            pass

        return None

    @property
    def branch_name(self):
        return os.getenv(self._ENV_BRANCH_NAME)

    @property
    def is_production(self):
        is_production_str = os.getenv(self._ENV_IS_PRODUCTION)
        if not is_production_str or str(is_production_str).lower() == "false":
            return False

        return True

    @property
    def databases(self):
        if not self.configuration or "databases" not in self.configuration:
            return []

        return [DatabaseConfiguration(database_dict) for database_dict in self.configuration["databases"]]

    def get_database_by_name(self, name):
        databases = list(filter(lambda x: x.name == name, self.databases))
        if not databases:
            return None

        return databases[0]
