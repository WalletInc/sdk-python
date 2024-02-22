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
> object archive_merchant_profile()

Archive Merchant

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Archive Merchant
        api_response = api_instance.archive_merchant_profile()
        print("The response of MerchantApi->archive_merchant_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->archive_merchant_profile: %s\n" % e)
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

# **archive_payment_object_broadcast**
> object archive_payment_object_broadcast(broadcast_id)

Archive payment object broadcast

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
    api_instance = wallet.MerchantApi(api_client)
    broadcast_id = None # object | 

    try:
        # Archive payment object broadcast
        api_response = api_instance.archive_payment_object_broadcast(broadcast_id)
        print("The response of MerchantApi->archive_payment_object_broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->archive_payment_object_broadcast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_id** | [**object**](.md)|  | 

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

# **count_inbound_sms**
> WTCountResult count_inbound_sms(phone_number_id, from_phone_number=from_phone_number, body=body)

Count inbound SMSes

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = None # object | 
    from_phone_number = 'from_phone_number_example' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Count inbound SMSes
        api_response = api_instance.count_inbound_sms(phone_number_id, from_phone_number=from_phone_number, body=body)
        print("The response of MerchantApi->count_inbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->count_inbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | [**object**](.md)|  | 
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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    locale = 'locale_example' # str | 

    try:
        # Export inbound messages
        api_response = api_instance.export_inbound_messages(phone_number_id, locale)
        print("The response of MerchantApi->export_inbound_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->export_inbound_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
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
> str export_outbound_messages(phone_number_id, locale, payment_object_broadcast_id=payment_object_broadcast_id)

Export outbound messages

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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    locale = 'locale_example' # str | 
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)

    try:
        # Export outbound messages
        api_response = api_instance.export_outbound_messages(phone_number_id, locale, payment_object_broadcast_id=payment_object_broadcast_id)
        print("The response of MerchantApi->export_outbound_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->export_outbound_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **locale** | **str**|  | 
 **payment_object_broadcast_id** | **str**|  | [optional] 

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
> List[AdvertisementCreditBroadcast] fetch_advertisement_credit_broadcasts(is_archive_included=is_archive_included)

Fetch all ad credit broadcasts

### Example


```python
import wallet
from wallet.models.advertisement_credit_broadcast import AdvertisementCreditBroadcast
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
    api_instance = wallet.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all ad credit broadcasts
        api_response = api_instance.fetch_advertisement_credit_broadcasts(is_archive_included=is_archive_included)
        print("The response of MerchantApi->fetch_advertisement_credit_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_advertisement_credit_broadcasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[AdvertisementCreditBroadcast]**](AdvertisementCreditBroadcast.md)

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
> object fetch_custom_roles()

Fetch custom roles

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Fetch custom roles
        api_response = api_instance.fetch_custom_roles()
        print("The response of MerchantApi->fetch_custom_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_custom_roles: %s\n" % e)
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

# **fetch_dynamic_voucher_broadcasts**
> List[DynamicVoucherBroadcast] fetch_dynamic_voucher_broadcasts(is_archive_included=is_archive_included)

Fetch all dynamic voucher broadcasts

### Example


```python
import wallet
from wallet.models.dynamic_voucher_broadcast import DynamicVoucherBroadcast
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
    api_instance = wallet.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all dynamic voucher broadcasts
        api_response = api_instance.fetch_dynamic_voucher_broadcasts(is_archive_included=is_archive_included)
        print("The response of MerchantApi->fetch_dynamic_voucher_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_dynamic_voucher_broadcasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[DynamicVoucherBroadcast]**](DynamicVoucherBroadcast.md)

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
> object fetch_employees()

Fetch all employees

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Fetch all employees
        api_response = api_instance.fetch_employees()
        print("The response of MerchantApi->fetch_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_employees: %s\n" % e)
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

# **fetch_help_desk_requests**
> List[HelpDeskRequest] fetch_help_desk_requests(phone_number_id, is_resolved=is_resolved)

Fetch help desk requests

### Example


```python
import wallet
from wallet.models.help_desk_request import HelpDeskRequest
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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = None # object | 
    is_resolved = True # bool |  (optional)

    try:
        # Fetch help desk requests
        api_response = api_instance.fetch_help_desk_requests(phone_number_id, is_resolved=is_resolved)
        print("The response of MerchantApi->fetch_help_desk_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_help_desk_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | [**object**](.md)|  | 
 **is_resolved** | **bool**|  | [optional] 

### Return type

[**List[HelpDeskRequest]**](HelpDeskRequest.md)

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
import wallet
from wallet.models.imported_list import ImportedList
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
    api_instance = wallet.MerchantApi(api_client)
    list_id = None # object | 

    try:
        # Fetch imported list
        api_response = api_instance.fetch_imported_list(list_id)
        print("The response of MerchantApi->fetch_imported_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_imported_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | [**object**](.md)|  | 

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
> object fetch_imported_lists(is_archive_included=is_archive_included)

Fetch all imported lists

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
    api_instance = wallet.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all imported lists
        api_response = api_instance.fetch_imported_lists(is_archive_included=is_archive_included)
        print("The response of MerchantApi->fetch_imported_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_imported_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

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

# **fetch_inbound_sms**
> List[InboundSMS] fetch_inbound_sms(phone_number_id, from_phone_number=from_phone_number)

Fetch inbound SMSes

### Example


```python
import wallet
from wallet.models.inbound_sms import InboundSMS
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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = None # object | 
    from_phone_number = 'from_phone_number_example' # str |  (optional)

    try:
        # Fetch inbound SMSes
        api_response = api_instance.fetch_inbound_sms(phone_number_id, from_phone_number=from_phone_number)
        print("The response of MerchantApi->fetch_inbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_inbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | [**object**](.md)|  | 
 **from_phone_number** | **str**|  | [optional] 

### Return type

[**List[InboundSMS]**](InboundSMS.md)

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
> FetchInboundSMSByPage200Response fetch_inbound_smsby_page(phone_number_id, from_phone_number=from_phone_number, page_size=page_size, page_num=page_num)

Fetch inbound SMSes by page

### Example


```python
import wallet
from wallet.models.fetch_inbound_smsby_page200_response import FetchInboundSMSByPage200Response
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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = None # object | 
    from_phone_number = 'from_phone_number_example' # str |  (optional)
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)

    try:
        # Fetch inbound SMSes by page
        api_response = api_instance.fetch_inbound_smsby_page(phone_number_id, from_phone_number=from_phone_number, page_size=page_size, page_num=page_num)
        print("The response of MerchantApi->fetch_inbound_smsby_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_inbound_smsby_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | [**object**](.md)|  | 
 **from_phone_number** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **page_num** | **float**|  | [optional] 

### Return type

[**FetchInboundSMSByPage200Response**](FetchInboundSMSByPage200Response.md)

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
> List[OutboundSMS] fetch_merchant_outbound_sms(phone_number_id, to_phone_number)

Fetch outbound SMSes

### Example


```python
import wallet
from wallet.models.outbound_sms import OutboundSMS
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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = None # object | 
    to_phone_number = 'to_phone_number_example' # str | 

    try:
        # Fetch outbound SMSes
        api_response = api_instance.fetch_merchant_outbound_sms(phone_number_id, to_phone_number)
        print("The response of MerchantApi->fetch_merchant_outbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_merchant_outbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | [**object**](.md)|  | 
 **to_phone_number** | **str**|  | 

### Return type

[**List[OutboundSMS]**](OutboundSMS.md)

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
> object fetch_merchant_phone_numbers(is_archive_included=is_archive_included, is_approved=is_approved)

Fetch all phone numbers

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
    api_instance = wallet.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)
    is_approved = True # bool |  (optional)

    try:
        # Fetch all phone numbers
        api_response = api_instance.fetch_merchant_phone_numbers(is_archive_included=is_archive_included, is_approved=is_approved)
        print("The response of MerchantApi->fetch_merchant_phone_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_merchant_phone_numbers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 
 **is_approved** | **bool**|  | [optional] 

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

# **fetch_opt_in_list**
> OptInList fetch_opt_in_list(list_id)

Fetch opt in list

### Example


```python
import wallet
from wallet.models.opt_in_list import OptInList
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
    api_instance = wallet.MerchantApi(api_client)
    list_id = None # object | 

    try:
        # Fetch opt in list
        api_response = api_instance.fetch_opt_in_list(list_id)
        print("The response of MerchantApi->fetch_opt_in_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_opt_in_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | [**object**](.md)|  | 

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
> object fetch_opt_in_lists(is_archive_included=is_archive_included)

Fetch all opt in lists

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
    api_instance = wallet.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all opt in lists
        api_response = api_instance.fetch_opt_in_lists(is_archive_included=is_archive_included)
        print("The response of MerchantApi->fetch_opt_in_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_opt_in_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

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

# **fetch_phone_number**
> PhoneNumber fetch_phone_number(phone_number_id)

Fetch phone number

### Example


```python
import wallet
from wallet.models.phone_number import PhoneNumber
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
    api_instance = wallet.MerchantApi(api_client)
    phone_number_id = None # object | 

    try:
        # Fetch phone number
        api_response = api_instance.fetch_phone_number(phone_number_id)
        print("The response of MerchantApi->fetch_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | [**object**](.md)|  | 

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
> object fetch_public_employees()

Fetch public representative employees of the merchant

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Fetch public representative employees of the merchant
        api_response = api_instance.fetch_public_employees()
        print("The response of MerchantApi->fetch_public_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_public_employees: %s\n" % e)
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

# **fetch_simple_sms_broadcasts**
> List[SimpleSMSBroadcast] fetch_simple_sms_broadcasts(is_archive_included=is_archive_included)

Fetch all simple SMS broadcasts

### Example


```python
import wallet
from wallet.models.simple_sms_broadcast import SimpleSMSBroadcast
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
    api_instance = wallet.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all simple SMS broadcasts
        api_response = api_instance.fetch_simple_sms_broadcasts(is_archive_included=is_archive_included)
        print("The response of MerchantApi->fetch_simple_sms_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_simple_sms_broadcasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[SimpleSMSBroadcast]**](SimpleSMSBroadcast.md)

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
> List[StaticVoucherCampaignBroadcast] fetch_static_voucher_campaign_broadcasts(is_archive_included=is_archive_included)

Fetch all static voucher campaign broadcasts

### Example


```python
import wallet
from wallet.models.static_voucher_campaign_broadcast import StaticVoucherCampaignBroadcast
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
    api_instance = wallet.MerchantApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all static voucher campaign broadcasts
        api_response = api_instance.fetch_static_voucher_campaign_broadcasts(is_archive_included=is_archive_included)
        print("The response of MerchantApi->fetch_static_voucher_campaign_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_static_voucher_campaign_broadcasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[StaticVoucherCampaignBroadcast]**](StaticVoucherCampaignBroadcast.md)

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
> List[Tcpa] fetch_tcpa_filter()

Fetch all TCPA Filters

### Example


```python
import wallet
from wallet.models.tcpa import Tcpa
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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Fetch all TCPA Filters
        api_response = api_instance.fetch_tcpa_filter()
        print("The response of MerchantApi->fetch_tcpa_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_tcpa_filter: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Tcpa]**](Tcpa.md)

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
> object fetch_wallet_configuration()

Fetch wallet configuration

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
    api_instance = wallet.MerchantApi(api_client)

    try:
        # Fetch wallet configuration
        api_response = api_instance.fetch_wallet_configuration()
        print("The response of MerchantApi->fetch_wallet_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->fetch_wallet_configuration: %s\n" % e)
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

# **update_merchant**
> object update_merchant(wt_merchant_update)

Update merchant details

### Example


```python
import wallet
from wallet.models.wt_merchant_update import WTMerchantUpdate
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
    api_instance = wallet.MerchantApi(api_client)
    wt_merchant_update = wallet.WTMerchantUpdate() # WTMerchantUpdate | 

    try:
        # Update merchant details
        api_response = api_instance.update_merchant(wt_merchant_update)
        print("The response of MerchantApi->update_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->update_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update** | [**WTMerchantUpdate**](WTMerchantUpdate.md)|  | 

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

# **update_points_of_contact**
> object update_points_of_contact(wt_merchant_update_points_of_contact)

Update billing contact

### Example


```python
import wallet
from wallet.models.wt_merchant_update_points_of_contact import WTMerchantUpdatePointsOfContact
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
    api_instance = wallet.MerchantApi(api_client)
    wt_merchant_update_points_of_contact = wallet.WTMerchantUpdatePointsOfContact() # WTMerchantUpdatePointsOfContact | 

    try:
        # Update billing contact
        api_response = api_instance.update_points_of_contact(wt_merchant_update_points_of_contact)
        print("The response of MerchantApi->update_points_of_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->update_points_of_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update_points_of_contact** | [**WTMerchantUpdatePointsOfContact**](WTMerchantUpdatePointsOfContact.md)|  | 

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

# **update_pos_integration**
> object update_pos_integration(wt_merchant_update_pos_integration)

Update POS Integration

### Example


```python
import wallet
from wallet.models.wt_merchant_update_pos_integration import WTMerchantUpdatePOSIntegration
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
    api_instance = wallet.MerchantApi(api_client)
    wt_merchant_update_pos_integration = wallet.WTMerchantUpdatePOSIntegration() # WTMerchantUpdatePOSIntegration | 

    try:
        # Update POS Integration
        api_response = api_instance.update_pos_integration(wt_merchant_update_pos_integration)
        print("The response of MerchantApi->update_pos_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApi->update_pos_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_update_pos_integration** | [**WTMerchantUpdatePOSIntegration**](WTMerchantUpdatePOSIntegration.md)|  | 

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

