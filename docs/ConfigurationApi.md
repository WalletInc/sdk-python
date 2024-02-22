# wallet.ConfigurationApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_public_chat_room**](ConfigurationApi.md#create_public_chat_room) | **POST** /v2/wallet/createPublicChatRoom | 
[**save_merchant_credit_payment_design**](ConfigurationApi.md#save_merchant_credit_payment_design) | **PUT** /v2/wallet/merchantCredit/paymentDesign | Update wallet record
[**save_wallet_record**](ConfigurationApi.md#save_wallet_record) | **PUT** /v2/wallet | Update wallet record


# **create_public_chat_room**
> str create_public_chat_room()



Save wallet record

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
    api_instance = wallet.ConfigurationApi(api_client)

    try:
        api_response = api_instance.create_public_chat_room()
        print("The response of ConfigurationApi->create_public_chat_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_public_chat_room: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

Update wallet record

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
    api_instance = wallet.ConfigurationApi(api_client)
    save_merchant_credit_payment_design_request = wallet.SaveMerchantCreditPaymentDesignRequest() # SaveMerchantCreditPaymentDesignRequest | 

    try:
        # Update wallet record
        api_response = api_instance.save_merchant_credit_payment_design(save_merchant_credit_payment_design_request)
        print("The response of ConfigurationApi->save_merchant_credit_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->save_merchant_credit_payment_design: %s\n" % e)
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
> WalletConfiguration save_wallet_record(wt_wallet_configuration_save_wallet_record)

Update wallet record

### Example


```python
import wallet
from wallet.models.wt_wallet_configuration_save_wallet_record import WTWalletConfigurationSaveWalletRecord
from wallet.models.wallet_configuration import WalletConfiguration
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
    api_instance = wallet.ConfigurationApi(api_client)
    wt_wallet_configuration_save_wallet_record = wallet.WTWalletConfigurationSaveWalletRecord() # WTWalletConfigurationSaveWalletRecord | 

    try:
        # Update wallet record
        api_response = api_instance.save_wallet_record(wt_wallet_configuration_save_wallet_record)
        print("The response of ConfigurationApi->save_wallet_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->save_wallet_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_wallet_configuration_save_wallet_record** | [**WTWalletConfigurationSaveWalletRecord**](WTWalletConfigurationSaveWalletRecord.md)|  | 

### Return type

[**WalletConfiguration**](WalletConfiguration.md)

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

