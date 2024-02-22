# wallet.VideosApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_video**](VideosApi.md#archive_video) | **DELETE** /v2/video/{id} | Archive video
[**create_video**](VideosApi.md#create_video) | **POST** /v2/video | Create video
[**fetch_all_video**](VideosApi.md#fetch_all_video) | **GET** /v2/video/all | Fetch all video
[**restore_video**](VideosApi.md#restore_video) | **PATCH** /v2/video/{id} | Restore video
[**update_video**](VideosApi.md#update_video) | **PUT** /v2/video/{id} | Update video


# **archive_video**
> Video archive_video(id)

Archive video

### Example


```python
import wallet
from wallet.models.video import Video
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
    api_instance = wallet.VideosApi(api_client)
    id = None # object | 

    try:
        # Archive video
        api_response = api_instance.archive_video(id)
        print("The response of VideosApi->archive_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->archive_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Video**](Video.md)

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

# **create_video**
> Video create_video(wt_video_create_params)

Create video

### Example


```python
import wallet
from wallet.models.video import Video
from wallet.models.wt_video_create_params import WTVideoCreateParams
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
    api_instance = wallet.VideosApi(api_client)
    wt_video_create_params = wallet.WTVideoCreateParams() # WTVideoCreateParams | 

    try:
        # Create video
        api_response = api_instance.create_video(wt_video_create_params)
        print("The response of VideosApi->create_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->create_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_video_create_params** | [**WTVideoCreateParams**](WTVideoCreateParams.md)|  | 

### Return type

[**Video**](Video.md)

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

# **fetch_all_video**
> object fetch_all_video(is_archive_included=is_archive_included)

Fetch all video

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
    api_instance = wallet.VideosApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all video
        api_response = api_instance.fetch_all_video(is_archive_included=is_archive_included)
        print("The response of VideosApi->fetch_all_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->fetch_all_video: %s\n" % e)
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

# **restore_video**
> Video restore_video(id)

Restore video

### Example


```python
import wallet
from wallet.models.video import Video
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
    api_instance = wallet.VideosApi(api_client)
    id = None # object | 

    try:
        # Restore video
        api_response = api_instance.restore_video(id)
        print("The response of VideosApi->restore_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->restore_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Video**](Video.md)

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

# **update_video**
> Video update_video(id, wt_video_update_params)

Update video

### Example


```python
import wallet
from wallet.models.video import Video
from wallet.models.wt_video_update_params import WTVideoUpdateParams
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
    api_instance = wallet.VideosApi(api_client)
    id = None # object | 
    wt_video_update_params = wallet.WTVideoUpdateParams() # WTVideoUpdateParams | 

    try:
        # Update video
        api_response = api_instance.update_video(id, wt_video_update_params)
        print("The response of VideosApi->update_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->update_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_video_update_params** | [**WTVideoUpdateParams**](WTVideoUpdateParams.md)|  | 

### Return type

[**Video**](Video.md)

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

