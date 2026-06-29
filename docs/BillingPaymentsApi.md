# wallet.BillingPaymentsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_add_on**](BillingPaymentsApi.md#buy_add_on) | **POST** /v2/billing/products/addOns/{productID} | Buy add-on product
[**buy_special_offer**](BillingPaymentsApi.md#buy_special_offer) | **POST** /v2/billing/products/specialOffers/{productID} | Buy special offer
[**cancel_plan**](BillingPaymentsApi.md#cancel_plan) | **DELETE** /v2/billing/plan | Cancel billing plan
[**change_plan**](BillingPaymentsApi.md#change_plan) | **PUT** /v2/billing/plan | Change billing plan
[**fetch_add_ons**](BillingPaymentsApi.md#fetch_add_ons) | **GET** /v2/billing/products/addOns | Get add-on products
[**fetch_customer_payment_methods**](BillingPaymentsApi.md#fetch_customer_payment_methods) | **GET** /v2/billing/paymentMethods/all | Get payment methods
[**fetch_industry**](BillingPaymentsApi.md#fetch_industry) | **GET** /v2/billing/industry | Get merchant&#39;s industry
[**fetch_invoices**](BillingPaymentsApi.md#fetch_invoices) | **GET** /v2/billing/invoices/all | Get invoices
[**fetch_special_offers**](BillingPaymentsApi.md#fetch_special_offers) | **GET** /v2/billing/products/specialOffers | Get special offers
[**fetch_subscription**](BillingPaymentsApi.md#fetch_subscription) | **GET** /v2/billing/subscription | Get subscription
[**fetch_usage_summary**](BillingPaymentsApi.md#fetch_usage_summary) | **GET** /v2/billing/summary | Get usage summary
[**save_payment_method**](BillingPaymentsApi.md#save_payment_method) | **PUT** /v2/billing/paymentMethod | Save payment method
[**set_default_payment_method**](BillingPaymentsApi.md#set_default_payment_method) | **POST** /v2/billing/paymentMethod/default | Set payment method as default
[**upcoming_invoices**](BillingPaymentsApi.md#upcoming_invoices) | **GET** /v2/billing/invoices/upcoming | Get upcoming invoices
[**verify_payment_method**](BillingPaymentsApi.md#verify_payment_method) | **GET** /v2/billing/paymentMethod | Verify payment method


# **buy_add_on**
> object buy_add_on(product_id)

Buy add-on product

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
    api_instance = wallet.BillingPaymentsApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Buy add-on product
        api_response = api_instance.buy_add_on(product_id)
        print("The response of BillingPaymentsApi->buy_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->buy_add_on: %s\n" % e)
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
    api_instance = wallet.BillingPaymentsApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Buy special offer
        api_response = api_instance.buy_special_offer(product_id)
        print("The response of BillingPaymentsApi->buy_special_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->buy_special_offer: %s\n" % e)
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

Cancel billing plan

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Cancel billing plan
        api_response = api_instance.cancel_plan()
        print("The response of BillingPaymentsApi->cancel_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->cancel_plan: %s\n" % e)
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
    api_instance = wallet.BillingPaymentsApi(api_client)
    wt_billing_change_plan = wallet.WTBillingChangePlan() # WTBillingChangePlan | 

    try:
        # Change billing plan
        api_response = api_instance.change_plan(wt_billing_change_plan)
        print("The response of BillingPaymentsApi->change_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->change_plan: %s\n" % e)
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

Get add-on products

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Get add-on products
        api_response = api_instance.fetch_add_ons()
        print("The response of BillingPaymentsApi->fetch_add_ons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->fetch_add_ons: %s\n" % e)
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

# **fetch_customer_payment_methods**
> object fetch_customer_payment_methods()

Get payment methods

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Get payment methods
        api_response = api_instance.fetch_customer_payment_methods()
        print("The response of BillingPaymentsApi->fetch_customer_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->fetch_customer_payment_methods: %s\n" % e)
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

# **fetch_industry**
> FetchIndustry200Response fetch_industry()

Get merchant's industry

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Get merchant's industry
        api_response = api_instance.fetch_industry()
        print("The response of BillingPaymentsApi->fetch_industry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->fetch_industry: %s\n" % e)
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

Get invoices

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Get invoices
        api_response = api_instance.fetch_invoices()
        print("The response of BillingPaymentsApi->fetch_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->fetch_invoices: %s\n" % e)
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

Get special offers

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Get special offers
        api_response = api_instance.fetch_special_offers()
        print("The response of BillingPaymentsApi->fetch_special_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->fetch_special_offers: %s\n" % e)
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

Get subscription

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Get subscription
        api_response = api_instance.fetch_subscription()
        print("The response of BillingPaymentsApi->fetch_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->fetch_subscription: %s\n" % e)
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

Get usage summary

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
    api_instance = wallet.BillingPaymentsApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get usage summary
        api_response = api_instance.fetch_usage_summary(start_date_time=start_date_time, end_date_time=end_date_time)
        print("The response of BillingPaymentsApi->fetch_usage_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->fetch_usage_summary: %s\n" % e)
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
    api_instance = wallet.BillingPaymentsApi(api_client)
    wt_billing_save_payment_method = wallet.WTBillingSavePaymentMethod() # WTBillingSavePaymentMethod | 

    try:
        # Save payment method
        api_response = api_instance.save_payment_method(wt_billing_save_payment_method)
        print("The response of BillingPaymentsApi->save_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->save_payment_method: %s\n" % e)
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

# **set_default_payment_method**
> Merchant set_default_payment_method(set_default_payment_method_request)

Set payment method as default

### Example


```python
import wallet
from wallet.models.merchant import Merchant
from wallet.models.set_default_payment_method_request import SetDefaultPaymentMethodRequest
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
    api_instance = wallet.BillingPaymentsApi(api_client)
    set_default_payment_method_request = wallet.SetDefaultPaymentMethodRequest() # SetDefaultPaymentMethodRequest | 

    try:
        # Set payment method as default
        api_response = api_instance.set_default_payment_method(set_default_payment_method_request)
        print("The response of BillingPaymentsApi->set_default_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->set_default_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_default_payment_method_request** | [**SetDefaultPaymentMethodRequest**](SetDefaultPaymentMethodRequest.md)|  | 

### Return type

[**Merchant**](Merchant.md)

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

Get upcoming invoices

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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Get upcoming invoices
        api_response = api_instance.upcoming_invoices()
        print("The response of BillingPaymentsApi->upcoming_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->upcoming_invoices: %s\n" % e)
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
    api_instance = wallet.BillingPaymentsApi(api_client)

    try:
        # Verify payment method
        api_response = api_instance.verify_payment_method()
        print("The response of BillingPaymentsApi->verify_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentsApi->verify_payment_method: %s\n" % e)
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

