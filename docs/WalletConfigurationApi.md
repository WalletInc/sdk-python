# wallet.WalletConfigurationApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_pass_style**](WalletConfigurationApi.md#fetch_pass_style) | **GET** /wallet/passStyle | Get pass styling
[**generate_android_keystore**](WalletConfigurationApi.md#generate_android_keystore) | **POST** /v2/wallet/android/keystore | Generate Android TWA signing keystore
[**reset_pass_style**](WalletConfigurationApi.md#reset_pass_style) | **DELETE** /wallet/passStyle/{provider} | Reset one provider&#39;s pass styling
[**save_merchant_credit_payment_design**](WalletConfigurationApi.md#save_merchant_credit_payment_design) | **PUT** /v2/wallet/merchantCredit/paymentDesign | Update payment design for merchant credits
[**save_wallet_record**](WalletConfigurationApi.md#save_wallet_record) | **PUT** /v2/wallet | Update wallet record


# **fetch_pass_style**
> WTPassStyleResponse fetch_pass_style()

Get pass styling

### Example


```python
import wallet
from wallet.models.wt_pass_style_response import WTPassStyleResponse
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
    api_instance = wallet.WalletConfigurationApi(api_client)

    try:
        # Get pass styling
        api_response = api_instance.fetch_pass_style()
        print("The response of WalletConfigurationApi->fetch_pass_style:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletConfigurationApi->fetch_pass_style: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WTPassStyleResponse**](WTPassStyleResponse.md)

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

# **generate_android_keystore**
> WTAndroidKeystoreResponse generate_android_keystore(regenerate=regenerate)

Generate Android TWA signing keystore

### Example


```python
import wallet
from wallet.models.wt_android_keystore_response import WTAndroidKeystoreResponse
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
    api_instance = wallet.WalletConfigurationApi(api_client)
    regenerate = True # bool |  (optional)

    try:
        # Generate Android TWA signing keystore
        api_response = api_instance.generate_android_keystore(regenerate=regenerate)
        print("The response of WalletConfigurationApi->generate_android_keystore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletConfigurationApi->generate_android_keystore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regenerate** | **bool**|  | [optional] 

### Return type

[**WTAndroidKeystoreResponse**](WTAndroidKeystoreResponse.md)

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

# **reset_pass_style**
> WTPassStyleResponse reset_pass_style(provider)

Reset one provider's pass styling

### Example


```python
import wallet
from wallet.models.wt_pass_style_response import WTPassStyleResponse
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
    api_instance = wallet.WalletConfigurationApi(api_client)
    provider = wallet.WTWalletPassProvider() # WTWalletPassProvider | 

    try:
        # Reset one provider's pass styling
        api_response = api_instance.reset_pass_style(provider)
        print("The response of WalletConfigurationApi->reset_pass_style:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletConfigurationApi->reset_pass_style: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**WTWalletPassProvider**](.md)|  | 

### Return type

[**WTPassStyleResponse**](WTPassStyleResponse.md)

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

# **save_merchant_credit_payment_design**
> object save_merchant_credit_payment_design(save_merchant_credit_payment_design_request)

Update payment design for merchant credits

### Example


```python
import wallet
from wallet.models.save_merchant_credit_payment_design_request import SaveMerchantCreditPaymentDesignRequest
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
    api_instance = wallet.WalletConfigurationApi(api_client)
    save_merchant_credit_payment_design_request = wallet.SaveMerchantCreditPaymentDesignRequest() # SaveMerchantCreditPaymentDesignRequest | 

    try:
        # Update payment design for merchant credits
        api_response = api_instance.save_merchant_credit_payment_design(save_merchant_credit_payment_design_request)
        print("The response of WalletConfigurationApi->save_merchant_credit_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletConfigurationApi->save_merchant_credit_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_merchant_credit_payment_design_request** | [**SaveMerchantCreditPaymentDesignRequest**](SaveMerchantCreditPaymentDesignRequest.md)|  | 

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

# **save_wallet_record**
> object save_wallet_record(wt_wallet_configuration_save_wallet_record)

Update wallet record

### Example


```python
import wallet
from wallet.models.wt_wallet_configuration_save_wallet_record import WTWalletConfigurationSaveWalletRecord
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
    api_instance = wallet.WalletConfigurationApi(api_client)
    wt_wallet_configuration_save_wallet_record = wallet.WTWalletConfigurationSaveWalletRecord() # WTWalletConfigurationSaveWalletRecord | 

    try:
        # Update wallet record
        api_response = api_instance.save_wallet_record(wt_wallet_configuration_save_wallet_record)
        print("The response of WalletConfigurationApi->save_wallet_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletConfigurationApi->save_wallet_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_wallet_configuration_save_wallet_record** | [**WTWalletConfigurationSaveWalletRecord**](WTWalletConfigurationSaveWalletRecord.md)|  | 

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

