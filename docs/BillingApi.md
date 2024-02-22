# wallet.BillingApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_add_on**](BillingApi.md#buy_add_on) | **POST** /v2/billing/products/addOns/{productID} | Fetch add-on products, or 1-time purchase products (non-subscription products)
[**buy_special_offer**](BillingApi.md#buy_special_offer) | **POST** /v2/billing/products/specialOffers/{productID} | Buy special offer
[**cancel_plan**](BillingApi.md#cancel_plan) | **DELETE** /v2/billing/plan | Cancel billing plan and revert to default
[**change_plan**](BillingApi.md#change_plan) | **PUT** /v2/billing/plan | Change billing plan
[**fetch_add_ons**](BillingApi.md#fetch_add_ons) | **GET** /v2/billing/products/addOns | Fetch add-on products, or 1-time purchase products (non-subscription products)
[**fetch_industry**](BillingApi.md#fetch_industry) | **GET** /v2/billing/industry | Fetch merchant&#39;s industry
[**fetch_invoices**](BillingApi.md#fetch_invoices) | **GET** /v2/billing/invoices/all | Fetch all invoices
[**fetch_special_offers**](BillingApi.md#fetch_special_offers) | **GET** /v2/billing/products/specialOffers | Fetch special offer products
[**fetch_subscription**](BillingApi.md#fetch_subscription) | **GET** /v2/billing/subscription | Fetch subscription
[**fetch_usage_summary**](BillingApi.md#fetch_usage_summary) | **GET** /v2/billing/summary | Fetch usage summary
[**save_payment_method**](BillingApi.md#save_payment_method) | **PUT** /v2/billing/paymentMethod | Save payment method
[**upcoming_invoices**](BillingApi.md#upcoming_invoices) | **GET** /v2/billing/invoices/upcoming | Fetch upcoming invoices
[**verify_payment_method**](BillingApi.md#verify_payment_method) | **GET** /v2/billing/paymentMethod | Verify payment method


# **buy_add_on**
> object buy_add_on(product_id)

Fetch add-on products, or 1-time purchase products (non-subscription products)

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
    api_instance = wallet.BillingApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Fetch add-on products, or 1-time purchase products (non-subscription products)
        api_response = api_instance.buy_add_on(product_id)
        print("The response of BillingApi->buy_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->buy_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

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

# **buy_special_offer**
> object buy_special_offer(product_id)

Buy special offer

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
    api_instance = wallet.BillingApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Buy special offer
        api_response = api_instance.buy_special_offer(product_id)
        print("The response of BillingApi->buy_special_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->buy_special_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

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

# **cancel_plan**
> object cancel_plan()

Cancel billing plan and revert to default

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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Cancel billing plan and revert to default
        api_response = api_instance.cancel_plan()
        print("The response of BillingApi->cancel_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->cancel_plan: %s\n" % e)
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

# **change_plan**
> object change_plan(wt_billing_change_plan)

Change billing plan

### Example


```python
import wallet
from wallet.models.wt_billing_change_plan import WTBillingChangePlan
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
    api_instance = wallet.BillingApi(api_client)
    wt_billing_change_plan = wallet.WTBillingChangePlan() # WTBillingChangePlan | 

    try:
        # Change billing plan
        api_response = api_instance.change_plan(wt_billing_change_plan)
        print("The response of BillingApi->change_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->change_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_billing_change_plan** | [**WTBillingChangePlan**](WTBillingChangePlan.md)|  | 

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

# **fetch_add_ons**
> List[object] fetch_add_ons()

Fetch add-on products, or 1-time purchase products (non-subscription products)

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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Fetch add-on products, or 1-time purchase products (non-subscription products)
        api_response = api_instance.fetch_add_ons()
        print("The response of BillingApi->fetch_add_ons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->fetch_add_ons: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

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

# **fetch_industry**
> FetchIndustry200Response fetch_industry()

Fetch merchant's industry

### Example


```python
import wallet
from wallet.models.fetch_industry200_response import FetchIndustry200Response
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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Fetch merchant's industry
        api_response = api_instance.fetch_industry()
        print("The response of BillingApi->fetch_industry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->fetch_industry: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FetchIndustry200Response**](FetchIndustry200Response.md)

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

# **fetch_invoices**
> object fetch_invoices()

Fetch all invoices

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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Fetch all invoices
        api_response = api_instance.fetch_invoices()
        print("The response of BillingApi->fetch_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->fetch_invoices: %s\n" % e)
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

# **fetch_special_offers**
> List[object] fetch_special_offers()

Fetch special offer products

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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Fetch special offer products
        api_response = api_instance.fetch_special_offers()
        print("The response of BillingApi->fetch_special_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->fetch_special_offers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

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

# **fetch_subscription**
> object fetch_subscription()

Fetch subscription

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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Fetch subscription
        api_response = api_instance.fetch_subscription()
        print("The response of BillingApi->fetch_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->fetch_subscription: %s\n" % e)
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

# **fetch_usage_summary**
> object fetch_usage_summary(start_date_time=start_date_time, end_date_time=end_date_time)

Fetch usage summary

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
    api_instance = wallet.BillingApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Fetch usage summary
        api_response = api_instance.fetch_usage_summary(start_date_time=start_date_time, end_date_time=end_date_time)
        print("The response of BillingApi->fetch_usage_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->fetch_usage_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | [optional] 
 **end_date_time** | **datetime**|  | [optional] 

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

# **save_payment_method**
> object save_payment_method(wt_billing_save_payment_method)

Save payment method

### Example


```python
import wallet
from wallet.models.wt_billing_save_payment_method import WTBillingSavePaymentMethod
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
    api_instance = wallet.BillingApi(api_client)
    wt_billing_save_payment_method = wallet.WTBillingSavePaymentMethod() # WTBillingSavePaymentMethod | 

    try:
        # Save payment method
        api_response = api_instance.save_payment_method(wt_billing_save_payment_method)
        print("The response of BillingApi->save_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->save_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_billing_save_payment_method** | [**WTBillingSavePaymentMethod**](WTBillingSavePaymentMethod.md)|  | 

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

# **upcoming_invoices**
> object upcoming_invoices()

Fetch upcoming invoices

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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Fetch upcoming invoices
        api_response = api_instance.upcoming_invoices()
        print("The response of BillingApi->upcoming_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->upcoming_invoices: %s\n" % e)
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

# **verify_payment_method**
> WTBillingVerifyPaymentMethodResponse verify_payment_method()

Verify payment method

### Example


```python
import wallet
from wallet.models.wt_billing_verify_payment_method_response import WTBillingVerifyPaymentMethodResponse
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
    api_instance = wallet.BillingApi(api_client)

    try:
        # Verify payment method
        api_response = api_instance.verify_payment_method()
        print("The response of BillingApi->verify_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->verify_payment_method: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WTBillingVerifyPaymentMethodResponse**](WTBillingVerifyPaymentMethodResponse.md)

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

