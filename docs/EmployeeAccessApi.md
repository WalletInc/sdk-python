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
import time
import wallet
from wallet.api import employee_access_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.employee import Employee
from wallet.model.wt_authentication_register import WTAuthenticationRegister
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
    api_instance = employee_access_api.EmployeeAccessApi(api_client)
    wt_authentication_register = WTAuthenticationRegister(
        first_name="John",
        last_name="Doe",
        email="email_example",
        password="password_example",
        hear_about_us="Social Media",
        hear_about_us_details="Social Media Advertisement",
        company_name="Delicious BBQ",
        merchant_type="Restaurant",
        street_address1="street_address1_example",
        street_address2="street_address2_example",
        city="San Jose",
        state="California",
        zip="94088",
        country="United States of America",
        phone_number="+1807877878",
        ein="12-3456789",
    ) # WTAuthenticationRegister | 

    # example passing only required values which don't have defaults set
    try:
        # Register
        api_response = api_instance.register(wt_authentication_register)
        pprint(api_response)
    except wallet.ApiException as e:
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

