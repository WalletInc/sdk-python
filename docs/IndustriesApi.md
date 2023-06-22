# wallet.IndustriesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_all_industries**](IndustriesApi.md#fetch_all_industries) | **GET** /system/industries/all | Fetch all industries
[**fetch_domains_by_industry**](IndustriesApi.md#fetch_domains_by_industry) | **GET** /system/industries/domains | Fetch all industries


# **fetch_all_industries**
> [InlineResponse200] fetch_all_industries()

Fetch all industries

### Example


```python
import time
import wallet
from wallet.api import industries_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = industries_api.IndustriesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all industries
        api_response = api_instance.fetch_all_industries()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling IndustriesApi->fetch_all_industries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_domains_by_industry**
> InlineResponse20011 fetch_domains_by_industry()

Fetch all industries

### Example


```python
import time
import wallet
from wallet.api import industries_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.inline_response20011 import InlineResponse20011
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = industries_api.IndustriesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all industries
        api_response = api_instance.fetch_domains_by_industry()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling IndustriesApi->fetch_domains_by_industry: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

