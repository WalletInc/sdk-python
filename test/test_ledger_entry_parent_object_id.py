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

from wallet.models.ledger_entry_parent_object_id import LedgerEntryParentObjectID

class TestLedgerEntryParentObjectID(unittest.TestCase):
    """LedgerEntryParentObjectID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LedgerEntryParentObjectID:
        """Test LedgerEntryParentObjectID
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LedgerEntryParentObjectID`
        """
        model = LedgerEntryParentObjectID()
        if include_optional:
            return LedgerEntryParentObjectID(
            )
        else:
            return LedgerEntryParentObjectID(
        )
        """

    def testLedgerEntryParentObjectID(self):
        """Test LedgerEntryParentObjectID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()