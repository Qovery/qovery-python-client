import os
import unittest

from qovery_client.qovery import Qovery


class MyQoveryTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyQoveryTest, self).__init__(*args, **kwargs)

        f = open("b64.txt", "r")
        self.b64_file = f.read()
        f.close()

        self.local_configuration_file_path = "local_configuration.json"

        os.environ["QOVERY_JSON_B64"] = self.b64_file
        os.environ["QOVERY_BRANCH_NAME"] = "master"
        os.environ["QOVERY_IS_PRODUCTION"] = "true"

        self.qovery = Qovery()

    def test_is_production(self):
        self.assertEqual(self.qovery.is_production, True)

    def test_branch_name(self):
        self.assertEqual(self.qovery.branch_name, "master")

    def test_configuration(self):
        os.environ["QOVERY_JSON_B64"] = ""
        q = Qovery(configuration_file_path=self.local_configuration_file_path)
        os.environ["QOVERY_JSON_B64"] = self.b64_file

        self.assertIsNotNone(q.configuration)

    def test_configuration_with_bad_file_path(self):
        os.environ["QOVERY_JSON_B64"] = ""
        q = Qovery(configuration_file_path='it_does_not_exists')
        os.environ["QOVERY_JSON_B64"] = self.b64_file

        self.assertIsNone(q.configuration)

    def test_list_databases(self):
        self.assertEqual(len(self.qovery.databases), 1)

    def test_get_database_by_name(self):
        self.assertIsNotNone(self.qovery.get_database_by_name("my-pql"))

    def test_get_wrong_database_by_name(self):
        self.assertIsNone(self.qovery.get_database_by_name("toto"))

    def test_database_host(self):
        self.assertIsNotNone(self.qovery.get_database_by_name("my-pql").host)


if __name__ == '__main__':
    unittest.main()
