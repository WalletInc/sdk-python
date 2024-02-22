# wallet.TransactionLedgerApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_all_ledger_transactions**](TransactionLedgerApi.md#fetch_all_ledger_transactions) | **GET** /v2/pos/ledger/transactions/all | Fetch ledger transactions by page


# **fetch_all_ledger_transactions**
> FetchAllLedgerTransactions200Response fetch_all_ledger_transactions(start_date_time, end_date_time, page_num, page_size, register_type=register_type)

Fetch ledger transactions by page

### Example


```python
import wallet
from wallet.models.fetch_all_ledger_transactions200_response import FetchAllLedgerTransactions200Response
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TransactionLedgerApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    page_num = 3.4 # float | 
    page_size = 3.4 # float | 
    register_type = wallet.ApplicableTerminals() # ApplicableTerminals |  (optional)

    try:
        # Fetch ledger transactions by page
        api_response = api_instance.fetch_all_ledger_transactions(start_date_time, end_date_time, page_num, page_size, register_type=register_type)
        print("The response of TransactionLedgerApi->fetch_all_ledger_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionLedgerApi->fetch_all_ledger_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 
 **page_num** | **float**|  | 
 **page_size** | **float**|  | 
 **register_type** | [**ApplicableTerminals**](.md)|  | [optional] 

### Return type

[**FetchAllLedgerTransactions200Response**](FetchAllLedgerTransactions200Response.md)

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

