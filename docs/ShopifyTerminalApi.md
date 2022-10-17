# wallet.ShopifyTerminalApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_wallet_item_from_shopify_terminal**](ShopifyTerminalApi.md#fetch_wallet_item_from_shopify_terminal) | **GET** /v2/pos/shopify/item/{itemID} | Fetch item
[**redeem_wallet_item_from_shopify_terminal**](ShopifyTerminalApi.md#redeem_wallet_item_from_shopify_terminal) | **POST** /v2/pos/shopify/item/redeem/{itemID} | Redeem item
[**refund_wallet_item_from_shopify_terminal**](ShopifyTerminalApi.md#refund_wallet_item_from_shopify_terminal) | **POST** /v2/pos/shopify/item/refund/{ledgerEntryID} | Refund transaction


# **fetch_wallet_item_from_shopify_terminal**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_wallet_item_from_shopify_terminal(item_id)

Fetch item

### Example


```python
import time
import wallet
from wallet.api import shopify_terminal_api
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
    api_instance = shopify_terminal_api.ShopifyTerminalApi(api_client)
    item_id = "itemID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch item
        api_response = api_instance.fetch_wallet_item_from_shopify_terminal(item_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ShopifyTerminalApi->fetch_wallet_item_from_shopify_terminal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |

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

# **redeem_wallet_item_from_shopify_terminal**
> bool, date, datetime, dict, float, int, list, str, none_type redeem_wallet_item_from_shopify_terminal(item_id, wt_wallet_item_redemption)

Redeem item

### Example


```python
import time
import wallet
from wallet.api import shopify_terminal_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_wallet_item_redemption import WTWalletItemRedemption
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shopify_terminal_api.ShopifyTerminalApi(api_client)
    item_id = "itemID_example" # str | 
    wt_wallet_item_redemption = WTWalletItemRedemption(
        check_amount=500,
        transaction_number="jdfju8uy832hn4ujbh",
        meta_value="JD-344",
    ) # WTWalletItemRedemption | 

    # example passing only required values which don't have defaults set
    try:
        # Redeem item
        api_response = api_instance.redeem_wallet_item_from_shopify_terminal(item_id, wt_wallet_item_redemption)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ShopifyTerminalApi->redeem_wallet_item_from_shopify_terminal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |
 **wt_wallet_item_redemption** | [**WTWalletItemRedemption**](WTWalletItemRedemption.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **refund_wallet_item_from_shopify_terminal**
> bool, date, datetime, dict, float, int, list, str, none_type refund_wallet_item_from_shopify_terminal(ledger_entry_id)

Refund transaction

### Example


```python
import time
import wallet
from wallet.api import shopify_terminal_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = shopify_terminal_api.ShopifyTerminalApi(api_client)
    ledger_entry_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Refund transaction
        api_response = api_instance.refund_wallet_item_from_shopify_terminal(ledger_entry_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ShopifyTerminalApi->refund_wallet_item_from_shopify_terminal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_entry_id** | **NanoID**|  |

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

