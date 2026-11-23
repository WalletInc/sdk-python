# wallet.HelpDeskApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_help_desk_requests**](HelpDeskApi.md#fetch_help_desk_requests) | **GET** /v2/merchant/helpDeskRequests/{phoneNumberID} | Get help desk requests
[**send_help_desk_response**](HelpDeskApi.md#send_help_desk_response) | **POST** /v2/employee/helpDesk/response | Send help desk response
[**set_help_desk_request_resolved**](HelpDeskApi.md#set_help_desk_request_resolved) | **PATCH** /v2/employee/helpDesk/request/{helpDeskRequestID} | Resolve help desk request


# **fetch_help_desk_requests**
> List[HelpDeskRequest] fetch_help_desk_requests(phone_number_id, is_resolved=is_resolved)

Get help desk requests

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.help_desk_request import HelpDeskRequest
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.HelpDeskApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    is_resolved = True # bool |  (optional)

    try:
        # Get help desk requests
        api_response = api_instance.fetch_help_desk_requests(phone_number_id, is_resolved=is_resolved)
        print("The response of HelpDeskApi->fetch_help_desk_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelpDeskApi->fetch_help_desk_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **is_resolved** | **bool**|  | [optional] 

### Return type

[**List[HelpDeskRequest]**](HelpDeskRequest.md)

### Authorization

[api_token](../README.md#api_token)

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

# **send_help_desk_response**
> OutboundSMS send_help_desk_response(wt_employee_send_help_desk_response)

Send help desk response

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.outbound_sms import OutboundSMS
from wallet.models.wt_employee_send_help_desk_response import WTEmployeeSendHelpDeskResponse
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.HelpDeskApi(api_client)
    wt_employee_send_help_desk_response = wallet.WTEmployeeSendHelpDeskResponse() # WTEmployeeSendHelpDeskResponse | 

    try:
        # Send help desk response
        api_response = api_instance.send_help_desk_response(wt_employee_send_help_desk_response)
        print("The response of HelpDeskApi->send_help_desk_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelpDeskApi->send_help_desk_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_send_help_desk_response** | [**WTEmployeeSendHelpDeskResponse**](WTEmployeeSendHelpDeskResponse.md)|  | 

### Return type

[**OutboundSMS**](OutboundSMS.md)

### Authorization

[api_token](../README.md#api_token)

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

# **set_help_desk_request_resolved**
> HelpDeskRequest set_help_desk_request_resolved(help_desk_request_id)

Resolve help desk request

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.help_desk_request import HelpDeskRequest
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.HelpDeskApi(api_client)
    help_desk_request_id = 'help_desk_request_id_example' # str | 

    try:
        # Resolve help desk request
        api_response = api_instance.set_help_desk_request_resolved(help_desk_request_id)
        print("The response of HelpDeskApi->set_help_desk_request_resolved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelpDeskApi->set_help_desk_request_resolved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **help_desk_request_id** | **str**|  | 

### Return type

[**HelpDeskRequest**](HelpDeskRequest.md)

### Authorization

[api_token](../README.md#api_token)

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

