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
from wallet.model.merchant_id import MerchantID
from wallet.model.prefixed_nano_id import PrefixedNanoID
globals()['MerchantID'] = MerchantID
globals()['PrefixedNanoID'] = PrefixedNanoID
from wallet.model.member import Member


class TestMember(unittest.TestCase):
    """Member unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMember(self):
        """Test Member"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Member()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
