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

from wallet.models.wt_dynamic_voucher_summary_status import WTDynamicVoucherSummaryStatus

class TestWTDynamicVoucherSummaryStatus(unittest.TestCase):
    """WTDynamicVoucherSummaryStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WTDynamicVoucherSummaryStatus:
        """Test WTDynamicVoucherSummaryStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WTDynamicVoucherSummaryStatus`
        """
        model = WTDynamicVoucherSummaryStatus()
        if include_optional:
            return WTDynamicVoucherSummaryStatus(
            )
        else:
            return WTDynamicVoucherSummaryStatus(
        )
        """

    def testWTDynamicVoucherSummaryStatus(self):
        """Test WTDynamicVoucherSummaryStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
