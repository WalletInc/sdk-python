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

from wallet.models.fetch_inbound_smsby_page200_response import FetchInboundSMSByPage200Response

class TestFetchInboundSMSByPage200Response(unittest.TestCase):
    """FetchInboundSMSByPage200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FetchInboundSMSByPage200Response:
        """Test FetchInboundSMSByPage200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FetchInboundSMSByPage200Response`
        """
        model = FetchInboundSMSByPage200Response()
        if include_optional:
            return FetchInboundSMSByPage200Response(
                total = 1.337,
                length = 1.337,
                results = [
                    wallet.models.inbound_sms.InboundSMS(
                        id = jdu37eua98, 
                        automated_reply = 'This is an automated reply', 
                        automated_reply_additional_info = 'Extra information from Twilio', 
                        sms_sid = 'AHSufjdikj', 
                        sms_message_sid = 'KSIUhwyh87', 
                        sms_status = 'Succeeded', 
                        messaging_service_sid = 'JAUR53tdg2', 
                        account_sid = 'KAIDBVH461', 
                        message_sid = 'AUJDifhy21', 
                        body = 'This is the content in an SMS', 
                        num_segments = 2, 
                        to = '+18047552674', 
                        to_city = 'San Francisco', 
                        to_state = 'California', 
                        to_zip = '94016', 
                        to_country = 'USA', 
                        from = '+18047552674', 
                        from_city = 'New York City', 
                        from_state = 'New York', 
                        from_zip = '10001', 
                        from_country = 'USA', 
                        media_urls = [
                            ''
                            ], 
                        watson_intent = 'Watson Intent', 
                        watson_intents = 'Watson Intents', 
                        watson_context = 'Watson Context', 
                        watson_contexts = 'Watson Contexts', 
                        num_media = 1, 
                        api_version = '2.0.1', 
                        is_opt_in = True, 
                        is_help_desk_request = True, 
                        merchant_id = 'C0123456789', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_active = True, 
                        body_lowercase = 'this is the content in an sms', 
                        from_localized = '8047552674', )
                    ]
            )
        else:
            return FetchInboundSMSByPage200Response(
                total = 1.337,
                length = 1.337,
                results = [
                    wallet.models.inbound_sms.InboundSMS(
                        id = jdu37eua98, 
                        automated_reply = 'This is an automated reply', 
                        automated_reply_additional_info = 'Extra information from Twilio', 
                        sms_sid = 'AHSufjdikj', 
                        sms_message_sid = 'KSIUhwyh87', 
                        sms_status = 'Succeeded', 
                        messaging_service_sid = 'JAUR53tdg2', 
                        account_sid = 'KAIDBVH461', 
                        message_sid = 'AUJDifhy21', 
                        body = 'This is the content in an SMS', 
                        num_segments = 2, 
                        to = '+18047552674', 
                        to_city = 'San Francisco', 
                        to_state = 'California', 
                        to_zip = '94016', 
                        to_country = 'USA', 
                        from = '+18047552674', 
                        from_city = 'New York City', 
                        from_state = 'New York', 
                        from_zip = '10001', 
                        from_country = 'USA', 
                        media_urls = [
                            ''
                            ], 
                        watson_intent = 'Watson Intent', 
                        watson_intents = 'Watson Intents', 
                        watson_context = 'Watson Context', 
                        watson_contexts = 'Watson Contexts', 
                        num_media = 1, 
                        api_version = '2.0.1', 
                        is_opt_in = True, 
                        is_help_desk_request = True, 
                        merchant_id = 'C0123456789', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_active = True, 
                        body_lowercase = 'this is the content in an sms', 
                        from_localized = '8047552674', )
                    ],
        )
        """

    def testFetchInboundSMSByPage200Response(self):
        """Test FetchInboundSMSByPage200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
