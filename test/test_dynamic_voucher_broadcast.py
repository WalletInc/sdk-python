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
from wallet.model.dynamic_voucher import DynamicVoucher
from wallet.model.ss_nano_id import SSNanoID
from wallet.model.wt_imported_list import WTImportedList
from wallet.model.wt_opt_in_list import WTOptInList
globals()['DynamicVoucher'] = DynamicVoucher
globals()['SSNanoID'] = SSNanoID
globals()['WTImportedList'] = WTImportedList
globals()['WTOptInList'] = WTOptInList
from wallet.model.dynamic_voucher_broadcast import DynamicVoucherBroadcast


class TestDynamicVoucherBroadcast(unittest.TestCase):
    """DynamicVoucherBroadcast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDynamicVoucherBroadcast(self):
        """Test DynamicVoucherBroadcast"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DynamicVoucherBroadcast()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
