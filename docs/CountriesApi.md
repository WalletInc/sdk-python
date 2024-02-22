# wallet.CountriesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_all_countries**](CountriesApi.md#fetch_all_countries) | **GET** /system/countries/all | Fetch all countries


# **fetch_all_countries**
> List[FetchAllCountries200ResponseInner] fetch_all_countries()

Fetch all countries

### Example


```python
import wallet
from wallet.models.fetch_all_countries200_response_inner import FetchAllCountries200ResponseInner
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
    api_instance = wallet.CountriesApi(api_client)

    try:
        # Fetch all countries
        api_response = api_instance.fetch_all_countries()
        print("The response of CountriesApi->fetch_all_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->fetch_all_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FetchAllCountries200ResponseInner]**](FetchAllCountries200ResponseInner.md)

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

