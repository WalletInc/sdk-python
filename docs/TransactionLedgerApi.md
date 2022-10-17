# wallet.TransactionLedgerApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_all_ledger_transactions**](TransactionLedgerApi.md#fetch_all_ledger_transactions) | **GET** /v2/pos/ledger/transactions/all | Fetch ledger transactions by page


# **fetch_all_ledger_transactions**
> InlineResponse2005 fetch_all_ledger_transactions(start_date_time, end_date_time, page_num, page_size)

Fetch ledger transactions by page

### Example


```python
import time
import wallet
from wallet.api import transaction_ledger_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.applicable_terminals import ApplicableTerminals
from wallet.model.inline_response2005 import InlineResponse2005
from wallet.model.auth_error import AuthError
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_ledger_api.TransactionLedgerApi(api_client)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    page_num = 3.14 # float | 
    page_size = 3.14 # float | 
    register_type = ApplicableTerminals(None) # ApplicableTerminals |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch ledger transactions by page
        api_response = api_instance.fetch_all_ledger_transactions(start_date_time, end_date_time, page_num, page_size)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling TransactionLedgerApi->fetch_all_ledger_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch ledger transactions by page
        api_response = api_instance.fetch_all_ledger_transactions(start_date_time, end_date_time, page_num, page_size, register_type=register_type)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling TransactionLedgerApi->fetch_all_ledger_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  |
 **end_date_time** | **datetime**|  |
 **page_num** | **float**|  |
 **page_size** | **float**|  |
 **register_type** | **ApplicableTerminals**|  | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

