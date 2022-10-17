"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.514
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import unittest

import wallet
from wallet.api.system_api import SystemApi  # noqa: E501


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self):
        self.api = SystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role(self):
        """Test case for create_role

        Create role  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete role  # noqa: E501
        """
        pass

    def test_fetch_audit_log_of_roles(self):
        """Test case for fetch_audit_log_of_roles

        Fetch role's audit log  # noqa: E501
        """
        pass

    def test_fetch_employees_with_role(self):
        """Test case for fetch_employees_with_role

        Fetch employees with role  # noqa: E501
        """
        pass

    def test_fetch_webpages_for_role(self):
        """Test case for fetch_webpages_for_role

        Fetch webpages for role  # noqa: E501
        """
        pass

    def test_load_role(self):
        """Test case for load_role

        Fetch role  # noqa: E501
        """
        pass

    def test_save_role(self):
        """Test case for save_role

        Update role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
