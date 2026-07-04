# wallet.EmployeesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_peer_to_roles**](EmployeesApi.md#add_peer_to_roles) | **POST** /v2/employee/roles/peer/{userID} | Add peer to roles
[**create_employee_peer**](EmployeesApi.md#create_employee_peer) | **POST** /v2/employee/peer | Create employee peer
[**fetch_merchant**](EmployeesApi.md#fetch_merchant) | **GET** /v2/employee/merchant | Create employee alert
[**fetch_messages**](EmployeesApi.md#fetch_messages) | **GET** /v2/employee/messages/all | Get all messages
[**fetch_peer_activity**](EmployeesApi.md#fetch_peer_activity) | **GET** /v2/employee/peer/activity/{employeeID} | Get peer activity
[**fetch_peers_permissions**](EmployeesApi.md#fetch_peers_permissions) | **GET** /v2/employee/peer/permissions/{userID} | Get peer permissions
[**fetch_profile_info**](EmployeesApi.md#fetch_profile_info) | **GET** /v2/employee | Get employee info
[**load_webpages_of_employee**](EmployeesApi.md#load_webpages_of_employee) | **GET** /v2/employee/webpages/all | Get employee&#39;s permissions
[**modify_peers_roles**](EmployeesApi.md#modify_peers_roles) | **PUT** /v2/employee/peer/permissions/{userID} | Modify peer&#39;s roles
[**remove_peer_from_all_roles**](EmployeesApi.md#remove_peer_from_all_roles) | **DELETE** /v2/employee/peer/permissions/{userID} | Remove peer from all roles
[**set_alerts_read**](EmployeesApi.md#set_alerts_read) | **PATCH** /v2/employee/alerts | Mark alerts as read
[**set_messages_read**](EmployeesApi.md#set_messages_read) | **PATCH** /v2/employee/messages | Mark messages as read
[**set_profile_picture**](EmployeesApi.md#set_profile_picture) | **PUT** /v2/employee/profile/picture | Set profile picture
[**update_email_notification_preference**](EmployeesApi.md#update_email_notification_preference) | **PUT** /v2/employee/emailNotificationPreference | Changes the employee&#39;s email notification preference to enabled or disabled
[**update_employee_peer**](EmployeesApi.md#update_employee_peer) | **PUT** /v2/employee/peer/{userID} | Update peer


# **add_peer_to_roles**
> str add_peer_to_roles(user_id, wt_employee_peer_roles)

Add peer to roles

### Example


```python
import wallet
from wallet.models.wt_employee_peer_roles import WTEmployeePeerRoles
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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = 'user_id_example' # str | 
    wt_employee_peer_roles = wallet.WTEmployeePeerRoles() # WTEmployeePeerRoles | 

    try:
        # Add peer to roles
        api_response = api_instance.add_peer_to_roles(user_id, wt_employee_peer_roles)
        print("The response of EmployeesApi->add_peer_to_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->add_peer_to_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **wt_employee_peer_roles** | [**WTEmployeePeerRoles**](WTEmployeePeerRoles.md)|  | 

### Return type

**str**

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

# **create_employee_peer**
> Employee create_employee_peer(wt_employee_create)

Create employee peer

### Example


```python
import wallet
from wallet.models.employee import Employee
from wallet.models.wt_employee_create import WTEmployeeCreate
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_create = wallet.WTEmployeeCreate() # WTEmployeeCreate | 

    try:
        # Create employee peer
        api_response = api_instance.create_employee_peer(wt_employee_create)
        print("The response of EmployeesApi->create_employee_peer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_employee_peer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create** | [**WTEmployeeCreate**](WTEmployeeCreate.md)|  | 

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

# **fetch_merchant**
> object fetch_merchant()

Create employee alert

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Create employee alert
        api_response = api_instance.fetch_merchant()
        print("The response of EmployeesApi->fetch_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_merchant: %s\n" % e)
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
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_messages**
> List[Message] fetch_messages()

Get all messages

### Example


```python
import wallet
from wallet.models.message import Message
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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Get all messages
        api_response = api_instance.fetch_messages()
        print("The response of EmployeesApi->fetch_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_messages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Message]**](Message.md)

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

# **fetch_peer_activity**
> List[EmployeeActivityLog] fetch_peer_activity(employee_id)

Get peer activity

### Example


```python
import wallet
from wallet.models.employee_activity_log import EmployeeActivityLog
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
    api_instance = wallet.EmployeesApi(api_client)
    employee_id = 'employee_id_example' # str | 

    try:
        # Get peer activity
        api_response = api_instance.fetch_peer_activity(employee_id)
        print("The response of EmployeesApi->fetch_peer_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_peer_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 

### Return type

[**List[EmployeeActivityLog]**](EmployeeActivityLog.md)

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

# **fetch_peers_permissions**
> List[object] fetch_peers_permissions(user_id)

Get peer permissions

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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get peer permissions
        api_response = api_instance.fetch_peers_permissions(user_id)
        print("The response of EmployeesApi->fetch_peers_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_peers_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

**List[object]**

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

# **fetch_profile_info**
> Employee fetch_profile_info()

Get employee info

### Example


```python
import wallet
from wallet.models.employee import Employee
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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Get employee info
        api_response = api_instance.fetch_profile_info()
        print("The response of EmployeesApi->fetch_profile_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_profile_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Employee**](Employee.md)

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

# **load_webpages_of_employee**
> List[Webpage] load_webpages_of_employee()

Get employee's permissions

### Example


```python
import wallet
from wallet.models.webpage import Webpage
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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Get employee's permissions
        api_response = api_instance.load_webpages_of_employee()
        print("The response of EmployeesApi->load_webpages_of_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->load_webpages_of_employee: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Webpage]**](Webpage.md)

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

# **modify_peers_roles**
> List[object] modify_peers_roles(user_id, wt_employee_peer_roles)

Modify peer's roles

### Example


```python
import wallet
from wallet.models.wt_employee_peer_roles import WTEmployeePeerRoles
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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = 'user_id_example' # str | 
    wt_employee_peer_roles = wallet.WTEmployeePeerRoles() # WTEmployeePeerRoles | 

    try:
        # Modify peer's roles
        api_response = api_instance.modify_peers_roles(user_id, wt_employee_peer_roles)
        print("The response of EmployeesApi->modify_peers_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->modify_peers_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **wt_employee_peer_roles** | [**WTEmployeePeerRoles**](WTEmployeePeerRoles.md)|  | 

### Return type

**List[object]**

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

# **remove_peer_from_all_roles**
> bool remove_peer_from_all_roles(user_id)

Remove peer from all roles

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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Remove peer from all roles
        api_response = api_instance.remove_peer_from_all_roles(user_id)
        print("The response of EmployeesApi->remove_peer_from_all_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->remove_peer_from_all_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

**bool**

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

# **set_alerts_read**
> bool set_alerts_read()

Mark alerts as read

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Mark alerts as read
        api_response = api_instance.set_alerts_read()
        print("The response of EmployeesApi->set_alerts_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_alerts_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

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

# **set_messages_read**
> bool set_messages_read()

Mark messages as read

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Mark messages as read
        api_response = api_instance.set_messages_read()
        print("The response of EmployeesApi->set_messages_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_messages_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

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

# **set_profile_picture**
> str set_profile_picture(wt_employee_create_media_file)

Set profile picture

### Example


```python
import wallet
from wallet.models.wt_employee_create_media_file import WTEmployeeCreateMediaFile
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_create_media_file = wallet.WTEmployeeCreateMediaFile() # WTEmployeeCreateMediaFile | 

    try:
        # Set profile picture
        api_response = api_instance.set_profile_picture(wt_employee_create_media_file)
        print("The response of EmployeesApi->set_profile_picture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_profile_picture: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create_media_file** | [**WTEmployeeCreateMediaFile**](WTEmployeeCreateMediaFile.md)|  | 

### Return type

**str**

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

# **update_email_notification_preference**
> Employee update_email_notification_preference(update_email_notification_preference_request)

Changes the employee's email notification preference to enabled or disabled

### Example


```python
import wallet
from wallet.models.employee import Employee
from wallet.models.update_email_notification_preference_request import UpdateEmailNotificationPreferenceRequest
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
    api_instance = wallet.EmployeesApi(api_client)
    update_email_notification_preference_request = wallet.UpdateEmailNotificationPreferenceRequest() # UpdateEmailNotificationPreferenceRequest | 

    try:
        # Changes the employee's email notification preference to enabled or disabled
        api_response = api_instance.update_email_notification_preference(update_email_notification_preference_request)
        print("The response of EmployeesApi->update_email_notification_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->update_email_notification_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_email_notification_preference_request** | [**UpdateEmailNotificationPreferenceRequest**](UpdateEmailNotificationPreferenceRequest.md)|  | 

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

# **update_employee_peer**
> Employee update_employee_peer(user_id, wt_employee_update)

Update peer

### Example


```python
import wallet
from wallet.models.employee import Employee
from wallet.models.wt_employee_update import WTEmployeeUpdate
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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = 'user_id_example' # str | 
    wt_employee_update = wallet.WTEmployeeUpdate() # WTEmployeeUpdate | 

    try:
        # Update peer
        api_response = api_instance.update_employee_peer(user_id, wt_employee_update)
        print("The response of EmployeesApi->update_employee_peer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->update_employee_peer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **wt_employee_update** | [**WTEmployeeUpdate**](WTEmployeeUpdate.md)|  | 

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

