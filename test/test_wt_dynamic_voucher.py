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
from wallet.model.nano_id import NanoID
from wallet.model.wt_dynamic_voucher_summary import WTDynamicVoucherSummary
globals()['MerchantID'] = MerchantID
globals()['NanoID'] = NanoID
globals()['WTDynamicVoucherSummary'] = WTDynamicVoucherSummary
from wallet.model.wt_dynamic_voucher import WTDynamicVoucher


class TestWTDynamicVoucher(unittest.TestCase):
    """WTDynamicVoucher unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWTDynamicVoucher(self):
        """Test WTDynamicVoucher"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WTDynamicVoucher()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
