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
import wallet
from wallet.models.amenity import Amenity
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
    api_instance = wallet.AmenitiesApi(api_client)
    id = None # object | 

    try:
        # Archive amenity
        api_response = api_instance.archive_amenity(id)
        print("The response of AmenitiesApi->archive_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->archive_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.amenity import Amenity
from wallet.models.wt_amenity_create_params import WTAmenityCreateParams
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
    api_instance = wallet.AmenitiesApi(api_client)
    wt_amenity_create_params = wallet.WTAmenityCreateParams() # WTAmenityCreateParams | 

    try:
        # Create amenity
        api_response = api_instance.create_amenity(wt_amenity_create_params)
        print("The response of AmenitiesApi->create_amenity:\n")
        pprint(api_response)
    except Exception as e:
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
> object fetch_all_amenities(is_archive_included=is_archive_included)

Fetch all amenities

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
    api_instance = wallet.AmenitiesApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all amenities
        api_response = api_instance.fetch_all_amenities(is_archive_included=is_archive_included)
        print("The response of AmenitiesApi->fetch_all_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->fetch_all_amenities: %s\n" % e)
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

# **restore_amenity**
> Amenity restore_amenity(id)

Restore amenity

### Example


```python
import wallet
from wallet.models.amenity import Amenity
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
    api_instance = wallet.AmenitiesApi(api_client)
    id = None # object | 

    try:
        # Restore amenity
        api_response = api_instance.restore_amenity(id)
        print("The response of AmenitiesApi->restore_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->restore_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.amenity import Amenity
from wallet.models.wt_amenity_update_params import WTAmenityUpdateParams
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
    api_instance = wallet.AmenitiesApi(api_client)
    id = None # object | 
    wt_amenity_update_params = wallet.WTAmenityUpdateParams() # WTAmenityUpdateParams | 

    try:
        # Update amenity
        api_response = api_instance.update_amenity(id, wt_amenity_update_params)
        print("The response of AmenitiesApi->update_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->update_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
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

