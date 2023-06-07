# wallet.AmenitiesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_amenity**](AmenitiesApi.md#archive_amenity) | **DELETE** /v2/amenities/{id} | Archive amenity
[**create_amenity**](AmenitiesApi.md#create_amenity) | **POST** /v2/amenities | Create amenity
[**fetch_all_amenities**](AmenitiesApi.md#fetch_all_amenities) | **GET** /v2/amenities/all | Fetch all amenities
[**restore_amenity**](AmenitiesApi.md#restore_amenity) | **PATCH** /v2/amenities/{id} | Restore amenity
[**update_amenity**](AmenitiesApi.md#update_amenity) | **PUT** /v2/amenities/{id} | Update amenity


# **archive_amenity**
> Amenity archive_amenity(id)

Archive amenity

### Example


```python
import time
import wallet
from wallet.api import amenities_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.amenity import Amenity
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
    api_instance = amenities_api.AmenitiesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive amenity
        api_response = api_instance.archive_amenity(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AmenitiesApi->archive_amenity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Amenity**](Amenity.md)

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

# **create_amenity**
> Amenity create_amenity(wt_amenity_create_params)

Create amenity

### Example


```python
import time
import wallet
from wallet.api import amenities_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_amenity_create_params import WTAmenityCreateParams
from wallet.model.amenity import Amenity
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
    api_instance = amenities_api.AmenitiesApi(api_client)
    wt_amenity_create_params = WTAmenityCreateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        display_value="20% Off!",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
    ) # WTAmenityCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create amenity
        api_response = api_instance.create_amenity(wt_amenity_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AmenitiesApi->create_amenity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_amenity_create_params** | [**WTAmenityCreateParams**](WTAmenityCreateParams.md)|  |

### Return type

[**Amenity**](Amenity.md)

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

# **fetch_all_amenities**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_amenities()

Fetch all amenities

### Example


```python
import time
import wallet
from wallet.api import amenities_api
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
    api_instance = amenities_api.AmenitiesApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all amenities
        api_response = api_instance.fetch_all_amenities(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AmenitiesApi->fetch_all_amenities: %s\n" % e)
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

# **restore_amenity**
> Amenity restore_amenity(id)

Restore amenity

### Example


```python
import time
import wallet
from wallet.api import amenities_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.amenity import Amenity
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
    api_instance = amenities_api.AmenitiesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore amenity
        api_response = api_instance.restore_amenity(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AmenitiesApi->restore_amenity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Amenity**](Amenity.md)

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

# **update_amenity**
> Amenity update_amenity(id, wt_amenity_update_params)

Update amenity

### Example


```python
import time
import wallet
from wallet.api import amenities_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.amenity import Amenity
from wallet.model.wt_amenity_update_params import WTAmenityUpdateParams
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
    api_instance = amenities_api.AmenitiesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_amenity_update_params = WTAmenityUpdateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        display_value="20% Off!",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
    ) # WTAmenityUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update amenity
        api_response = api_instance.update_amenity(id, wt_amenity_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AmenitiesApi->update_amenity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_amenity_update_params** | [**WTAmenityUpdateParams**](WTAmenityUpdateParams.md)|  |

### Return type

[**Amenity**](Amenity.md)

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

