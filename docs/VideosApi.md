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
import time
import wallet
from wallet.api import videos_api
from wallet.model.video import Video
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
    api_instance = videos_api.VideosApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive video
        api_response = api_instance.archive_video(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VideosApi->archive_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import videos_api
from wallet.model.video import Video
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_video_create_params import WTVideoCreateParams
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
    api_instance = videos_api.VideosApi(api_client)
    wt_video_create_params = WTVideoCreateParams(
        title="This is the title of the video",
        description="This is the description of the video",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.mp4",
        additional_info_url="https://your-site.com/videos/steak-house",
    ) # WTVideoCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create video
        api_response = api_instance.create_video(wt_video_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
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
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_video()

Fetch all video

### Example


```python
import time
import wallet
from wallet.api import videos_api
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
    api_instance = videos_api.VideosApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all video
        api_response = api_instance.fetch_all_video(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VideosApi->fetch_all_video: %s\n" % e)
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

# **restore_video**
> Video restore_video(id)

Restore video

### Example


```python
import time
import wallet
from wallet.api import videos_api
from wallet.model.video import Video
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
    api_instance = videos_api.VideosApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore video
        api_response = api_instance.restore_video(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VideosApi->restore_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import videos_api
from wallet.model.video import Video
from wallet.model.internal_server_error import InternalServerError
from wallet.model.wt_video_update_params import WTVideoUpdateParams
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
    api_instance = videos_api.VideosApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_video_update_params = WTVideoUpdateParams(
        title="This is the title of the video",
        description="This is the description of the video",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.mp4",
        additional_info_url="https://your-site.com/videos/steak-house",
    ) # WTVideoUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update video
        api_response = api_instance.update_video(id, wt_video_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VideosApi->update_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

