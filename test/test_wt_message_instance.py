"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.535
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import wallet
from wallet.model.message_direction import MessageDirection
from wallet.model.message_status import MessageStatus
globals()['MessageDirection'] = MessageDirection
globals()['MessageStatus'] = MessageStatus
from wallet.model.wt_message_instance import WTMessageInstance


class TestWTMessageInstance(unittest.TestCase):
    """WTMessageInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWTMessageInstance(self):
        """Test WTMessageInstance"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WTMessageInstance()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
