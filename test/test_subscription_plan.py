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
from wallet.model.portal_page import PortalPage
from wallet.model.subscription_product import SubscriptionProduct
globals()['PortalPage'] = PortalPage
globals()['SubscriptionProduct'] = SubscriptionProduct
from wallet.model.subscription_plan import SubscriptionPlan


class TestSubscriptionPlan(unittest.TestCase):
    """SubscriptionPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscriptionPlan(self):
        """Test SubscriptionPlan"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SubscriptionPlan()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
