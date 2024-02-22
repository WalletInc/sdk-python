# wallet.EmployeeAccessApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register**](EmployeeAccessApi.md#register) | **POST** /authentication/register | Register


# **register**
> Employee register(wt_authentication_register)

Register

### Example


```python
import wallet
from wallet.models.employee import Employee
from wallet.models.wt_authentication_register import WTAuthenticationRegister
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
    api_instance = wallet.EmployeeAccessApi(api_client)
    wt_authentication_register = wallet.WTAuthenticationRegister() # WTAuthenticationRegister | 

    try:
        # Register
        api_response = api_instance.register(wt_authentication_register)
        print("The response of EmployeeAccessApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeAccessApi->register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_authentication_register** | [**WTAuthenticationRegister**](WTAuthenticationRegister.md)|  | 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

