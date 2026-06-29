# wallet.GalleryApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_image_grid**](GalleryApi.md#archive_image_grid) | **DELETE** /v2/imageGrid/{id} | Archive Gallery Image
[**create_image_grid**](GalleryApi.md#create_image_grid) | **POST** /v2/imageGrid | Create Gallery Image
[**fetch_all_image_grid**](GalleryApi.md#fetch_all_image_grid) | **GET** /v2/imageGrid/all | Get all Gallery Images
[**restore_image_grid**](GalleryApi.md#restore_image_grid) | **PATCH** /v2/imageGrid/{id} | Restore Gallery Image
[**update_image_grid**](GalleryApi.md#update_image_grid) | **PUT** /v2/imageGrid/{id} | Update Gallery Image


# **archive_image_grid**
> ImageGrid archive_image_grid(id)

Archive Gallery Image

### Example


```python
import wallet
from wallet.models.image_grid import ImageGrid
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
    api_instance = wallet.GalleryApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Gallery Image
        api_response = api_instance.archive_image_grid(id)
        print("The response of GalleryApi->archive_image_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GalleryApi->archive_image_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Create Gallery Image

### Example


```python
import wallet
from wallet.models.image_grid import ImageGrid
from wallet.models.wt_image_grid_create_params import WTImageGridCreateParams
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
    api_instance = wallet.GalleryApi(api_client)
    wt_image_grid_create_params = wallet.WTImageGridCreateParams() # WTImageGridCreateParams | 

    try:
        # Create Gallery Image
        api_response = api_instance.create_image_grid(wt_image_grid_create_params)
        print("The response of GalleryApi->create_image_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GalleryApi->create_image_grid: %s\n" % e)
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
> object fetch_all_image_grid(is_archive_included=is_archive_included)

Get all Gallery Images

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
    api_instance = wallet.GalleryApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Gallery Images
        api_response = api_instance.fetch_all_image_grid(is_archive_included=is_archive_included)
        print("The response of GalleryApi->fetch_all_image_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GalleryApi->fetch_all_image_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

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

# **restore_image_grid**
> ImageGrid restore_image_grid(id)

Restore Gallery Image

### Example


```python
import wallet
from wallet.models.image_grid import ImageGrid
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
    api_instance = wallet.GalleryApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Gallery Image
        api_response = api_instance.restore_image_grid(id)
        print("The response of GalleryApi->restore_image_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GalleryApi->restore_image_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Update Gallery Image

### Example


```python
import wallet
from wallet.models.image_grid import ImageGrid
from wallet.models.wt_image_grid_update_params import WTImageGridUpdateParams
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
    api_instance = wallet.GalleryApi(api_client)
    id = 'id_example' # str | 
    wt_image_grid_update_params = wallet.WTImageGridUpdateParams() # WTImageGridUpdateParams | 

    try:
        # Update Gallery Image
        api_response = api_instance.update_image_grid(id, wt_image_grid_update_params)
        print("The response of GalleryApi->update_image_grid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GalleryApi->update_image_grid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

