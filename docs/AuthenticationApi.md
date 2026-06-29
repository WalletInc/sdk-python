# wallet.AuthenticationApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /authentication/login | Login
[**login_status**](AuthenticationApi.md#login_status) | **GET** /authentication/status/{token} | Retrieve session token status
[**logout**](AuthenticationApi.md#logout) | **DELETE** /authentication/logout | Logout
[**register**](AuthenticationApi.md#register) | **POST** /authentication/register | Register


# **login**
> WTAuthenticationLoginResponse login(wt_authentication_login_request)

Login

### Example


```python
import wallet
from wallet.models.wt_authentication_login_request import WTAuthenticationLoginRequest
from wallet.models.wt_authentication_login_response import WTAuthenticationLoginResponse
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
    api_instance = wallet.AuthenticationApi(api_client)
    wt_authentication_login_request = wallet.WTAuthenticationLoginRequest() # WTAuthenticationLoginRequest | 

    try:
        # Login
        api_response = api_instance.login(wt_authentication_login_request)
        print("The response of AuthenticationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_authentication_login_request** | [**WTAuthenticationLoginRequest**](WTAuthenticationLoginRequest.md)|  | 

### Return type

[**WTAuthenticationLoginResponse**](WTAuthenticationLoginResponse.md)

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

# **login_status**
> LoginStatus200Response login_status(token)

Retrieve session token status

### Example


```python
import wallet
from wallet.models.login_status200_response import LoginStatus200Response
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
    api_instance = wallet.AuthenticationApi(api_client)
    token = 'token_example' # str | 

    try:
        # Retrieve session token status
        api_response = api_instance.login_status(token)
        print("The response of AuthenticationApi->login_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**LoginStatus200Response**](LoginStatus200Response.md)

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

# **logout**
> str logout()

Logout

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
    api_instance = wallet.AuthenticationApi(api_client)

    try:
        # Logout
        api_response = api_instance.logout()
        print("The response of AuthenticationApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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
    api_instance = wallet.AuthenticationApi(api_client)
    wt_authentication_register = wallet.WTAuthenticationRegister() # WTAuthenticationRegister | 

    try:
        # Register
        api_response = api_instance.register(wt_authentication_register)
        print("The response of AuthenticationApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->register: %s\n" % e)
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

