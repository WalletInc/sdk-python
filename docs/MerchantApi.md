# wallet.MerchantApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_merchant_profile**](MerchantApi.md#archive_merchant_profile) | **DELETE** /v2/merchant/delete | Archive Merchant
[**fetch_custom_roles**](MerchantApi.md#fetch_custom_roles) | **GET** /v2/merchant/roles/custom | Get custom roles
[**fetch_employees**](MerchantApi.md#fetch_employees) | **GET** /v2/merchant/employees/all | Get all employees
[**fetch_public_employees**](MerchantApi.md#fetch_public_employees) | **GET** /v2/merchant/employees/public | Get public representative employees of the merchant
[**fetch_wallet_configuration**](MerchantApi.md#fetch_wallet_configuration) | **GET** /v2/merchant/wallet/configuration | Get wallet configuration
[**update_merchant**](MerchantApi.md#update_merchant) | **PUT** /v2/merchant | Update merchant details
[**update_points_of_contact**](MerchantApi.md#update_points_of_contact) | **PUT** /v2/merchant/pointsOfContact | Update points of contact
[**update_pos_integration**](MerchantApi.md#update_pos_integration) | **PUT** /v2/merchant/pos/integration | Update POS Integration


# **archive_merchant_profile**
> object archive_merchant_profile()

Archive Merchant

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Archive Merchant
        api_response = api_instance.archive_merchant_profile()
        print("The response of MerchantApi->archive_merchant_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->archive_merchant_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **fetch_custom_roles**
> object fetch_custom_roles()

Get custom roles

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Get custom roles
        api_response = api_instance.fetch_custom_roles()
        print("The response of MerchantApi->fetch_custom_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_custom_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **fetch_employees**
> object fetch_employees()

Get all employees

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Get all employees
        api_response = api_instance.fetch_employees()
        print("The response of MerchantApi->fetch_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_employees: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **fetch_public_employees**
> object fetch_public_employees()

Get public representative employees of the merchant

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Get public representative employees of the merchant
        api_response = api_instance.fetch_public_employees()
        print("The response of MerchantApi->fetch_public_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_public_employees: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **fetch_wallet_configuration**
> object fetch_wallet_configuration()

Get wallet configuration

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Get wallet configuration
        api_response = api_instance.fetch_wallet_configuration()
        print("The response of MerchantApi->fetch_wallet_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_wallet_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **update_merchant**
> object update_merchant(wt_merchant_update)

Update merchant details

### Example


```python
import wallet
from wallet.models.wt_merchant_update import WTMerchantUpdate
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
    api_instance = wallet.MerchantApi(api_client)
    wt_merchant_update = wallet.WTMerchantUpdate() # WTMerchantUpdate | 

    try:
        # Update merchant details
        api_response = api_instance.update_merchant(wt_merchant_update)
        print("The response of MerchantApi->update_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->update_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update** | [**WTMerchantUpdate**](WTMerchantUpdate.md)|  | 

### Return type

**object**

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

# **update_points_of_contact**
> object update_points_of_contact(wt_merchant_update_points_of_contact)

Update points of contact

### Example


```python
import wallet
from wallet.models.wt_merchant_update_points_of_contact import WTMerchantUpdatePointsOfContact
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
    api_instance = wallet.MerchantApi(api_client)
    wt_merchant_update_points_of_contact = wallet.WTMerchantUpdatePointsOfContact() # WTMerchantUpdatePointsOfContact | 

    try:
        # Update points of contact
        api_response = api_instance.update_points_of_contact(wt_merchant_update_points_of_contact)
        print("The response of MerchantApi->update_points_of_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->update_points_of_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update_points_of_contact** | [**WTMerchantUpdatePointsOfContact**](WTMerchantUpdatePointsOfContact.md)|  | 

### Return type

**object**

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

# **update_pos_integration**
> object update_pos_integration(wt_merchant_update_pos_integration)

Update POS Integration

### Example


```python
import wallet
from wallet.models.wt_merchant_update_pos_integration import WTMerchantUpdatePOSIntegration
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
    api_instance = wallet.MerchantApi(api_client)
    wt_merchant_update_pos_integration = wallet.WTMerchantUpdatePOSIntegration() # WTMerchantUpdatePOSIntegration | 

    try:
        # Update POS Integration
        api_response = api_instance.update_pos_integration(wt_merchant_update_pos_integration)
        print("The response of MerchantApi->update_pos_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->update_pos_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update_pos_integration** | [**WTMerchantUpdatePOSIntegration**](WTMerchantUpdatePOSIntegration.md)|  | 

### Return type

**object**

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

