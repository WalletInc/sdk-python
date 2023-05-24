"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.535
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import unittest

import wallet
from wallet.api.qr_code_designs_api import QRCodeDesignsApi  # noqa: E501


class TestQRCodeDesignsApi(unittest.TestCase):
    """QRCodeDesignsApi unit test stubs"""

    def setUp(self):
        self.api = QRCodeDesignsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_qr_code_design(self):
        """Test case for archive_qr_code_design

        Archive QR Code Design  # noqa: E501
        """
        pass

    def test_create_qr_code_design(self):
        """Test case for create_qr_code_design

        Create QR Code design  # noqa: E501
        """
        pass

    def test_fetch_all_qr_code_designs(self):
        """Test case for fetch_all_qr_code_designs

        Fetch all active QR Code Designs  # noqa: E501
        """
        pass

    def test_fetch_qr_code_design_by_id(self):
        """Test case for fetch_qr_code_design_by_id

        Fetch QR Code Design  # noqa: E501
        """
        pass

    def test_restore_qr_code_design(self):
        """Test case for restore_qr_code_design

        Restore payment design  # noqa: E501
        """
        pass

    def test_update_qr_code_design(self):
        """Test case for update_qr_code_design

        Update QR Code Design  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
