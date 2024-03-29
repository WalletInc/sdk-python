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

from wallet.models.fetch_domains_by_industry200_response import FetchDomainsByIndustry200Response

class TestFetchDomainsByIndustry200Response(unittest.TestCase):
    """FetchDomainsByIndustry200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FetchDomainsByIndustry200Response:
        """Test FetchDomainsByIndustry200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FetchDomainsByIndustry200Response`
        """
        model = FetchDomainsByIndustry200Response()
        if include_optional:
            return FetchDomainsByIndustry200Response(
                entertainment = [
                    null
                    ],
                grocery = [
                    null
                    ],
                service = [
                    null
                    ],
                casino = [
                    null
                    ],
                hospitality = [
                    null
                    ],
                food = [
                    null
                    ],
                retail = [
                    null
                    ]
            )
        else:
            return FetchDomainsByIndustry200Response(
                entertainment = [
                    null
                    ],
                grocery = [
                    null
                    ],
                service = [
                    null
                    ],
                casino = [
                    null
                    ],
                hospitality = [
                    null
                    ],
                food = [
                    null
                    ],
                retail = [
                    null
                    ],
        )
        """

    def testFetchDomainsByIndustry200Response(self):
        """Test FetchDomainsByIndustry200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
