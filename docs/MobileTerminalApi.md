# wallet.MobileTerminalApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_wallet_item_from_mobile_terminal**](MobileTerminalApi.md#fetch_wallet_item_from_mobile_terminal) | **GET** /v2/pos/mobile/item/{itemID} | Fetch item
[**find_member_by_id**](MobileTerminalApi.md#find_member_by_id) | **GET** /v2/pos/mobile/member/{memberID} | Find member
[**redeem_wallet_item_from_mobile_terminal**](MobileTerminalApi.md#redeem_wallet_item_from_mobile_terminal) | **POST** /v2/pos/mobile/item/redeem/{itemID} | Redeem item


# **fetch_wallet_item_from_mobile_terminal**
> object fetch_wallet_item_from_mobile_terminal(item_id)

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
    api_instance = wallet.MobileTerminalApi(api_client)
    item_id = 'item_id_example' # str | 

    try:
        # Fetch item
        api_response = api_instance.fetch_wallet_item_from_mobile_terminal(item_id)
        print("The response of MobileTerminalApi->fetch_wallet_item_from_mobile_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileTerminalApi->fetch_wallet_item_from_mobile_terminal: %s\n" % e)
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

# **find_member_by_id**
> Member find_member_by_id(member_id)

Find member

### Example


```python
import wallet
from wallet.models.member import Member
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
    api_instance = wallet.MobileTerminalApi(api_client)
    member_id = 'member_id_example' # str | 

    try:
        # Find member
        api_response = api_instance.find_member_by_id(member_id)
        print("The response of MobileTerminalApi->find_member_by_id:\n")
        pprint(api_response)
    except Exception as e:
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
> object redeem_wallet_item_from_mobile_terminal(item_id, wt_wallet_item_redemption)

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
    api_instance = wallet.MobileTerminalApi(api_client)
    item_id = 'item_id_example' # str | 
    wt_wallet_item_redemption = wallet.WTWalletItemRedemption() # WTWalletItemRedemption | 

    try:
        # Redeem item
        api_response = api_instance.redeem_wallet_item_from_mobile_terminal(item_id, wt_wallet_item_redemption)
        print("The response of MobileTerminalApi->redeem_wallet_item_from_mobile_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileTerminalApi->redeem_wallet_item_from_mobile_terminal: %s\n" % e)
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

