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

from wallet.models.fetch_industry200_response import FetchIndustry200Response

class TestFetchIndustry200Response(unittest.TestCase):
    """FetchIndustry200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FetchIndustry200Response:
        """Test FetchIndustry200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FetchIndustry200Response`
        """
        model = FetchIndustry200Response()
        if include_optional:
            return FetchIndustry200Response(
                plans = [
                    wallet.models.subscription_plan.SubscriptionPlan(
                        id = '', 
                        name = '', 
                        price = 1.337, 
                        nickname = '', 
                        examples = '', 
                        products = [
                            wallet.models.subscription_product.SubscriptionProduct(
                                id = '', 
                                title = '', 
                                title_full = '', 
                                category = '', 
                                volume = 1.337, 
                                features = [
                                    wallet.models.subscription_feature.SubscriptionFeature(
                                        sort_num = 1.337, 
                                        name = '', 
                                        max_volume = '', 
                                        measurement = '', 
                                        description = '', 
                                        current_volume = '', 
                                        is_exceeded = True, 
                                        is_in_use = True, 
                                        is_enabled = True, )
                                    ], 
                                pages = [
                                    'analytics-ad-credits'
                                    ], 
                                icon_name = '', 
                                description = '', 
                                is_hourly = True, 
                                release_status = '', )
                            ], 
                        all_pages = [
                            'analytics-ad-credits'
                            ], )
                    ],
                title = '',
                icon = '',
                sort_number = '',
                id = ''
            )
        else:
            return FetchIndustry200Response(
                plans = [
                    wallet.models.subscription_plan.SubscriptionPlan(
                        id = '', 
                        name = '', 
                        price = 1.337, 
                        nickname = '', 
                        examples = '', 
                        products = [
                            wallet.models.subscription_product.SubscriptionProduct(
                                id = '', 
                                title = '', 
                                title_full = '', 
                                category = '', 
                                volume = 1.337, 
                                features = [
                                    wallet.models.subscription_feature.SubscriptionFeature(
                                        sort_num = 1.337, 
                                        name = '', 
                                        max_volume = '', 
                                        measurement = '', 
                                        description = '', 
                                        current_volume = '', 
                                        is_exceeded = True, 
                                        is_in_use = True, 
                                        is_enabled = True, )
                                    ], 
                                pages = [
                                    'analytics-ad-credits'
                                    ], 
                                icon_name = '', 
                                description = '', 
                                is_hourly = True, 
                                release_status = '', )
                            ], 
                        all_pages = [
                            'analytics-ad-credits'
                            ], )
                    ],
                title = '',
                icon = '',
                sort_number = '',
                id = '',
        )
        """

    def testFetchIndustry200Response(self):
        """Test FetchIndustry200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
