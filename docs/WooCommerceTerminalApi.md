# wallet.WooCommerceTerminalApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_wallet_item_from_woo_commerce_terminal**](WooCommerceTerminalApi.md#fetch_wallet_item_from_woo_commerce_terminal) | **GET** /v2/pos/woocommerce/item/{itemID} | Fetch item
[**redeem_wallet_item_from_woo_commerce_terminal**](WooCommerceTerminalApi.md#redeem_wallet_item_from_woo_commerce_terminal) | **POST** /v2/pos/woocommerce/item/redeem/{itemID} | Redeem item
[**refund_wallet_item_from_woo_commerce_terminal**](WooCommerceTerminalApi.md#refund_wallet_item_from_woo_commerce_terminal) | **POST** /v2/pos/woocommerce/item/refund/{ledgerEntryID} | Refund transaction


# **fetch_wallet_item_from_woo_commerce_terminal**
> object fetch_wallet_item_from_woo_commerce_terminal(item_id)

Fetch item

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
    api_instance = wallet.WooCommerceTerminalApi(api_client)
    item_id = 'item_id_example' # str | 

    try:
        # Fetch item
        api_response = api_instance.fetch_wallet_item_from_woo_commerce_terminal(item_id)
        print("The response of WooCommerceTerminalApi->fetch_wallet_item_from_woo_commerce_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WooCommerceTerminalApi->fetch_wallet_item_from_woo_commerce_terminal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 

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

# **redeem_wallet_item_from_woo_commerce_terminal**
> object redeem_wallet_item_from_woo_commerce_terminal(item_id, wt_wallet_item_redemption)

Redeem item

### Example


```python
import wallet
from wallet.models.wt_wallet_item_redemption import WTWalletItemRedemption
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
    api_instance = wallet.WooCommerceTerminalApi(api_client)
    item_id = 'item_id_example' # str | 
    wt_wallet_item_redemption = wallet.WTWalletItemRedemption() # WTWalletItemRedemption | 

    try:
        # Redeem item
        api_response = api_instance.redeem_wallet_item_from_woo_commerce_terminal(item_id, wt_wallet_item_redemption)
        print("The response of WooCommerceTerminalApi->redeem_wallet_item_from_woo_commerce_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WooCommerceTerminalApi->redeem_wallet_item_from_woo_commerce_terminal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **wt_wallet_item_redemption** | [**WTWalletItemRedemption**](WTWalletItemRedemption.md)|  | 

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

# **refund_wallet_item_from_woo_commerce_terminal**
> object refund_wallet_item_from_woo_commerce_terminal(ledger_entry_id)

Refund transaction

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
    api_instance = wallet.WooCommerceTerminalApi(api_client)
    ledger_entry_id = 'ledger_entry_id_example' # str | 

    try:
        # Refund transaction
        api_response = api_instance.refund_wallet_item_from_woo_commerce_terminal(ledger_entry_id)
        print("The response of WooCommerceTerminalApi->refund_wallet_item_from_woo_commerce_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WooCommerceTerminalApi->refund_wallet_item_from_woo_commerce_terminal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_entry_id** | **str**|  | 

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

