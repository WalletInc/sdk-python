# coding: utf-8

"""
    wallet-api

    API

    The version of the OpenAPI document: 2.1.600
    Contact: development@wallet.inc
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wallet.models.employee_schedule_start_meridiem import EmployeeScheduleStartMeridiem

class TestEmployeeScheduleStartMeridiem(unittest.TestCase):
    """EmployeeScheduleStartMeridiem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployeeScheduleStartMeridiem:
        """Test EmployeeScheduleStartMeridiem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmployeeScheduleStartMeridiem`
        """
        model = EmployeeScheduleStartMeridiem()
        if include_optional:
            return EmployeeScheduleStartMeridiem(
            )
        else:
            return EmployeeScheduleStartMeridiem(
        )
        """

    def testEmployeeScheduleStartMeridiem(self):
        """Test EmployeeScheduleStartMeridiem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()