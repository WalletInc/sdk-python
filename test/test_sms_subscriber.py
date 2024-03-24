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

from wallet.models.sms_subscriber import SmsSubscriber

class TestSmsSubscriber(unittest.TestCase):
    """SmsSubscriber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmsSubscriber:
        """Test SmsSubscriber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SmsSubscriber`
        """
        model = SmsSubscriber()
        if include_optional:
            return SmsSubscriber(
                mobile_number = '+18001234567',
                id = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_active = True,
                merchant_id = 'C0123456789'
            )
        else:
            return SmsSubscriber(
                mobile_number = '+18001234567',
                id = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_active = True,
                merchant_id = 'C0123456789',
        )
        """

    def testSmsSubscriber(self):
        """Test SmsSubscriber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()