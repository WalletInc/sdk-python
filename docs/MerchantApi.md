# wallet.MerchantApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_merchant_profile**](MerchantApi.md#archive_merchant_profile) | **DELETE** /v2/merchant/delete | Archive Merchant
[**archive_payment_object_broadcast**](MerchantApi.md#archive_payment_object_broadcast) | **DELETE** /v2/merchant/paymentObjectBroadcast/{broadcastID} | Archive payment object broadcast
[**count_inbound_sms**](MerchantApi.md#count_inbound_sms) | **GET** /v2/merchant/sms/inbound/count/{phoneNumberID} | Count inbound SMSes
[**export_inbound_messages**](MerchantApi.md#export_inbound_messages) | **PUT** /v2/merchant/sms/inbound/export/{phoneNumberID} | Export inbound messages
[**export_outbound_messages**](MerchantApi.md#export_outbound_messages) | **PUT** /v2/merchant/sms/outbound/export/{phoneNumberID} | Export outbound messages
[**fetch_advertisement_credit_broadcasts**](MerchantApi.md#fetch_advertisement_credit_broadcasts) | **GET** /v2/merchant/broadcasts/adCredits/all | Fetch all ad credit broadcasts
[**fetch_custom_roles**](MerchantApi.md#fetch_custom_roles) | **GET** /v2/merchant/roles/custom | Fetch custom roles
[**fetch_dynamic_voucher_broadcasts**](MerchantApi.md#fetch_dynamic_voucher_broadcasts) | **GET** /v2/merchant/broadcasts/dynamicVouchers/all | Fetch all dynamic voucher broadcasts
[**fetch_employees**](MerchantApi.md#fetch_employees) | **GET** /v2/merchant/employees/all | Fetch all employees
[**fetch_help_desk_requests**](MerchantApi.md#fetch_help_desk_requests) | **GET** /v2/merchant/helpDeskRequests/{phoneNumberID} | Fetch help desk requests
[**fetch_imported_list**](MerchantApi.md#fetch_imported_list) | **GET** /v2/merchant/lists/imported/{listID} | Fetch imported list
[**fetch_imported_lists**](MerchantApi.md#fetch_imported_lists) | **GET** /v2/merchant/lists/imported/all | Fetch all imported lists
[**fetch_inbound_sms**](MerchantApi.md#fetch_inbound_sms) | **GET** /v2/merchant/sms/inbound/{phoneNumberID} | Fetch inbound SMSes
[**fetch_inbound_smsby_page**](MerchantApi.md#fetch_inbound_smsby_page) | **GET** /v2/merchant/sms/inbound/page/{phoneNumberID} | Fetch inbound SMSes by page
[**fetch_merchant_outbound_sms**](MerchantApi.md#fetch_merchant_outbound_sms) | **GET** /v2/merchant/sms/outbound/{phoneNumberID} | Fetch outbound SMSes
[**fetch_merchant_phone_numbers**](MerchantApi.md#fetch_merchant_phone_numbers) | **GET** /v2/merchant/phoneNumbers/all | Fetch all phone numbers
[**fetch_opt_in_list**](MerchantApi.md#fetch_opt_in_list) | **GET** /v2/merchant/lists/optIn/{listID} | Fetch opt in list
[**fetch_opt_in_lists**](MerchantApi.md#fetch_opt_in_lists) | **GET** /v2/merchant/lists/optIn/all | Fetch all opt in lists
[**fetch_phone_number**](MerchantApi.md#fetch_phone_number) | **GET** /v2/merchant/phoneNumber/{phoneNumberID} | Fetch phone number
[**fetch_public_employees**](MerchantApi.md#fetch_public_employees) | **GET** /v2/merchant/employees/public | Fetch public representative employees of the merchant
[**fetch_simple_sms_broadcasts**](MerchantApi.md#fetch_simple_sms_broadcasts) | **GET** /v2/merchant/broadcasts/simpleSMS/all | Fetch all simple SMS broadcasts
[**fetch_static_voucher_campaign_broadcasts**](MerchantApi.md#fetch_static_voucher_campaign_broadcasts) | **GET** /v2/merchant/broadcasts/staticVoucherCampaign/all | Fetch all static voucher campaign broadcasts
[**fetch_tcpa_filter**](MerchantApi.md#fetch_tcpa_filter) | **GET** /v2/merchant/tcpa/filter/all | Fetch all TCPA Filters
[**fetch_wallet_configuration**](MerchantApi.md#fetch_wallet_configuration) | **GET** /v2/merchant/wallet/configuration | Fetch wallet configuration
[**update_merchant**](MerchantApi.md#update_merchant) | **PUT** /v2/merchant | Update merchant details
[**update_points_of_contact**](MerchantApi.md#update_points_of_contact) | **PUT** /v2/merchant/pointsOfContact | Update billing contact
[**update_pos_integration**](MerchantApi.md#update_pos_integration) | **PUT** /v2/merchant/pos/integration | Update POS Integration


# **archive_merchant_profile**
> bool, date, datetime, dict, float, int, list, str, none_type archive_merchant_profile()

Archive Merchant

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Archive Merchant
        api_response = api_instance.archive_merchant_profile()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->archive_merchant_profile: %s\n" % e)
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

# **archive_payment_object_broadcast**
> bool, date, datetime, dict, float, int, list, str, none_type archive_payment_object_broadcast(broadcast_id)

Archive payment object broadcast

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)
    broadcast_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive payment object broadcast
        api_response = api_instance.archive_payment_object_broadcast(broadcast_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->archive_payment_object_broadcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

# **count_inbound_sms**
> WTCountResult count_inbound_sms(phone_number_id)

Count inbound SMSes

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    from_phone_number = "fromPhoneNumber_example" # str |  (optional)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count inbound SMSes
        api_response = api_instance.count_inbound_sms(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->count_inbound_sms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count inbound SMSes
        api_response = api_instance.count_inbound_sms(phone_number_id, from_phone_number=from_phone_number, body=body)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->count_inbound_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **from_phone_number** | **str**|  | [optional]
 **body** | **str**|  | [optional]

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **export_inbound_messages**
> str export_inbound_messages(phone_number_id, locale)

Export inbound messages

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 
    locale = "locale_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Export inbound messages
        api_response = api_instance.export_inbound_messages(phone_number_id, locale)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->export_inbound_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |
 **locale** | **str**|  |

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

# **export_outbound_messages**
> str export_outbound_messages(phone_number_id, locale)

Export outbound messages

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 
    locale = "locale_example" # str | 
    payment_object_broadcast_id = NanoID("C") # NanoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export outbound messages
        api_response = api_instance.export_outbound_messages(phone_number_id, locale)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->export_outbound_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export outbound messages
        api_response = api_instance.export_outbound_messages(phone_number_id, locale, payment_object_broadcast_id=payment_object_broadcast_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->export_outbound_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |
 **locale** | **str**|  |
 **payment_object_broadcast_id** | **NanoID**|  | [optional]

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

# **fetch_advertisement_credit_broadcasts**
> [AdvertisementCreditBroadcast] fetch_advertisement_credit_broadcasts()

Fetch all ad credit broadcasts

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.advertisement_credit_broadcast import AdvertisementCreditBroadcast
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all ad credit broadcasts
        api_response = api_instance.fetch_advertisement_credit_broadcasts(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_advertisement_credit_broadcasts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[AdvertisementCreditBroadcast]**](AdvertisementCreditBroadcast.md)

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

# **fetch_custom_roles**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_custom_roles()

Fetch custom roles

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch custom roles
        api_response = api_instance.fetch_custom_roles()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_custom_roles: %s\n" % e)
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

# **fetch_dynamic_voucher_broadcasts**
> [DynamicVoucherBroadcast] fetch_dynamic_voucher_broadcasts()

Fetch all dynamic voucher broadcasts

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.dynamic_voucher_broadcast import DynamicVoucherBroadcast
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all dynamic voucher broadcasts
        api_response = api_instance.fetch_dynamic_voucher_broadcasts(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_dynamic_voucher_broadcasts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[DynamicVoucherBroadcast]**](DynamicVoucherBroadcast.md)

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

# **fetch_employees**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_employees()

Fetch all employees

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all employees
        api_response = api_instance.fetch_employees()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_employees: %s\n" % e)
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

# **fetch_help_desk_requests**
> [HelpDeskRequest] fetch_help_desk_requests(phone_number_id)

Fetch help desk requests

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.help_desk_request import HelpDeskRequest
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
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    is_resolved = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch help desk requests
        api_response = api_instance.fetch_help_desk_requests(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_help_desk_requests: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch help desk requests
        api_response = api_instance.fetch_help_desk_requests(phone_number_id, is_resolved=is_resolved)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_help_desk_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **is_resolved** | **bool**|  | [optional]

### Return type

[**[HelpDeskRequest]**](HelpDeskRequest.md)

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

# **fetch_imported_list**
> ImportedList fetch_imported_list(list_id)

Fetch imported list

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.imported_list import ImportedList
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
    api_instance = merchant_api.MerchantApi(api_client)
    list_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch imported list
        api_response = api_instance.fetch_imported_list(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_imported_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**ImportedList**](ImportedList.md)

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

# **fetch_imported_lists**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_imported_lists()

Fetch all imported lists

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all imported lists
        api_response = api_instance.fetch_imported_lists(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_imported_lists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

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

# **fetch_inbound_sms**
> [InboundSMS] fetch_inbound_sms(phone_number_id)

Fetch inbound SMSes

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.inbound_sms import InboundSMS
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
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    from_phone_number = "fromPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch inbound SMSes
        api_response = api_instance.fetch_inbound_sms(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_inbound_sms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch inbound SMSes
        api_response = api_instance.fetch_inbound_sms(phone_number_id, from_phone_number=from_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_inbound_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **from_phone_number** | **str**|  | [optional]

### Return type

[**[InboundSMS]**](InboundSMS.md)

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

# **fetch_inbound_smsby_page**
> InlineResponse2002 fetch_inbound_smsby_page(phone_number_id)

Fetch inbound SMSes by page

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    from_phone_number = "fromPhoneNumber_example" # str |  (optional)
    page_size = 3.14 # float |  (optional)
    page_num = 3.14 # float |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch inbound SMSes by page
        api_response = api_instance.fetch_inbound_smsby_page(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_inbound_smsby_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch inbound SMSes by page
        api_response = api_instance.fetch_inbound_smsby_page(phone_number_id, from_phone_number=from_phone_number, page_size=page_size, page_num=page_num)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_inbound_smsby_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **from_phone_number** | **str**|  | [optional]
 **page_size** | **float**|  | [optional]
 **page_num** | **float**|  | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **fetch_merchant_outbound_sms**
> [OutboundSMS] fetch_merchant_outbound_sms(phone_number_id, to_phone_number)

Fetch outbound SMSes

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.outbound_sms import OutboundSMS
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    to_phone_number = "toPhoneNumber_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch outbound SMSes
        api_response = api_instance.fetch_merchant_outbound_sms(phone_number_id, to_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_merchant_outbound_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **to_phone_number** | **str**|  |

### Return type

[**[OutboundSMS]**](OutboundSMS.md)

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

# **fetch_merchant_phone_numbers**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_merchant_phone_numbers()

Fetch all phone numbers

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)
    is_approved = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all phone numbers
        api_response = api_instance.fetch_merchant_phone_numbers(is_archive_included=is_archive_included, is_approved=is_approved)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_merchant_phone_numbers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]
 **is_approved** | **bool**|  | [optional]

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

# **fetch_opt_in_list**
> OptInList fetch_opt_in_list(list_id)

Fetch opt in list

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.opt_in_list import OptInList
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
    api_instance = merchant_api.MerchantApi(api_client)
    list_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch opt in list
        api_response = api_instance.fetch_opt_in_list(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_opt_in_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**OptInList**](OptInList.md)

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

# **fetch_opt_in_lists**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_opt_in_lists()

Fetch all opt in lists

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all opt in lists
        api_response = api_instance.fetch_opt_in_lists(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_opt_in_lists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

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

# **fetch_phone_number**
> PhoneNumber fetch_phone_number(phone_number_id)

Fetch phone number

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.phone_number import PhoneNumber
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
    api_instance = merchant_api.MerchantApi(api_client)
    phone_number_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch phone number
        api_response = api_instance.fetch_phone_number(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

# **fetch_public_employees**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_public_employees()

Fetch public representative employees of the merchant

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch public representative employees of the merchant
        api_response = api_instance.fetch_public_employees()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_public_employees: %s\n" % e)
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

# **fetch_simple_sms_broadcasts**
> [SimpleSMSBroadcast] fetch_simple_sms_broadcasts()

Fetch all simple SMS broadcasts

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.simple_sms_broadcast import SimpleSMSBroadcast
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
    api_instance = merchant_api.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all simple SMS broadcasts
        api_response = api_instance.fetch_simple_sms_broadcasts(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_simple_sms_broadcasts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[SimpleSMSBroadcast]**](SimpleSMSBroadcast.md)

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

# **fetch_static_voucher_campaign_broadcasts**
> [StaticVoucherCampaignBroadcast] fetch_static_voucher_campaign_broadcasts()

Fetch all static voucher campaign broadcasts

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher_campaign_broadcast import StaticVoucherCampaignBroadcast
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
    api_instance = merchant_api.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all static voucher campaign broadcasts
        api_response = api_instance.fetch_static_voucher_campaign_broadcasts(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_static_voucher_campaign_broadcasts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[StaticVoucherCampaignBroadcast]**](StaticVoucherCampaignBroadcast.md)

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

# **fetch_tcpa_filter**
> [Tcpa] fetch_tcpa_filter()

Fetch all TCPA Filters

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.tcpa import Tcpa
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all TCPA Filters
        api_response = api_instance.fetch_tcpa_filter()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_tcpa_filter: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Tcpa]**](Tcpa.md)

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

# **fetch_wallet_configuration**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_wallet_configuration()

Fetch wallet configuration

### Example


```python
import time
import wallet
from wallet.api import merchant_api
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
    api_instance = merchant_api.MerchantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch wallet configuration
        api_response = api_instance.fetch_wallet_configuration()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->fetch_wallet_configuration: %s\n" % e)
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

# **update_merchant**
> bool, date, datetime, dict, float, int, list, str, none_type update_merchant(wt_merchant_update)

Update merchant details

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_merchant_update import WTMerchantUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)
    wt_merchant_update = WTMerchantUpdate(
        company_name="Wallet Inc",
        address1="address1_example",
        address2="address2_example",
        city="city_example",
        state="state_example",
        country="country_example",
        phone_number="phone_number_example",
        zip="zip_example",
        currency_abbreviation="currency_abbreviation_example",
    ) # WTMerchantUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update merchant details
        api_response = api_instance.update_merchant(wt_merchant_update)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->update_merchant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update** | [**WTMerchantUpdate**](WTMerchantUpdate.md)|  |

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

# **update_points_of_contact**
> bool, date, datetime, dict, float, int, list, str, none_type update_points_of_contact(wt_merchant_update_points_of_contact)

Update billing contact

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.wt_merchant_update_points_of_contact import WTMerchantUpdatePointsOfContact
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
    api_instance = merchant_api.MerchantApi(api_client)
    wt_merchant_update_points_of_contact = WTMerchantUpdatePointsOfContact(
        billing_employee_id=NanoID("C"),
        marketing_employee_id=NanoID("C"),
        technical_employee_id=NanoID("C"),
        customer_service_employee_id=NanoID("C"),
    ) # WTMerchantUpdatePointsOfContact | 

    # example passing only required values which don't have defaults set
    try:
        # Update billing contact
        api_response = api_instance.update_points_of_contact(wt_merchant_update_points_of_contact)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->update_points_of_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update_points_of_contact** | [**WTMerchantUpdatePointsOfContact**](WTMerchantUpdatePointsOfContact.md)|  |

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

# **update_pos_integration**
> bool, date, datetime, dict, float, int, list, str, none_type update_pos_integration(wt_merchant_update_pos_integration)

Update POS Integration

### Example


```python
import time
import wallet
from wallet.api import merchant_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_merchant_update_pos_integration import WTMerchantUpdatePOSIntegration
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_api.MerchantApi(api_client)
    wt_merchant_update_pos_integration = WTMerchantUpdatePOSIntegration(
        info_genesis_property_id="info_genesis_property_id_example",
    ) # WTMerchantUpdatePOSIntegration | 

    # example passing only required values which don't have defaults set
    try:
        # Update POS Integration
        api_response = api_instance.update_pos_integration(wt_merchant_update_pos_integration)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantApi->update_pos_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update_pos_integration** | [**WTMerchantUpdatePOSIntegration**](WTMerchantUpdatePOSIntegration.md)|  |

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

