# wallet.IndustriesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_all_industries**](IndustriesApi.md#fetch_all_industries) | **GET** /system/industries/all | Fetch all industries
[**fetch_domains_by_industry**](IndustriesApi.md#fetch_domains_by_industry) | **GET** /system/industries/domains | Fetch all industries
[**fetch_industries_ids**](IndustriesApi.md#fetch_industries_ids) | **GET** /system/industries/trimmed | Fetch all industries


# **fetch_all_industries**
> List[FetchIndustry200Response] fetch_all_industries()

Fetch all industries

### Example


```python
import wallet
from wallet.models.fetch_industry200_response import FetchIndustry200Response
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
    api_instance = wallet.IndustriesApi(api_client)

    try:
        # Fetch all industries
        api_response = api_instance.fetch_all_industries()
        print("The response of IndustriesApi->fetch_all_industries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->fetch_all_industries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FetchIndustry200Response]**](FetchIndustry200Response.md)

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
> FetchDomainsByIndustry200Response fetch_domains_by_industry()

Fetch all industries

### Example


```python
import wallet
from wallet.models.fetch_domains_by_industry200_response import FetchDomainsByIndustry200Response
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
    api_instance = wallet.IndustriesApi(api_client)

    try:
        # Fetch all industries
        api_response = api_instance.fetch_domains_by_industry()
        print("The response of IndustriesApi->fetch_domains_by_industry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->fetch_domains_by_industry: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FetchDomainsByIndustry200Response**](FetchDomainsByIndustry200Response.md)

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

# **fetch_industries_ids**
> object fetch_industries_ids()

Fetch all industries

### Example


```python
import wallet
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
    api_instance = wallet.IndustriesApi(api_client)

    try:
        # Fetch all industries
        api_response = api_instance.fetch_industries_ids()
        print("The response of IndustriesApi->fetch_industries_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndustriesApi->fetch_industries_ids: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

