"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.514
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import wallet
from wallet.model.ss_nano_id import SSNanoID
globals()['SSNanoID'] = SSNanoID
from wallet.model.phone_number import PhoneNumber


class TestPhoneNumber(unittest.TestCase):
    """PhoneNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPhoneNumber(self):
        """Test PhoneNumber"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PhoneNumber()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
