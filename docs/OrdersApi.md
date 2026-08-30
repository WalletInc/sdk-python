# wallet.OrdersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_order**](OrdersApi.md#fetch_order) | **GET** /orders/{orderId} | Fetch one of the authenticated merchant&#39;s orders by id Returns the order with its line items. 403-family error if the order belongs to another merchant (ownership is asserted server-side).
[**list_orders**](OrdersApi.md#list_orders) | **GET** /orders | List the authenticated merchant&#39;s orders Newest first, each hydrated with its line items. Read-only receipts/status for Flow B.
[**redact_order_donor_note**](OrdersApi.md#redact_order_donor_note) | **POST** /orders/{orderId}/donor-note/redact | Redact (soft-delete) the donor note on one of the authenticated merchant&#39;s orders KAN-862 takedown path: hides a guest-supplied tip / donation note from every surface. The original text is RETAINED server-side (soft-delete) for a possible exposure / legal review; no \&quot;[redacted]\&quot; placeholder is shown. Idempotent (an order with no note, or an already-redacted note, is a no-op). 403-family error if the order belongs to another merchant (ownership is asserted server-side).


# **fetch_order**
> WTOrder fetch_order(order_id)

Fetch one of the authenticated merchant's orders by id Returns the order with its line items. 403-family error if the order belongs to another merchant (ownership is asserted server-side).

### Example


```python
import wallet
from wallet.models.wt_order import WTOrder
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
    api_instance = wallet.OrdersApi(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # Fetch one of the authenticated merchant's orders by id Returns the order with its line items. 403-family error if the order belongs to another merchant (ownership is asserted server-side).
        api_response = api_instance.fetch_order(order_id)
        print("The response of OrdersApi->fetch_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->fetch_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**WTOrder**](WTOrder.md)

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

# **list_orders**
> List[WTOrder] list_orders()

List the authenticated merchant's orders Newest first, each hydrated with its line items. Read-only receipts/status for Flow B.

### Example


```python
import wallet
from wallet.models.wt_order import WTOrder
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
    api_instance = wallet.OrdersApi(api_client)

    try:
        # List the authenticated merchant's orders Newest first, each hydrated with its line items. Read-only receipts/status for Flow B.
        api_response = api_instance.list_orders()
        print("The response of OrdersApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->list_orders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WTOrder]**](WTOrder.md)

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

# **redact_order_donor_note**
> WTOrder redact_order_donor_note(order_id)

Redact (soft-delete) the donor note on one of the authenticated merchant's orders KAN-862 takedown path: hides a guest-supplied tip / donation note from every surface. The original text is RETAINED server-side (soft-delete) for a possible exposure / legal review; no \"[redacted]\" placeholder is shown. Idempotent (an order with no note, or an already-redacted note, is a no-op). 403-family error if the order belongs to another merchant (ownership is asserted server-side).

### Example


```python
import wallet
from wallet.models.wt_order import WTOrder
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
    api_instance = wallet.OrdersApi(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # Redact (soft-delete) the donor note on one of the authenticated merchant's orders KAN-862 takedown path: hides a guest-supplied tip / donation note from every surface. The original text is RETAINED server-side (soft-delete) for a possible exposure / legal review; no \"[redacted]\" placeholder is shown. Idempotent (an order with no note, or an already-redacted note, is a no-op). 403-family error if the order belongs to another merchant (ownership is asserted server-side).
        api_response = api_instance.redact_order_donor_note(order_id)
        print("The response of OrdersApi->redact_order_donor_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->redact_order_donor_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**WTOrder**](WTOrder.md)

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

