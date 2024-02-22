# wallet.QRCodeDesignsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_qr_code_design**](QRCodeDesignsApi.md#archive_qr_code_design) | **DELETE** /v2/qrcodedesign/{id} | Archive QR Code Design
[**create_qr_code_design**](QRCodeDesignsApi.md#create_qr_code_design) | **POST** /v2/qrcodedesign | Create QR Code design
[**fetch_all_qr_code_designs**](QRCodeDesignsApi.md#fetch_all_qr_code_designs) | **GET** /v2/qrcodedesign/all | Fetch all active QR Code Designs
[**fetch_qr_code_design_by_id**](QRCodeDesignsApi.md#fetch_qr_code_design_by_id) | **GET** /v2/qrcodedesign/{id} | Fetch QR Code Design
[**restore_qr_code_design**](QRCodeDesignsApi.md#restore_qr_code_design) | **PATCH** /v2/qrcodedesign/{id} | Restore payment design
[**update_qr_code_design**](QRCodeDesignsApi.md#update_qr_code_design) | **PUT** /v2/qrcodedesign/{id} | Update QR Code Design


# **archive_qr_code_design**
> WTQRCodeDesign archive_qr_code_design(id)

Archive QR Code Design

### Example


```python
import wallet
from wallet.models.wtqr_code_design import WTQRCodeDesign
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
    api_instance = wallet.QRCodeDesignsApi(api_client)
    id = None # object | 

    try:
        # Archive QR Code Design
        api_response = api_instance.archive_qr_code_design(id)
        print("The response of QRCodeDesignsApi->archive_qr_code_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodeDesignsApi->archive_qr_code_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTQRCodeDesign**](WTQRCodeDesign.md)

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

# **create_qr_code_design**
> WTQRCodeDesign create_qr_code_design(wtqr_code_design_create_params)

Create QR Code design

### Example


```python
import wallet
from wallet.models.wtqr_code_design import WTQRCodeDesign
from wallet.models.wtqr_code_design_create_params import WTQRCodeDesignCreateParams
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
    api_instance = wallet.QRCodeDesignsApi(api_client)
    wtqr_code_design_create_params = wallet.WTQRCodeDesignCreateParams() # WTQRCodeDesignCreateParams | 

    try:
        # Create QR Code design
        api_response = api_instance.create_qr_code_design(wtqr_code_design_create_params)
        print("The response of QRCodeDesignsApi->create_qr_code_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodeDesignsApi->create_qr_code_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wtqr_code_design_create_params** | [**WTQRCodeDesignCreateParams**](WTQRCodeDesignCreateParams.md)|  | 

### Return type

[**WTQRCodeDesign**](WTQRCodeDesign.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failed |  -  |
**409** | Duplicate Row Found |  -  |
**422** | Validation Failed |  -  |
**424** | Merchant Not Initialized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_qr_code_designs**
> List[WTQRCodeDesign] fetch_all_qr_code_designs(is_archive_included=is_archive_included)

Fetch all active QR Code Designs

### Example


```python
import wallet
from wallet.models.wtqr_code_design import WTQRCodeDesign
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
    api_instance = wallet.QRCodeDesignsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all active QR Code Designs
        api_response = api_instance.fetch_all_qr_code_designs(is_archive_included=is_archive_included)
        print("The response of QRCodeDesignsApi->fetch_all_qr_code_designs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodeDesignsApi->fetch_all_qr_code_designs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTQRCodeDesign]**](WTQRCodeDesign.md)

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

# **fetch_qr_code_design_by_id**
> WTQRCodeDesign fetch_qr_code_design_by_id(id)

Fetch QR Code Design

### Example


```python
import wallet
from wallet.models.wtqr_code_design import WTQRCodeDesign
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
    api_instance = wallet.QRCodeDesignsApi(api_client)
    id = None # object | 

    try:
        # Fetch QR Code Design
        api_response = api_instance.fetch_qr_code_design_by_id(id)
        print("The response of QRCodeDesignsApi->fetch_qr_code_design_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodeDesignsApi->fetch_qr_code_design_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTQRCodeDesign**](WTQRCodeDesign.md)

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

# **restore_qr_code_design**
> QRCodeDesign restore_qr_code_design(id)

Restore payment design

### Example


```python
import wallet
from wallet.models.qr_code_design import QRCodeDesign
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
    api_instance = wallet.QRCodeDesignsApi(api_client)
    id = None # object | 

    try:
        # Restore payment design
        api_response = api_instance.restore_qr_code_design(id)
        print("The response of QRCodeDesignsApi->restore_qr_code_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodeDesignsApi->restore_qr_code_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**QRCodeDesign**](QRCodeDesign.md)

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

# **update_qr_code_design**
> WTQRCodeDesign update_qr_code_design(id, wtqr_code_design_update_params)

Update QR Code Design

### Example


```python
import wallet
from wallet.models.wtqr_code_design import WTQRCodeDesign
from wallet.models.wtqr_code_design_update_params import WTQRCodeDesignUpdateParams
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
    api_instance = wallet.QRCodeDesignsApi(api_client)
    id = None # object | 
    wtqr_code_design_update_params = wallet.WTQRCodeDesignUpdateParams() # WTQRCodeDesignUpdateParams | 

    try:
        # Update QR Code Design
        api_response = api_instance.update_qr_code_design(id, wtqr_code_design_update_params)
        print("The response of QRCodeDesignsApi->update_qr_code_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QRCodeDesignsApi->update_qr_code_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wtqr_code_design_update_params** | [**WTQRCodeDesignUpdateParams**](WTQRCodeDesignUpdateParams.md)|  | 

### Return type

[**WTQRCodeDesign**](WTQRCodeDesign.md)

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
**409** | Duplicate Row Found |  -  |
**422** | Validation Failed |  -  |
**424** | Foreign Key does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

