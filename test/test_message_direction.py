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
from wallet.model.message_direction_any_of import MessageDirectionAnyOf
from wallet.model.message_direction_any_of1 import MessageDirectionAnyOf1
from wallet.model.message_direction_any_of2 import MessageDirectionAnyOf2
from wallet.model.message_direction_any_of3 import MessageDirectionAnyOf3
globals()['MessageDirectionAnyOf'] = MessageDirectionAnyOf
globals()['MessageDirectionAnyOf1'] = MessageDirectionAnyOf1
globals()['MessageDirectionAnyOf2'] = MessageDirectionAnyOf2
globals()['MessageDirectionAnyOf3'] = MessageDirectionAnyOf3
from wallet.model.message_direction import MessageDirection


class TestMessageDirection(unittest.TestCase):
    """MessageDirection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessageDirection(self):
        """Test MessageDirection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MessageDirection()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
