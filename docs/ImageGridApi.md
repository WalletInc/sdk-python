# wallet.ImageGridApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_image_grid**](ImageGridApi.md#archive_image_grid) | **DELETE** /v2/imageGrid/{id} | Archive image
[**create_image_grid**](ImageGridApi.md#create_image_grid) | **POST** /v2/imageGrid | Create image
[**fetch_all_image_grid**](ImageGridApi.md#fetch_all_image_grid) | **GET** /v2/imageGrid/all | Fetch all images
[**restore_image_grid**](ImageGridApi.md#restore_image_grid) | **PATCH** /v2/imageGrid/{id} | Restore image
[**update_image_grid**](ImageGridApi.md#update_image_grid) | **PUT** /v2/imageGrid/{id} | Update image


# **archive_image_grid**
> ImageGrid archive_image_grid(id)

Archive image

### Example


```python
import time
import wallet
from wallet.api import image_grid_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.image_grid import ImageGrid
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
    api_instance = image_grid_api.ImageGridApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive image
        api_response = api_instance.archive_image_grid(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ImageGridApi->archive_image_grid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**ImageGrid**](ImageGrid.md)

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

# **create_image_grid**
> ImageGrid create_image_grid(wt_image_grid_create_params)

Create image

### Example


```python
import time
import wallet
from wallet.api import image_grid_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.image_grid import ImageGrid
from wallet.model.wt_image_grid_create_params import WTImageGridCreateParams
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
    api_instance = image_grid_api.ImageGridApi(api_client)
    wt_image_grid_create_params = WTImageGridCreateParams(
        title="This is the title of the image",
        url="https://example.com",
        media_url="https://example.com/image.gif",
        sequence_number=1,
        is_pinned=True,
    ) # WTImageGridCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create image
        api_response = api_instance.create_image_grid(wt_image_grid_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ImageGridApi->create_image_grid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_image_grid_create_params** | [**WTImageGridCreateParams**](WTImageGridCreateParams.md)|  |

### Return type

[**ImageGrid**](ImageGrid.md)

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

# **fetch_all_image_grid**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_image_grid()

Fetch all images

### Example


```python
import time
import wallet
from wallet.api import image_grid_api
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
    api_instance = image_grid_api.ImageGridApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all images
        api_response = api_instance.fetch_all_image_grid(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ImageGridApi->fetch_all_image_grid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

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

# **restore_image_grid**
> ImageGrid restore_image_grid(id)

Restore image

### Example


```python
import time
import wallet
from wallet.api import image_grid_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.image_grid import ImageGrid
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
    api_instance = image_grid_api.ImageGridApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore image
        api_response = api_instance.restore_image_grid(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ImageGridApi->restore_image_grid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**ImageGrid**](ImageGrid.md)

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

# **update_image_grid**
> ImageGrid update_image_grid(id, wt_image_grid_update_params)

Update image

### Example


```python
import time
import wallet
from wallet.api import image_grid_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.image_grid import ImageGrid
from wallet.model.wt_image_grid_update_params import WTImageGridUpdateParams
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
    api_instance = image_grid_api.ImageGridApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_image_grid_update_params = WTImageGridUpdateParams(
        title="This is the title of the image",
        url="https://example.com",
        media_url="https://example.com/image.gif",
        sequence_number=1,
        is_pinned=True,
    ) # WTImageGridUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update image
        api_response = api_instance.update_image_grid(id, wt_image_grid_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ImageGridApi->update_image_grid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_image_grid_update_params** | [**WTImageGridUpdateParams**](WTImageGridUpdateParams.md)|  |

### Return type

[**ImageGrid**](ImageGrid.md)

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

