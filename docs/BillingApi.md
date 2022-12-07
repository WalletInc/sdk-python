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
> bool, date, datetime, dict, float, int, list, str, none_type buy_add_on(product_id)

Fetch add-on products, or 1-time purchase products (non-subscription products)

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)
    product_id = "productID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch add-on products, or 1-time purchase products (non-subscription products)
        api_response = api_instance.buy_add_on(product_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->buy_add_on: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |

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

# **buy_special_offer**
> bool, date, datetime, dict, float, int, list, str, none_type buy_special_offer(product_id)

Buy special offer

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)
    product_id = "productID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Buy special offer
        api_response = api_instance.buy_special_offer(product_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->buy_special_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |

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

# **cancel_plan**
> bool, date, datetime, dict, float, int, list, str, none_type cancel_plan()

Cancel billing plan and revert to default

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Cancel billing plan and revert to default
        api_response = api_instance.cancel_plan()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->cancel_plan: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **change_plan**
> bool, date, datetime, dict, float, int, list, str, none_type change_plan(wt_billing_change_plan)

Change billing plan

### Example


```python
import time
import wallet
from wallet.api import billing_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.wt_billing_change_plan import WTBillingChangePlan
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
    api_instance = billing_api.BillingApi(api_client)
    wt_billing_change_plan = WTBillingChangePlan(
        plan_name="intro_default",
    ) # WTBillingChangePlan | 

    # example passing only required values which don't have defaults set
    try:
        # Change billing plan
        api_response = api_instance.change_plan(wt_billing_change_plan)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->change_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_billing_change_plan** | [**WTBillingChangePlan**](WTBillingChangePlan.md)|  |

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

# **fetch_add_ons**
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_add_ons()

Fetch add-on products, or 1-time purchase products (non-subscription products)

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch add-on products, or 1-time purchase products (non-subscription products)
        api_response = api_instance.fetch_add_ons()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->fetch_add_ons: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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
> InlineResponse200 fetch_industry()

Fetch merchant's industry

### Example


```python
import time
import wallet
from wallet.api import billing_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.inline_response200 import InlineResponse200
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch merchant's industry
        api_response = api_instance.fetch_industry()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->fetch_industry: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

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
> bool, date, datetime, dict, float, int, list, str, none_type fetch_invoices()

Fetch all invoices

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all invoices
        api_response = api_instance.fetch_invoices()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->fetch_invoices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **fetch_special_offers**
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_special_offers()

Fetch special offer products

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch special offer products
        api_response = api_instance.fetch_special_offers()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->fetch_special_offers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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
> bool, date, datetime, dict, float, int, list, str, none_type fetch_subscription()

Fetch subscription

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch subscription
        api_response = api_instance.fetch_subscription()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->fetch_subscription: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **fetch_usage_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} fetch_usage_summary()

Fetch usage summary

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch usage summary
        api_response = api_instance.fetch_usage_summary(start_date_time=start_date_time, end_date_time=end_date_time)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->fetch_usage_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | [optional]
 **end_date_time** | **datetime**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
> bool, date, datetime, dict, float, int, list, str, none_type save_payment_method(wt_billing_save_payment_method)

Save payment method

### Example


```python
import time
import wallet
from wallet.api import billing_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_billing_save_payment_method import WTBillingSavePaymentMethod
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
    api_instance = billing_api.BillingApi(api_client)
    wt_billing_save_payment_method = WTBillingSavePaymentMethod(
        payment_method_id="7y7huhdhhd",
    ) # WTBillingSavePaymentMethod | 

    # example passing only required values which don't have defaults set
    try:
        # Save payment method
        api_response = api_instance.save_payment_method(wt_billing_save_payment_method)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->save_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_billing_save_payment_method** | [**WTBillingSavePaymentMethod**](WTBillingSavePaymentMethod.md)|  |

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

# **upcoming_invoices**
> bool, date, datetime, dict, float, int, list, str, none_type upcoming_invoices()

Fetch upcoming invoices

### Example


```python
import time
import wallet
from wallet.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch upcoming invoices
        api_response = api_instance.upcoming_invoices()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling BillingApi->upcoming_invoices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **verify_payment_method**
> WTBillingVerifyPaymentMethodResponse verify_payment_method()

Verify payment method

### Example


```python
import time
import wallet
from wallet.api import billing_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_billing_verify_payment_method_response import WTBillingVerifyPaymentMethodResponse
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Verify payment method
        api_response = api_instance.verify_payment_method()
        pprint(api_response)
    except wallet.ApiException as e:
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

