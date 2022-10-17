# wallet.MobileTerminalApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_wallet_item_from_mobile_terminal**](MobileTerminalApi.md#fetch_wallet_item_from_mobile_terminal) | **GET** /v2/pos/mobile/item/{itemID} | Fetch item
[**find_member_by_id**](MobileTerminalApi.md#find_member_by_id) | **GET** /v2/pos/mobile/member/{memberID} | Find member
[**redeem_wallet_item_from_mobile_terminal**](MobileTerminalApi.md#redeem_wallet_item_from_mobile_terminal) | **POST** /v2/pos/mobile/item/redeem/{itemID} | Redeem item


# **fetch_wallet_item_from_mobile_terminal**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_wallet_item_from_mobile_terminal(item_id)

Fetch item

### Example


```python
import time
import wallet
from wallet.api import mobile_terminal_api
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
    api_instance = mobile_terminal_api.MobileTerminalApi(api_client)
    item_id = "itemID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch item
        api_response = api_instance.fetch_wallet_item_from_mobile_terminal(item_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MobileTerminalApi->fetch_wallet_item_from_mobile_terminal: %s\n" % e)
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

# **find_member_by_id**
> Member find_member_by_id(member_id)

Find member

### Example


```python
import time
import wallet
from wallet.api import mobile_terminal_api
from wallet.model.member import Member
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
    api_instance = mobile_terminal_api.MobileTerminalApi(api_client)
    member_id = "memberID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Find member
        api_response = api_instance.find_member_by_id(member_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MobileTerminalApi->find_member_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  |

### Return type

[**Member**](Member.md)

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

# **redeem_wallet_item_from_mobile_terminal**
> bool, date, datetime, dict, float, int, list, str, none_type redeem_wallet_item_from_mobile_terminal(item_id, wt_wallet_item_redemption)

Redeem item

### Example


```python
import time
import wallet
from wallet.api import mobile_terminal_api
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
    api_instance = mobile_terminal_api.MobileTerminalApi(api_client)
    item_id = "itemID_example" # str | 
    wt_wallet_item_redemption = WTWalletItemRedemption(
        check_amount=500,
        transaction_number="jdfju8uy832hn4ujbh",
        meta_value="JD-344",
    ) # WTWalletItemRedemption | 

    # example passing only required values which don't have defaults set
    try:
        # Redeem item
        api_response = api_instance.redeem_wallet_item_from_mobile_terminal(item_id, wt_wallet_item_redemption)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MobileTerminalApi->redeem_wallet_item_from_mobile_terminal: %s\n" % e)
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

