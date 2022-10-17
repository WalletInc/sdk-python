# wallet.UtilitiesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_prefixes**](UtilitiesApi.md#get_payment_prefixes) | **GET** /v2/payment/prefixes | Get payment prefixes


# **get_payment_prefixes**
> PaymentPrefixes get_payment_prefixes()

Get payment prefixes

### Example


```python
import time
import wallet
from wallet.api import utilities_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.payment_prefixes import PaymentPrefixes
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
    api_instance = utilities_api.UtilitiesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get payment prefixes
        api_response = api_instance.get_payment_prefixes()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling UtilitiesApi->get_payment_prefixes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentPrefixes**](PaymentPrefixes.md)

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

