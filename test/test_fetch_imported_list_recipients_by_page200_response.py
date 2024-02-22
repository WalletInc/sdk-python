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

from wallet.models.fetch_imported_list_recipients_by_page200_response import FetchImportedListRecipientsByPage200Response

class TestFetchImportedListRecipientsByPage200Response(unittest.TestCase):
    """FetchImportedListRecipientsByPage200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FetchImportedListRecipientsByPage200Response:
        """Test FetchImportedListRecipientsByPage200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FetchImportedListRecipientsByPage200Response`
        """
        model = FetchImportedListRecipientsByPage200Response()
        if include_optional:
            return FetchImportedListRecipientsByPage200Response(
                total = 1.337,
                length = 1.337,
                results = [
                    wallet.models.imported_list_recipient.ImportedListRecipient(
                        imported_list_id = 'C0123456789', 
                        mobile_phone_number = '+18047552674', 
                        id = jdu37eua98, 
                        merchant_id = 'C0123456789', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_active = True, 
                        opted_status = True, )
                    ]
            )
        else:
            return FetchImportedListRecipientsByPage200Response(
                total = 1.337,
                length = 1.337,
                results = [
                    wallet.models.imported_list_recipient.ImportedListRecipient(
                        imported_list_id = 'C0123456789', 
                        mobile_phone_number = '+18047552674', 
                        id = jdu37eua98, 
                        merchant_id = 'C0123456789', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_active = True, 
                        opted_status = True, )
                    ],
        )
        """

    def testFetchImportedListRecipientsByPage200Response(self):
        """Test FetchImportedListRecipientsByPage200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
