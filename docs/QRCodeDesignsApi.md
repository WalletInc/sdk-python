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
import time
import wallet
from wallet.api import qr_code_designs_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wtqr_code_design import WTQRCodeDesign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = qr_code_designs_api.QRCodeDesignsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive QR Code Design
        api_response = api_instance.archive_qr_code_design(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling QRCodeDesignsApi->archive_qr_code_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import qr_code_designs_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.merchant_not_initialized import MerchantNotInitialized
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wtqr_code_design import WTQRCodeDesign
from wallet.model.duplicate_row_found import DuplicateRowFound
from wallet.model.wtqr_code_design_create_params import WTQRCodeDesignCreateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = qr_code_designs_api.QRCodeDesignsApi(api_client)
    wtqr_code_design_create_params = WTQRCodeDesignCreateParams(
        name="This is the name of the design",
        size=1,
        margin=1,
        corner_radius=1,
        color_dark_hex="#000",
        color_light_hex="#ffffff",
        background_dimming_hex="#ffffff",
        logo_image_url="#ffffff",
        background_image_url="#ffffff",
        animated_gif_background_url="#ffffff",
    ) # WTQRCodeDesignCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create QR Code design
        api_response = api_instance.create_qr_code_design(wtqr_code_design_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
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
> [WTQRCodeDesign] fetch_all_qr_code_designs()

Fetch all active QR Code Designs

### Example


```python
import time
import wallet
from wallet.api import qr_code_designs_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wtqr_code_design import WTQRCodeDesign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = qr_code_designs_api.QRCodeDesignsApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all active QR Code Designs
        api_response = api_instance.fetch_all_qr_code_designs(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling QRCodeDesignsApi->fetch_all_qr_code_designs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[WTQRCodeDesign]**](WTQRCodeDesign.md)

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
import time
import wallet
from wallet.api import qr_code_designs_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wtqr_code_design import WTQRCodeDesign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = qr_code_designs_api.QRCodeDesignsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch QR Code Design
        api_response = api_instance.fetch_qr_code_design_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling QRCodeDesignsApi->fetch_qr_code_design_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import qr_code_designs_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.qr_code_design import QRCodeDesign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = qr_code_designs_api.QRCodeDesignsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore payment design
        api_response = api_instance.restore_qr_code_design(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling QRCodeDesignsApi->restore_qr_code_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import qr_code_designs_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
from wallet.model.wtqr_code_design_update_params import WTQRCodeDesignUpdateParams
from wallet.model.wtqr_code_design import WTQRCodeDesign
from wallet.model.duplicate_row_found import DuplicateRowFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = qr_code_designs_api.QRCodeDesignsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wtqr_code_design_update_params = WTQRCodeDesignUpdateParams(
        name="This is the name of the design",
        size=1,
        margin=1,
        corner_radius=1,
        color_dark_hex="#000",
        color_light_hex="#ffffff",
        background_dimming_hex="#ffffff",
        logo_image_url="#ffffff",
        background_image_url="#ffffff",
        animated_gif_background_url="#ffffff",
    ) # WTQRCodeDesignUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update QR Code Design
        api_response = api_instance.update_qr_code_design(id, wtqr_code_design_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling QRCodeDesignsApi->update_qr_code_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

