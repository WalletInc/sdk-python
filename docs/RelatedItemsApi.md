# wallet.RelatedItemsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_related_item_usage**](RelatedItemsApi.md#fetch_related_item_usage) | **GET** /relatedItems/usedBy/{type}/{id} | List where an item is attached
[**fetch_related_items**](RelatedItemsApi.md#fetch_related_items) | **GET** /relatedItems/{type}/{id} | Get an item&#39;s related items
[**save_related_items**](RelatedItemsApi.md#save_related_items) | **PUT** /relatedItems/{type}/{id} | Set an item&#39;s related items
[**search_related_items**](RelatedItemsApi.md#search_related_items) | **GET** /relatedItems/search | Search items to attach


# **fetch_related_item_usage**
> List[WTRelatedItemUsage] fetch_related_item_usage(type, id)

List where an item is attached

### Example


```python
import wallet
from wallet.models.wt_related_item_usage import WTRelatedItemUsage
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
    api_instance = wallet.RelatedItemsApi(api_client)
    type = wallet.WTRelatedItemType() # WTRelatedItemType | 
    id = 'id_example' # str | 

    try:
        # List where an item is attached
        api_response = api_instance.fetch_related_item_usage(type, id)
        print("The response of RelatedItemsApi->fetch_related_item_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelatedItemsApi->fetch_related_item_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**WTRelatedItemType**](.md)|  | 
 **id** | **str**|  | 

### Return type

[**List[WTRelatedItemUsage]**](WTRelatedItemUsage.md)

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

# **fetch_related_items**
> WTRelatedItems fetch_related_items(type, id)

Get an item's related items

### Example


```python
import wallet
from wallet.models.wt_related_items import WTRelatedItems
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
    api_instance = wallet.RelatedItemsApi(api_client)
    type = wallet.WTRelatedItemSourceType() # WTRelatedItemSourceType | 
    id = 'id_example' # str | 

    try:
        # Get an item's related items
        api_response = api_instance.fetch_related_items(type, id)
        print("The response of RelatedItemsApi->fetch_related_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelatedItemsApi->fetch_related_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**WTRelatedItemSourceType**](.md)|  | 
 **id** | **str**|  | 

### Return type

[**WTRelatedItems**](WTRelatedItems.md)

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

# **save_related_items**
> WTRelatedItems save_related_items(type, id, wt_related_items_update)

Set an item's related items

### Example


```python
import wallet
from wallet.models.wt_related_items import WTRelatedItems
from wallet.models.wt_related_items_update import WTRelatedItemsUpdate
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
    api_instance = wallet.RelatedItemsApi(api_client)
    type = wallet.WTRelatedItemSourceType() # WTRelatedItemSourceType | 
    id = 'id_example' # str | 
    wt_related_items_update = wallet.WTRelatedItemsUpdate() # WTRelatedItemsUpdate | 

    try:
        # Set an item's related items
        api_response = api_instance.save_related_items(type, id, wt_related_items_update)
        print("The response of RelatedItemsApi->save_related_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelatedItemsApi->save_related_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**WTRelatedItemSourceType**](.md)|  | 
 **id** | **str**|  | 
 **wt_related_items_update** | [**WTRelatedItemsUpdate**](WTRelatedItemsUpdate.md)|  | 

### Return type

[**WTRelatedItems**](WTRelatedItems.md)

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

# **search_related_items**
> WTRelatedItemSearchResults search_related_items(q=q, type=type, page=page)

Search items to attach

### Example


```python
import wallet
from wallet.models.wt_related_item_search_results import WTRelatedItemSearchResults
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
    api_instance = wallet.RelatedItemsApi(api_client)
    q = 'q_example' # str |  (optional)
    type = wallet.WTRelatedItemType() # WTRelatedItemType |  (optional)
    page = 3.4 # float |  (optional)

    try:
        # Search items to attach
        api_response = api_instance.search_related_items(q=q, type=type, page=page)
        print("The response of RelatedItemsApi->search_related_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelatedItemsApi->search_related_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **type** | [**WTRelatedItemType**](.md)|  | [optional] 
 **page** | **float**|  | [optional] 

### Return type

[**WTRelatedItemSearchResults**](WTRelatedItemSearchResults.md)

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

