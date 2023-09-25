"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.535
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from wallet.api_client import ApiClient, Endpoint as _Endpoint
from wallet.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from wallet.model.applicable_terminals import ApplicableTerminals
from wallet.model.auth_error import AuthError
from wallet.model.falsum_error import FalsumError
from wallet.model.inline_response2009 import InlineResponse2009
from wallet.model.internal_server_error import InternalServerError


class TransactionLedgerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.fetch_all_ledger_transactions_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2009,),
                'auth': [],
                'endpoint_path': '/v2/pos/ledger/transactions/all',
                'operation_id': 'fetch_all_ledger_transactions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'start_date_time',
                    'end_date_time',
                    'page_num',
                    'page_size',
                    'register_type',
                ],
                'required': [
                    'start_date_time',
                    'end_date_time',
                    'page_num',
                    'page_size',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'start_date_time':
                        (datetime,),
                    'end_date_time':
                        (datetime,),
                    'page_num':
                        (float,),
                    'page_size':
                        (float,),
                    'register_type':
                        (ApplicableTerminals,),
                },
                'attribute_map': {
                    'start_date_time': 'startDateTime',
                    'end_date_time': 'endDateTime',
                    'page_num': 'pageNum',
                    'page_size': 'pageSize',
                    'register_type': 'registerType',
                },
                'location_map': {
                    'start_date_time': 'query',
                    'end_date_time': 'query',
                    'page_num': 'query',
                    'page_size': 'query',
                    'register_type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def fetch_all_ledger_transactions(
        self,
        start_date_time,
        end_date_time,
        page_num,
        page_size,
        **kwargs
    ):
        """Fetch ledger transactions by page  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_all_ledger_transactions(start_date_time, end_date_time, page_num, page_size, async_req=True)
        >>> result = thread.get()

        Args:
            start_date_time (datetime):
            end_date_time (datetime):
            page_num (float):
            page_size (float):

        Keyword Args:
            register_type (ApplicableTerminals): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2009
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['start_date_time'] = \
            start_date_time
        kwargs['end_date_time'] = \
            end_date_time
        kwargs['page_num'] = \
            page_num
        kwargs['page_size'] = \
            page_size
        return self.fetch_all_ledger_transactions_endpoint.call_with_http_info(**kwargs)

