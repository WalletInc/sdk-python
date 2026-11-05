# wallet.MenusApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_menu**](MenusApi.md#archive_menu) | **DELETE** /menus/{id} | Archive a menu
[**archive_menu_item**](MenusApi.md#archive_menu_item) | **DELETE** /menuItems/{id} | Archive a menu item
[**archive_menu_option_group**](MenusApi.md#archive_menu_option_group) | **DELETE** /menuOptionGroups/{id} | Archive an option group
[**create_menu**](MenusApi.md#create_menu) | **POST** /menus | Create a menu
[**create_menu_item**](MenusApi.md#create_menu_item) | **POST** /menuItems | Create a menu item
[**create_menu_option_group**](MenusApi.md#create_menu_option_group) | **POST** /menuOptionGroups | Create an option group
[**fetch_menu**](MenusApi.md#fetch_menu) | **GET** /menus/{id} | Get a menu
[**fetch_menu_item**](MenusApi.md#fetch_menu_item) | **GET** /menuItems/{id} | Get a menu item
[**fetch_menu_items**](MenusApi.md#fetch_menu_items) | **GET** /menuItems | List menu items
[**fetch_menu_option_group**](MenusApi.md#fetch_menu_option_group) | **GET** /menuOptionGroups/{id} | Get an option group
[**fetch_menu_option_groups**](MenusApi.md#fetch_menu_option_groups) | **GET** /menuOptionGroups | List option groups
[**fetch_menus**](MenusApi.md#fetch_menus) | **GET** /menus | List menus
[**restore_menu**](MenusApi.md#restore_menu) | **PATCH** /menus/{id} | Restore a menu
[**restore_menu_item**](MenusApi.md#restore_menu_item) | **PATCH** /menuItems/{id} | Restore a menu item
[**restore_menu_option_group**](MenusApi.md#restore_menu_option_group) | **PATCH** /menuOptionGroups/{id} | Restore an option group
[**update_menu**](MenusApi.md#update_menu) | **PUT** /menus/{id} | Update a menu
[**update_menu_item**](MenusApi.md#update_menu_item) | **PUT** /menuItems/{id} | Update a menu item
[**update_menu_option_group**](MenusApi.md#update_menu_option_group) | **PUT** /menuOptionGroups/{id} | Update an option group


# **archive_menu**
> WTMenu archive_menu(id)

Archive a menu

### Example


```python
import wallet
from wallet.models.wt_menu import WTMenu
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive a menu
        api_response = api_instance.archive_menu(id)
        print("The response of MenusApi->archive_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->archive_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenu**](WTMenu.md)

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

# **archive_menu_item**
> WTMenuItem archive_menu_item(id)

Archive a menu item

### Example


```python
import wallet
from wallet.models.wt_menu_item import WTMenuItem
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive a menu item
        api_response = api_instance.archive_menu_item(id)
        print("The response of MenusApi->archive_menu_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->archive_menu_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenuItem**](WTMenuItem.md)

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

# **archive_menu_option_group**
> WTMenuOptionGroup archive_menu_option_group(id)

Archive an option group

### Example


```python
import wallet
from wallet.models.wt_menu_option_group import WTMenuOptionGroup
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive an option group
        api_response = api_instance.archive_menu_option_group(id)
        print("The response of MenusApi->archive_menu_option_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->archive_menu_option_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenuOptionGroup**](WTMenuOptionGroup.md)

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

# **create_menu**
> WTMenu create_menu(wt_menu_create_params)

Create a menu

### Example


```python
import wallet
from wallet.models.wt_menu import WTMenu
from wallet.models.wt_menu_create_params import WTMenuCreateParams
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
    api_instance = wallet.MenusApi(api_client)
    wt_menu_create_params = wallet.WTMenuCreateParams() # WTMenuCreateParams | 

    try:
        # Create a menu
        api_response = api_instance.create_menu(wt_menu_create_params)
        print("The response of MenusApi->create_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->create_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_menu_create_params** | [**WTMenuCreateParams**](WTMenuCreateParams.md)|  | 

### Return type

[**WTMenu**](WTMenu.md)

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

# **create_menu_item**
> WTMenuItem create_menu_item(wt_menu_item_create_params)

Create a menu item

### Example


```python
import wallet
from wallet.models.wt_menu_item import WTMenuItem
from wallet.models.wt_menu_item_create_params import WTMenuItemCreateParams
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
    api_instance = wallet.MenusApi(api_client)
    wt_menu_item_create_params = wallet.WTMenuItemCreateParams() # WTMenuItemCreateParams | 

    try:
        # Create a menu item
        api_response = api_instance.create_menu_item(wt_menu_item_create_params)
        print("The response of MenusApi->create_menu_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->create_menu_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_menu_item_create_params** | [**WTMenuItemCreateParams**](WTMenuItemCreateParams.md)|  | 

### Return type

[**WTMenuItem**](WTMenuItem.md)

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

# **create_menu_option_group**
> WTMenuOptionGroup create_menu_option_group(wt_menu_option_group_create_params)

Create an option group

### Example


```python
import wallet
from wallet.models.wt_menu_option_group import WTMenuOptionGroup
from wallet.models.wt_menu_option_group_create_params import WTMenuOptionGroupCreateParams
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
    api_instance = wallet.MenusApi(api_client)
    wt_menu_option_group_create_params = wallet.WTMenuOptionGroupCreateParams() # WTMenuOptionGroupCreateParams | 

    try:
        # Create an option group
        api_response = api_instance.create_menu_option_group(wt_menu_option_group_create_params)
        print("The response of MenusApi->create_menu_option_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->create_menu_option_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_menu_option_group_create_params** | [**WTMenuOptionGroupCreateParams**](WTMenuOptionGroupCreateParams.md)|  | 

### Return type

[**WTMenuOptionGroup**](WTMenuOptionGroup.md)

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

# **fetch_menu**
> WTMenu fetch_menu(id)

Get a menu

### Example


```python
import wallet
from wallet.models.wt_menu import WTMenu
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a menu
        api_response = api_instance.fetch_menu(id)
        print("The response of MenusApi->fetch_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->fetch_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenu**](WTMenu.md)

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

# **fetch_menu_item**
> WTMenuItem fetch_menu_item(id)

Get a menu item

### Example


```python
import wallet
from wallet.models.wt_menu_item import WTMenuItem
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a menu item
        api_response = api_instance.fetch_menu_item(id)
        print("The response of MenusApi->fetch_menu_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->fetch_menu_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenuItem**](WTMenuItem.md)

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

# **fetch_menu_items**
> List[WTMenuItem] fetch_menu_items(is_archive_included=is_archive_included)

List menu items

### Example


```python
import wallet
from wallet.models.wt_menu_item import WTMenuItem
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
    api_instance = wallet.MenusApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # List menu items
        api_response = api_instance.fetch_menu_items(is_archive_included=is_archive_included)
        print("The response of MenusApi->fetch_menu_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->fetch_menu_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTMenuItem]**](WTMenuItem.md)

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

# **fetch_menu_option_group**
> WTMenuOptionGroup fetch_menu_option_group(id)

Get an option group

### Example


```python
import wallet
from wallet.models.wt_menu_option_group import WTMenuOptionGroup
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get an option group
        api_response = api_instance.fetch_menu_option_group(id)
        print("The response of MenusApi->fetch_menu_option_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->fetch_menu_option_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenuOptionGroup**](WTMenuOptionGroup.md)

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

# **fetch_menu_option_groups**
> List[WTMenuOptionGroup] fetch_menu_option_groups(is_archive_included=is_archive_included)

List option groups

### Example


```python
import wallet
from wallet.models.wt_menu_option_group import WTMenuOptionGroup
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
    api_instance = wallet.MenusApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # List option groups
        api_response = api_instance.fetch_menu_option_groups(is_archive_included=is_archive_included)
        print("The response of MenusApi->fetch_menu_option_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->fetch_menu_option_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTMenuOptionGroup]**](WTMenuOptionGroup.md)

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

# **fetch_menus**
> List[WTMenu] fetch_menus(is_archive_included=is_archive_included)

List menus

### Example


```python
import wallet
from wallet.models.wt_menu import WTMenu
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
    api_instance = wallet.MenusApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # List menus
        api_response = api_instance.fetch_menus(is_archive_included=is_archive_included)
        print("The response of MenusApi->fetch_menus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->fetch_menus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTMenu]**](WTMenu.md)

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

# **restore_menu**
> WTMenu restore_menu(id)

Restore a menu

### Example


```python
import wallet
from wallet.models.wt_menu import WTMenu
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore a menu
        api_response = api_instance.restore_menu(id)
        print("The response of MenusApi->restore_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->restore_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenu**](WTMenu.md)

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

# **restore_menu_item**
> WTMenuItem restore_menu_item(id)

Restore a menu item

### Example


```python
import wallet
from wallet.models.wt_menu_item import WTMenuItem
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore a menu item
        api_response = api_instance.restore_menu_item(id)
        print("The response of MenusApi->restore_menu_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->restore_menu_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenuItem**](WTMenuItem.md)

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

# **restore_menu_option_group**
> WTMenuOptionGroup restore_menu_option_group(id)

Restore an option group

### Example


```python
import wallet
from wallet.models.wt_menu_option_group import WTMenuOptionGroup
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore an option group
        api_response = api_instance.restore_menu_option_group(id)
        print("The response of MenusApi->restore_menu_option_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->restore_menu_option_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMenuOptionGroup**](WTMenuOptionGroup.md)

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

# **update_menu**
> WTMenu update_menu(id, wt_menu_update_params)

Update a menu

### Example


```python
import wallet
from wallet.models.wt_menu import WTMenu
from wallet.models.wt_menu_update_params import WTMenuUpdateParams
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 
    wt_menu_update_params = wallet.WTMenuUpdateParams() # WTMenuUpdateParams | 

    try:
        # Update a menu
        api_response = api_instance.update_menu(id, wt_menu_update_params)
        print("The response of MenusApi->update_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->update_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_menu_update_params** | [**WTMenuUpdateParams**](WTMenuUpdateParams.md)|  | 

### Return type

[**WTMenu**](WTMenu.md)

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

# **update_menu_item**
> WTMenuItem update_menu_item(id, wt_menu_item_update_params)

Update a menu item

### Example


```python
import wallet
from wallet.models.wt_menu_item import WTMenuItem
from wallet.models.wt_menu_item_update_params import WTMenuItemUpdateParams
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 
    wt_menu_item_update_params = wallet.WTMenuItemUpdateParams() # WTMenuItemUpdateParams | 

    try:
        # Update a menu item
        api_response = api_instance.update_menu_item(id, wt_menu_item_update_params)
        print("The response of MenusApi->update_menu_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->update_menu_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_menu_item_update_params** | [**WTMenuItemUpdateParams**](WTMenuItemUpdateParams.md)|  | 

### Return type

[**WTMenuItem**](WTMenuItem.md)

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

# **update_menu_option_group**
> WTMenuOptionGroup update_menu_option_group(id, wt_menu_option_group_update_params)

Update an option group

### Example


```python
import wallet
from wallet.models.wt_menu_option_group import WTMenuOptionGroup
from wallet.models.wt_menu_option_group_update_params import WTMenuOptionGroupUpdateParams
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
    api_instance = wallet.MenusApi(api_client)
    id = 'id_example' # str | 
    wt_menu_option_group_update_params = wallet.WTMenuOptionGroupUpdateParams() # WTMenuOptionGroupUpdateParams | 

    try:
        # Update an option group
        api_response = api_instance.update_menu_option_group(id, wt_menu_option_group_update_params)
        print("The response of MenusApi->update_menu_option_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenusApi->update_menu_option_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_menu_option_group_update_params** | [**WTMenuOptionGroupUpdateParams**](WTMenuOptionGroupUpdateParams.md)|  | 

### Return type

[**WTMenuOptionGroup**](WTMenuOptionGroup.md)

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

