# wallet.LoginAndLogoutApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginAndLogoutApi.md#login) | **POST** /authentication/login | Login
[**login_status**](LoginAndLogoutApi.md#login_status) | **GET** /authentication/status/{token} | Retrieve status of session token
[**logout**](LoginAndLogoutApi.md#logout) | **DELETE** /authentication/logout | Logout


# **login**
> WTAuthenticationLoginResponse login(wt_authentication_login_request)

Login

### Example


```python
import time
import wallet
from wallet.api import login_and_logout_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_authentication_login_request import WTAuthenticationLoginRequest
from wallet.model.wt_authentication_login_response import WTAuthenticationLoginResponse
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
    api_instance = login_and_logout_api.LoginAndLogoutApi(api_client)
    wt_authentication_login_request = WTAuthenticationLoginRequest(
        username="username",
        password="password_example",
    ) # WTAuthenticationLoginRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login(wt_authentication_login_request)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoginAndLogoutApi->login: %s\n" % e)
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
> bool, date, datetime, dict, float, int, list, str, none_type login_status(token)

Retrieve status of session token

### Example


```python
import time
import wallet
from wallet.api import login_and_logout_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
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
    api_instance = login_and_logout_api.LoginAndLogoutApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve status of session token
        api_response = api_instance.login_status(token)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoginAndLogoutApi->login_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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
import time
import wallet
from wallet.api import login_and_logout_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
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
    api_instance = login_and_logout_api.LoginAndLogoutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logout
        api_response = api_instance.logout()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoginAndLogoutApi->logout: %s\n" % e)
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

