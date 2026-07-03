# wallet.VideosApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_video**](VideosApi.md#archive_video) | **DELETE** /v2/video/{id} | Archive Video
[**create_video**](VideosApi.md#create_video) | **POST** /v2/video | Create Video
[**fetch_all_video**](VideosApi.md#fetch_all_video) | **GET** /v2/video/all | Get all Videos
[**presign_video_upload**](VideosApi.md#presign_video_upload) | **POST** /v2/video/presign | Presign a direct-to-R2 video upload
[**restore_video**](VideosApi.md#restore_video) | **PATCH** /v2/video/{id} | Restore Video
[**update_video**](VideosApi.md#update_video) | **PUT** /v2/video/{id} | Update Video


# **archive_video**
> Video archive_video(id)

Archive Video

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
    id = 'id_example' # str | 

    try:
        # Archive Video
        api_response = api_instance.archive_video(id)
        print("The response of VideosApi->archive_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->archive_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Create Video

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
        # Create Video
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

Get all Videos

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
        # Get all Videos
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

# **presign_video_upload**
> WTVideoUploadPresign presign_video_upload(wt_video_upload_presign_params)

Presign a direct-to-R2 video upload

### Example


```python
import wallet
from wallet.models.wt_video_upload_presign import WTVideoUploadPresign
from wallet.models.wt_video_upload_presign_params import WTVideoUploadPresignParams
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
    wt_video_upload_presign_params = wallet.WTVideoUploadPresignParams() # WTVideoUploadPresignParams | 

    try:
        # Presign a direct-to-R2 video upload
        api_response = api_instance.presign_video_upload(wt_video_upload_presign_params)
        print("The response of VideosApi->presign_video_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->presign_video_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_video_upload_presign_params** | [**WTVideoUploadPresignParams**](WTVideoUploadPresignParams.md)|  | 

### Return type

[**WTVideoUploadPresign**](WTVideoUploadPresign.md)

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

# **restore_video**
> Video restore_video(id)

Restore Video

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
    id = 'id_example' # str | 

    try:
        # Restore Video
        api_response = api_instance.restore_video(id)
        print("The response of VideosApi->restore_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->restore_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Update Video

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
    id = 'id_example' # str | 
    wt_video_update_params = wallet.WTVideoUpdateParams() # WTVideoUpdateParams | 

    try:
        # Update Video
        api_response = api_instance.update_video(id, wt_video_update_params)
        print("The response of VideosApi->update_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->update_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

