# wallet.SMSApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquire_phone_number**](SMSApi.md#acquire_phone_number) | **POST** /v2/sms/phoneNumber/acquire | Acquire phone number
[**archive_phone_number**](SMSApi.md#archive_phone_number) | **DELETE** /v2/sms/phoneNumber/{phoneNumberID} | Archive phone number
[**archive_recipient**](SMSApi.md#archive_recipient) | **DELETE** /v2/sms/importedList/recipients/{id} | Archive recipient
[**count_imported_list_recipients**](SMSApi.md#count_imported_list_recipients) | **GET** /v2/sms/importedList/recipients/count/{listID} | Count imported list recipients
[**count_opt_in_list_subscribers**](SMSApi.md#count_opt_in_list_subscribers) | **GET** /v2/sms/optInList/subscribers/count/{listID} | Count opt in list subscribers
[**count_opt_in_source_subscribers**](SMSApi.md#count_opt_in_source_subscribers) | **GET** /v2/sms/optInSource/subscribers/count/{sourceID} | Count opt in source subscribers
[**count_outbound_sms**](SMSApi.md#count_outbound_sms) | **GET** /v2/sms/outbound/count/{phoneNumberID} | Count outbound SMS
[**create_imported_list**](SMSApi.md#create_imported_list) | **POST** /v2/sms/importedList | Create imported list
[**create_opt_in_list**](SMSApi.md#create_opt_in_list) | **POST** /v2/sms/optInList | Create opt in list
[**create_opt_in_list_source**](SMSApi.md#create_opt_in_list_source) | **POST** /v2/sms/optInListSource | Send SMS to opt in list
[**create_recipient_in_imported_list**](SMSApi.md#create_recipient_in_imported_list) | **POST** /v2/sms/importedList/recipients/create | Add new recipient in an imported list
[**create_sms_agreement**](SMSApi.md#create_sms_agreement) | **POST** /v2/sms/agreement/create | Accept SMS agreement
[**export_imported_list_recipients**](SMSApi.md#export_imported_list_recipients) | **POST** /v2/sms/importedList/recipients/export/{importedListID} | Export imported list recipients
[**export_opt_in_list_subscribers**](SMSApi.md#export_opt_in_list_subscribers) | **POST** /v2/sms/optInList/subscribers/export/{listID} | Export opt in list subscribers
[**fetch_blocked_tcpa_entries**](SMSApi.md#fetch_blocked_tcpa_entries) | **GET** /v2/sms/phoneNumber/blocked/{phoneNumberID} | Fetch blocked TCPA entries
[**fetch_imported_list_recipients**](SMSApi.md#fetch_imported_list_recipients) | **GET** /v2/sms/importedList/recipients/{listID} | Fetch imported list recipients
[**fetch_imported_list_recipients_by_page**](SMSApi.md#fetch_imported_list_recipients_by_page) | **GET** /v2/sms/importedList/recipients/page/{listID} | Fetch imported list recipients by page
[**fetch_opt_in_list_sources**](SMSApi.md#fetch_opt_in_list_sources) | **GET** /v2/sms/optInListSources/all | Fetch all opt in list sources
[**fetch_opt_in_list_subscribers**](SMSApi.md#fetch_opt_in_list_subscribers) | **GET** /v2/sms/optInList/subscribers/{listID} | Fetch opt in list subscribers
[**fetch_opt_in_list_subscribers_by_page**](SMSApi.md#fetch_opt_in_list_subscribers_by_page) | **GET** /v2/sms/optInList/subscribers/page/{listID} | Fetch opt in list subscribers by page
[**fetch_opt_in_lists_associated_with_phone_number**](SMSApi.md#fetch_opt_in_lists_associated_with_phone_number) | **GET** /v2/sms/phoneNumber/lists/{phoneNumberID} | Fetch opt in lists
[**fetch_opt_in_source_subscribers**](SMSApi.md#fetch_opt_in_source_subscribers) | **GET** /v2/sms/optInSource/subscribers/{sourceID} | Fetch opt in source subscribers
[**fetch_opt_in_sources_associated_with_phone_number**](SMSApi.md#fetch_opt_in_sources_associated_with_phone_number) | **GET** /v2/sms/phoneNumber/sources/{phoneNumberID} | Fetch opt in sources
[**fetch_outbound_sms**](SMSApi.md#fetch_outbound_sms) | **GET** /v2/sms/outbound/{phoneNumberID} | Fetch outbound SMS
[**fetch_outbound_smsby_page**](SMSApi.md#fetch_outbound_smsby_page) | **GET** /v2/sms/outbound/page/{phoneNumberID} | Fetch outbound SMSes by page
[**fetch_payment_object_broadcasts**](SMSApi.md#fetch_payment_object_broadcasts) | **GET** /v2/sms/paymentObjectBroadcasts/{phoneNumberID} | Fetch payment object broadcasts
[**fetch_sms_agreement**](SMSApi.md#fetch_sms_agreement) | **GET** /v2/sms/agreement | Fetch SMS agreement
[**import_imported_list_recipients**](SMSApi.md#import_imported_list_recipients) | **POST** /v2/sms/importedList/recipients/import/{importedListID} | Import imported list recipients
[**import_imported_list_recipients_from_membership_tier**](SMSApi.md#import_imported_list_recipients_from_membership_tier) | **POST** /v2/sms/importedList/recipients/import-from-tier | Import imported list recipients from a given membership tier
[**import_opt_in_list_subscribers**](SMSApi.md#import_opt_in_list_subscribers) | **POST** /v2/sms/optInList/subscribers/import/{listID} | Import opt in list subscribers
[**restore_phone_number**](SMSApi.md#restore_phone_number) | **PATCH** /v2/sms/phoneNumber/{phoneNumberID} | Restore phone number
[**restore_recipient**](SMSApi.md#restore_recipient) | **PATCH** /v2/sms/importedList/recipients/{id} | Restore recipient
[**retrieve_sent_and_max_count_of_messages**](SMSApi.md#retrieve_sent_and_max_count_of_messages) | **GET** /v2/sms/sent | Retrieve the number of messages sent by the merchant within the current billing cycle
[**save_imported_list**](SMSApi.md#save_imported_list) | **PUT** /v2/sms/importedList/{listID} | Save imported list
[**save_opt_in_list**](SMSApi.md#save_opt_in_list) | **PUT** /v2/sms/optInList/{listID} | Save opt in list
[**save_opt_in_list_source**](SMSApi.md#save_opt_in_list_source) | **PUT** /v2/sms/optInListSource/{sourceID} | Save opt in list source
[**send_phone_number_for_verification**](SMSApi.md#send_phone_number_for_verification) | **PUT** /v2/sms/phoneNumber/verification/{phoneNumberID} | Request phone number verification
[**update_phone_number**](SMSApi.md#update_phone_number) | **PUT** /v2/sms/phoneNumber/{phoneNumberID} | Update phone number


# **acquire_phone_number**
> PhoneNumber acquire_phone_number(wtsms_acquire_phone_number)

Acquire phone number

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wtsms_acquire_phone_number import WTSMSAcquirePhoneNumber
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
    api_instance = sms_api.SMSApi(api_client)
    wtsms_acquire_phone_number = WTSMSAcquirePhoneNumber(
        phone_number="+1808987878",
    ) # WTSMSAcquirePhoneNumber | 

    # example passing only required values which don't have defaults set
    try:
        # Acquire phone number
        api_response = api_instance.acquire_phone_number(wtsms_acquire_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->acquire_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wtsms_acquire_phone_number** | [**WTSMSAcquirePhoneNumber**](WTSMSAcquirePhoneNumber.md)|  |

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

# **archive_phone_number**
> PhoneNumber archive_phone_number(phone_number_id)

Archive phone number

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Archive phone number
        api_response = api_instance.archive_phone_number(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->archive_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |

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

# **archive_recipient**
> ImportedListRecipient archive_recipient(id)

Archive recipient

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.imported_list_recipient import ImportedListRecipient
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
    api_instance = sms_api.SMSApi(api_client)
    id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Archive recipient
        api_response = api_instance.archive_recipient(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->archive_recipient: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **NanoID**|  |

### Return type

[**ImportedListRecipient**](ImportedListRecipient.md)

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

# **count_imported_list_recipients**
> WTCountResult count_imported_list_recipients(list_id)

Count imported list recipients

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    is_archive_included = True # bool |  (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count imported list recipients
        api_response = api_instance.count_imported_list_recipients(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_imported_list_recipients: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count imported list recipients
        api_response = api_instance.count_imported_list_recipients(list_id, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_imported_list_recipients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **is_archive_included** | **bool**|  | [optional]
 **start_date** | **datetime**|  | [optional]
 **end_date** | **datetime**|  | [optional]

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

# **count_opt_in_list_subscribers**
> WTCountResult count_opt_in_list_subscribers(list_id)

Count opt in list subscribers

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count opt in list subscribers
        api_response = api_instance.count_opt_in_list_subscribers(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_opt_in_list_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count opt in list subscribers
        api_response = api_instance.count_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_opt_in_list_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **is_subscribed** | **bool**|  | [optional]
 **is_pending_age21_verification** | **bool**|  | [optional]
 **is_archive_included** | **bool**|  | [optional]
 **start_date** | **datetime**|  | [optional]
 **end_date** | **datetime**|  | [optional]

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

# **count_opt_in_source_subscribers**
> WTCountResult count_opt_in_source_subscribers(source_id)

Count opt in source subscribers

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    source_id = NanoID("C") # NanoID | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count opt in source subscribers
        api_response = api_instance.count_opt_in_source_subscribers(source_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_opt_in_source_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count opt in source subscribers
        api_response = api_instance.count_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_opt_in_source_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **NanoID**|  |
 **is_subscribed** | **bool**|  | [optional]
 **is_pending_age21_verification** | **bool**|  | [optional]
 **is_archive_included** | **bool**|  | [optional]
 **start_date** | **datetime**|  | [optional]
 **end_date** | **datetime**|  | [optional]

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

# **count_outbound_sms**
> WTCountResult count_outbound_sms(phone_number_id)

Count outbound SMS

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 
    to_phone_number = "toPhoneNumber_example" # str |  (optional)
    status = "status_example" # str |  (optional)
    payment_object_broadcast_id = NanoID("C") # NanoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count outbound SMS
        api_response = api_instance.count_outbound_sms(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_outbound_sms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count outbound SMS
        api_response = api_instance.count_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->count_outbound_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |
 **to_phone_number** | **str**|  | [optional]
 **status** | **str**|  | [optional]
 **payment_object_broadcast_id** | **NanoID**|  | [optional]

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

# **create_imported_list**
> ImportedList create_imported_list(wtsms_imported_list_create)

Create imported list

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wtsms_imported_list_create import WTSMSImportedListCreate
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
    api_instance = sms_api.SMSApi(api_client)
    wtsms_imported_list_create = WTSMSImportedListCreate(
        phone_number_id=NanoID("C"),
        is_active=True,
        list_name="Import on 19 Dec, 2021",
    ) # WTSMSImportedListCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create imported list
        api_response = api_instance.create_imported_list(wtsms_imported_list_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->create_imported_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wtsms_imported_list_create** | [**WTSMSImportedListCreate**](WTSMSImportedListCreate.md)|  |

### Return type

[**ImportedList**](ImportedList.md)

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

# **create_opt_in_list**
> OptInList create_opt_in_list(wt_opt_in_list_creation_params)

Create opt in list

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_opt_in_list_creation_params import WTOptInListCreationParams
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
    api_instance = sms_api.SMSApi(api_client)
    wt_opt_in_list_creation_params = WTOptInListCreationParams(
        is_active=True,
        list_name="Christmas Offers",
        phone_number_id=SSNanoID("C"),
        estimated_messages_per_month=2500,
        opt_in_keyword="SUBS",
        opt_out_keyword="UNSUB",
        opt_in_confirmed_response="Welcome to the list",
        opt_out_confirmed_response="Sorry to see you go",
        opt_in_confirmed_customer_receives="Welcome to the list",
        opt_out_confirmed_customer_receives="Sorry to see you go",
        is_over21_required=True,
        opt_in_confirmed_media_urls=[
            "opt_in_confirmed_media_urls_example",
        ],
        opt_out_confirmed_media_urls=[
            "opt_out_confirmed_media_urls_example",
        ],
    ) # WTOptInListCreationParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create opt in list
        api_response = api_instance.create_opt_in_list(wt_opt_in_list_creation_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->create_opt_in_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_opt_in_list_creation_params** | [**WTOptInListCreationParams**](WTOptInListCreationParams.md)|  |

### Return type

[**OptInList**](OptInList.md)

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

# **create_opt_in_list_source**
> OptInListSource create_opt_in_list_source(wtsms_opt_in_list_source_create)

Send SMS to opt in list

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.opt_in_list_source import OptInListSource
from wallet.model.wtsms_opt_in_list_source_create import WTSMSOptInListSourceCreate
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
    api_instance = sms_api.SMSApi(api_client)
    wtsms_opt_in_list_source_create = WTSMSOptInListSourceCreate(
        list_id=NanoID("C"),
        source_name="Social Media",
    ) # WTSMSOptInListSourceCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Send SMS to opt in list
        api_response = api_instance.create_opt_in_list_source(wtsms_opt_in_list_source_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->create_opt_in_list_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wtsms_opt_in_list_source_create** | [**WTSMSOptInListSourceCreate**](WTSMSOptInListSourceCreate.md)|  |

### Return type

[**OptInListSource**](OptInListSource.md)

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

# **create_recipient_in_imported_list**
> ImportedListRecipient create_recipient_in_imported_list(ss_imported_list_recipient_create_params)

Add new recipient in an imported list

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.ss_imported_list_recipient_create_params import SSImportedListRecipientCreateParams
from wallet.model.imported_list_recipient import ImportedListRecipient
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
    api_instance = sms_api.SMSApi(api_client)
    ss_imported_list_recipient_create_params = SSImportedListRecipientCreateParams(
        imported_list_id=SSNanoID("C"),
        mobile_phone_number="+18047552674",
    ) # SSImportedListRecipientCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Add new recipient in an imported list
        api_response = api_instance.create_recipient_in_imported_list(ss_imported_list_recipient_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->create_recipient_in_imported_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ss_imported_list_recipient_create_params** | [**SSImportedListRecipientCreateParams**](SSImportedListRecipientCreateParams.md)|  |

### Return type

[**ImportedListRecipient**](ImportedListRecipient.md)

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

# **create_sms_agreement**
> Agreement create_sms_agreement(wtsms_create_agreement)

Accept SMS agreement

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.agreement import Agreement
from wallet.model.wtsms_create_agreement import WTSMSCreateAgreement
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
    api_instance = sms_api.SMSApi(api_client)
    wtsms_create_agreement = WTSMSCreateAgreement(
        is_twilio_terms_read=True,
        is_privacy_policy_on_website=True,
        is_tos_on_website=True,
        is_stop_understood=True,
        is_manual_read=True,
        is_ctia_short_code_read=True,
        is_standards_understood=True,
        is_short_code_understood=True,
        is_opt_in_out_understood=True,
        is_short_code_transfer_understood=True,
        is_pricing_understood=True,
        is_short_code_timeline_understood=True,
    ) # WTSMSCreateAgreement | 

    # example passing only required values which don't have defaults set
    try:
        # Accept SMS agreement
        api_response = api_instance.create_sms_agreement(wtsms_create_agreement)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->create_sms_agreement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wtsms_create_agreement** | [**WTSMSCreateAgreement**](WTSMSCreateAgreement.md)|  |

### Return type

[**Agreement**](Agreement.md)

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

# **export_imported_list_recipients**
> str export_imported_list_recipients(imported_list_id)

Export imported list recipients

### Example


```python
import time
import wallet
from wallet.api import sms_api
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
    api_instance = sms_api.SMSApi(api_client)
    imported_list_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Export imported list recipients
        api_response = api_instance.export_imported_list_recipients(imported_list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->export_imported_list_recipients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_list_id** | **NanoID**|  |

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

# **export_opt_in_list_subscribers**
> str export_opt_in_list_subscribers(list_id)

Export opt in list subscribers

### Example


```python
import time
import wallet
from wallet.api import sms_api
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Export opt in list subscribers
        api_response = api_instance.export_opt_in_list_subscribers(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->export_opt_in_list_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |

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

# **fetch_blocked_tcpa_entries**
> [Tcpa] fetch_blocked_tcpa_entries(phone_number_id)

Fetch blocked TCPA entries

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch blocked TCPA entries
        api_response = api_instance.fetch_blocked_tcpa_entries(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_blocked_tcpa_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |

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

# **fetch_imported_list_recipients**
> [ImportedListRecipient] fetch_imported_list_recipients(list_id)

Fetch imported list recipients

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.imported_list_recipient import ImportedListRecipient
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch imported list recipients
        api_response = api_instance.fetch_imported_list_recipients(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_imported_list_recipients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |

### Return type

[**[ImportedListRecipient]**](ImportedListRecipient.md)

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

# **fetch_imported_list_recipients_by_page**
> InlineResponse2008 fetch_imported_list_recipients_by_page(list_id)

Fetch imported list recipients by page

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2008 import InlineResponse2008
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    page_size = 3.14 # float |  (optional)
    page_num = 3.14 # float |  (optional)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch imported list recipients by page
        api_response = api_instance.fetch_imported_list_recipients_by_page(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_imported_list_recipients_by_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch imported list recipients by page
        api_response = api_instance.fetch_imported_list_recipients_by_page(list_id, page_size=page_size, page_num=page_num, is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_imported_list_recipients_by_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **page_size** | **float**|  | [optional]
 **page_num** | **float**|  | [optional]
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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

# **fetch_opt_in_list_sources**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_opt_in_list_sources()

Fetch all opt in list sources

### Example


```python
import time
import wallet
from wallet.api import sms_api
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
    api_instance = sms_api.SMSApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all opt in list sources
        api_response = api_instance.fetch_opt_in_list_sources(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_sources: %s\n" % e)
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

# **fetch_opt_in_list_subscribers**
> [OptInListSubscriber] fetch_opt_in_list_subscribers(list_id)

Fetch opt in list subscribers

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.auth_error import AuthError
from wallet.model.opt_in_list_subscriber import OptInListSubscriber
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch opt in list subscribers
        api_response = api_instance.fetch_opt_in_list_subscribers(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch opt in list subscribers
        api_response = api_instance.fetch_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **is_subscribed** | **bool**|  | [optional]
 **is_pending_age21_verification** | **bool**|  | [optional]
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[OptInListSubscriber]**](OptInListSubscriber.md)

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

# **fetch_opt_in_list_subscribers_by_page**
> InlineResponse2007 fetch_opt_in_list_subscribers_by_page(list_id)

Fetch opt in list subscribers by page

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.inline_response2007 import InlineResponse2007
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    page_size = 3.14 # float |  (optional)
    page_num = 3.14 # float |  (optional)
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch opt in list subscribers by page
        api_response = api_instance.fetch_opt_in_list_subscribers_by_page(list_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_subscribers_by_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch opt in list subscribers by page
        api_response = api_instance.fetch_opt_in_list_subscribers_by_page(list_id, page_size=page_size, page_num=page_num, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_subscribers_by_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **page_size** | **float**|  | [optional]
 **page_num** | **float**|  | [optional]
 **is_subscribed** | **bool**|  | [optional]
 **is_pending_age21_verification** | **bool**|  | [optional]
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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

# **fetch_opt_in_lists_associated_with_phone_number**
> [OptInList] fetch_opt_in_lists_associated_with_phone_number(phone_number_id)

Fetch opt in lists

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.opt_in_list import OptInList
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch opt in lists
        api_response = api_instance.fetch_opt_in_lists_associated_with_phone_number(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_lists_associated_with_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |

### Return type

[**[OptInList]**](OptInList.md)

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

# **fetch_opt_in_source_subscribers**
> [OptInListSubscriber] fetch_opt_in_source_subscribers(source_id)

Fetch opt in source subscribers

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.auth_error import AuthError
from wallet.model.opt_in_list_subscriber import OptInListSubscriber
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sms_api.SMSApi(api_client)
    source_id = NanoID("C") # NanoID | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch opt in source subscribers
        api_response = api_instance.fetch_opt_in_source_subscribers(source_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_source_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch opt in source subscribers
        api_response = api_instance.fetch_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_source_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **NanoID**|  |
 **is_subscribed** | **bool**|  | [optional]
 **is_pending_age21_verification** | **bool**|  | [optional]
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[OptInListSubscriber]**](OptInListSubscriber.md)

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

# **fetch_opt_in_sources_associated_with_phone_number**
> [OptInListSource] fetch_opt_in_sources_associated_with_phone_number(phone_number_id)

Fetch opt in sources

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.opt_in_list_source import OptInListSource
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch opt in sources
        api_response = api_instance.fetch_opt_in_sources_associated_with_phone_number(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_opt_in_sources_associated_with_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |

### Return type

[**[OptInListSource]**](OptInListSource.md)

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

# **fetch_outbound_sms**
> [OutboundSMS] fetch_outbound_sms(phone_number_id)

Fetch outbound SMS

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 
    to_phone_number = "toPhoneNumber_example" # str |  (optional)
    status = "status_example" # str |  (optional)
    payment_object_broadcast_id = NanoID("C") # NanoID |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch outbound SMS
        api_response = api_instance.fetch_outbound_sms(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_outbound_sms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch outbound SMS
        api_response = api_instance.fetch_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_outbound_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |
 **to_phone_number** | **str**|  | [optional]
 **status** | **str**|  | [optional]
 **payment_object_broadcast_id** | **NanoID**|  | [optional]

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

# **fetch_outbound_smsby_page**
> InlineResponse2006 fetch_outbound_smsby_page(phone_number_id)

Fetch outbound SMSes by page

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.inline_response2006 import InlineResponse2006
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 
    to_phone_number = "toPhoneNumber_example" # str |  (optional)
    payment_object_broadcast_id = NanoID("C") # NanoID |  (optional)
    page_size = 3.14 # float |  (optional)
    page_num = 3.14 # float |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch outbound SMSes by page
        api_response = api_instance.fetch_outbound_smsby_page(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_outbound_smsby_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch outbound SMSes by page
        api_response = api_instance.fetch_outbound_smsby_page(phone_number_id, to_phone_number=to_phone_number, payment_object_broadcast_id=payment_object_broadcast_id, page_size=page_size, page_num=page_num)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_outbound_smsby_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |
 **to_phone_number** | **str**|  | [optional]
 **payment_object_broadcast_id** | **NanoID**|  | [optional]
 **page_size** | **float**|  | [optional]
 **page_num** | **float**|  | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

# **fetch_payment_object_broadcasts**
> [StaticVoucherCampaignBroadcast] fetch_payment_object_broadcasts(phone_number_id)

Fetch payment object broadcasts

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch payment object broadcasts
        api_response = api_instance.fetch_payment_object_broadcasts(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_payment_object_broadcasts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |

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

# **fetch_sms_agreement**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_sms_agreement()

Fetch SMS agreement

### Example


```python
import time
import wallet
from wallet.api import sms_api
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
    api_instance = sms_api.SMSApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch SMS agreement
        api_response = api_instance.fetch_sms_agreement()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->fetch_sms_agreement: %s\n" % e)
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

# **import_imported_list_recipients**
> str import_imported_list_recipients(imported_list_id, wt_employee_import_records)

Import imported list recipients

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.wt_employee_import_records import WTEmployeeImportRecords
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
    api_instance = sms_api.SMSApi(api_client)
    imported_list_id = NanoID("C") # NanoID | 
    wt_employee_import_records = WTEmployeeImportRecords(
        file_name="club-members-upload.csv",
        bucket="members",
    ) # WTEmployeeImportRecords | 

    # example passing only required values which don't have defaults set
    try:
        # Import imported list recipients
        api_response = api_instance.import_imported_list_recipients(imported_list_id, wt_employee_import_records)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->import_imported_list_recipients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_list_id** | **NanoID**|  |
 **wt_employee_import_records** | [**WTEmployeeImportRecords**](WTEmployeeImportRecords.md)|  |

### Return type

**str**

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

# **import_imported_list_recipients_from_membership_tier**
> str import_imported_list_recipients_from_membership_tier(wt_imported_list_recipient_from_membership_tier_import)

Import imported list recipients from a given membership tier

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_imported_list_recipient_from_membership_tier_import import WTImportedListRecipientFromMembershipTierImport
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sms_api.SMSApi(api_client)
    wt_imported_list_recipient_from_membership_tier_import = WTImportedListRecipientFromMembershipTierImport(
        list_name="Platinum Members List",
        phone_number_id=SSNanoID("C"),
        tier_id=None,
    ) # WTImportedListRecipientFromMembershipTierImport | 

    # example passing only required values which don't have defaults set
    try:
        # Import imported list recipients from a given membership tier
        api_response = api_instance.import_imported_list_recipients_from_membership_tier(wt_imported_list_recipient_from_membership_tier_import)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->import_imported_list_recipients_from_membership_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_imported_list_recipient_from_membership_tier_import** | [**WTImportedListRecipientFromMembershipTierImport**](WTImportedListRecipientFromMembershipTierImport.md)|  |

### Return type

**str**

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

# **import_opt_in_list_subscribers**
> str import_opt_in_list_subscribers(list_id, wtsms_import_opt_in_list_subscribers)

Import opt in list subscribers

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.wtsms_import_opt_in_list_subscribers import WTSMSImportOptInListSubscribers
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    wtsms_import_opt_in_list_subscribers = WTSMSImportOptInListSubscribers(
        file_name="club-members-upload.csv",
        bucket="members",
        opt_in_source_id=NanoID("C"),
    ) # WTSMSImportOptInListSubscribers | 

    # example passing only required values which don't have defaults set
    try:
        # Import opt in list subscribers
        api_response = api_instance.import_opt_in_list_subscribers(list_id, wtsms_import_opt_in_list_subscribers)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->import_opt_in_list_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **wtsms_import_opt_in_list_subscribers** | [**WTSMSImportOptInListSubscribers**](WTSMSImportOptInListSubscribers.md)|  |

### Return type

**str**

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

# **restore_phone_number**
> PhoneNumber restore_phone_number(phone_number_id)

Restore phone number

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Restore phone number
        api_response = api_instance.restore_phone_number(phone_number_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->restore_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |

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

# **restore_recipient**
> ImportedListRecipient restore_recipient(id)

Restore recipient

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.imported_list_recipient import ImportedListRecipient
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
    api_instance = sms_api.SMSApi(api_client)
    id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Restore recipient
        api_response = api_instance.restore_recipient(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->restore_recipient: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **NanoID**|  |

### Return type

[**ImportedListRecipient**](ImportedListRecipient.md)

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

# **retrieve_sent_and_max_count_of_messages**
> WTSMSLimits retrieve_sent_and_max_count_of_messages()

Retrieve the number of messages sent by the merchant within the current billing cycle

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wtsms_limits import WTSMSLimits
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sms_api.SMSApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the number of messages sent by the merchant within the current billing cycle
        api_response = api_instance.retrieve_sent_and_max_count_of_messages()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->retrieve_sent_and_max_count_of_messages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WTSMSLimits**](WTSMSLimits.md)

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

# **save_imported_list**
> ImportedList save_imported_list(list_id, wtsms_imported_list_create)

Save imported list

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wtsms_imported_list_create import WTSMSImportedListCreate
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    wtsms_imported_list_create = WTSMSImportedListCreate(
        phone_number_id=NanoID("C"),
        is_active=True,
        list_name="Import on 19 Dec, 2021",
    ) # WTSMSImportedListCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Save imported list
        api_response = api_instance.save_imported_list(list_id, wtsms_imported_list_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->save_imported_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **wtsms_imported_list_create** | [**WTSMSImportedListCreate**](WTSMSImportedListCreate.md)|  |

### Return type

[**ImportedList**](ImportedList.md)

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

# **save_opt_in_list**
> OptInList save_opt_in_list(list_id, wt_opt_in_list_creation_params)

Save opt in list

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_opt_in_list_creation_params import WTOptInListCreationParams
from wallet.model.opt_in_list import OptInList
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
    api_instance = sms_api.SMSApi(api_client)
    list_id = NanoID("C") # NanoID | 
    wt_opt_in_list_creation_params = WTOptInListCreationParams(
        is_active=True,
        list_name="Christmas Offers",
        phone_number_id=SSNanoID("C"),
        estimated_messages_per_month=2500,
        opt_in_keyword="SUBS",
        opt_out_keyword="UNSUB",
        opt_in_confirmed_response="Welcome to the list",
        opt_out_confirmed_response="Sorry to see you go",
        opt_in_confirmed_customer_receives="Welcome to the list",
        opt_out_confirmed_customer_receives="Sorry to see you go",
        is_over21_required=True,
        opt_in_confirmed_media_urls=[
            "opt_in_confirmed_media_urls_example",
        ],
        opt_out_confirmed_media_urls=[
            "opt_out_confirmed_media_urls_example",
        ],
    ) # WTOptInListCreationParams | 

    # example passing only required values which don't have defaults set
    try:
        # Save opt in list
        api_response = api_instance.save_opt_in_list(list_id, wt_opt_in_list_creation_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->save_opt_in_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **NanoID**|  |
 **wt_opt_in_list_creation_params** | [**WTOptInListCreationParams**](WTOptInListCreationParams.md)|  |

### Return type

[**OptInList**](OptInList.md)

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

# **save_opt_in_list_source**
> OptInListSource save_opt_in_list_source(source_id, wtsms_opt_in_list_source_create)

Save opt in list source

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.opt_in_list_source import OptInListSource
from wallet.model.nano_id import NanoID
from wallet.model.wtsms_opt_in_list_source_create import WTSMSOptInListSourceCreate
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
    api_instance = sms_api.SMSApi(api_client)
    source_id = NanoID("C") # NanoID | 
    wtsms_opt_in_list_source_create = WTSMSOptInListSourceCreate(
        list_id=NanoID("C"),
        source_name="Social Media",
    ) # WTSMSOptInListSourceCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Save opt in list source
        api_response = api_instance.save_opt_in_list_source(source_id, wtsms_opt_in_list_source_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->save_opt_in_list_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **NanoID**|  |
 **wtsms_opt_in_list_source_create** | [**WTSMSOptInListSourceCreate**](WTSMSOptInListSourceCreate.md)|  |

### Return type

[**OptInListSource**](OptInListSource.md)

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

# **send_phone_number_for_verification**
> str send_phone_number_for_verification(phone_number_id, wtsms_update_phone_number_config)

Request phone number verification

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.wtsms_update_phone_number_config import WTSMSUpdatePhoneNumberConfig
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 
    wtsms_update_phone_number_config = WTSMSUpdatePhoneNumberConfig(
        company_name="Wallet Inc",
        privacy_policy_url="https://example.com/privacy-policy",
        terms_of_service_url="https://example.comterms-of-service",
        message_footer="Info message from Wallet Inc",
        stop_response="Sorry to see you go",
        help_response="How can we help you?",
        help_desk_keyword="HELPME",
        help_desk_queue_response="How can we help you?",
        is_connected_to_watson=True,
        watson_username="watson_username_example",
        watson_password="watson_password_example",
        watson_conversation_workplace_id="watson_conversation_workplace_id_example",
    ) # WTSMSUpdatePhoneNumberConfig | 

    # example passing only required values which don't have defaults set
    try:
        # Request phone number verification
        api_response = api_instance.send_phone_number_for_verification(phone_number_id, wtsms_update_phone_number_config)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->send_phone_number_for_verification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |
 **wtsms_update_phone_number_config** | [**WTSMSUpdatePhoneNumberConfig**](WTSMSUpdatePhoneNumberConfig.md)|  |

### Return type

**str**

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

# **update_phone_number**
> PhoneNumber update_phone_number(phone_number_id, wtsms_update_phone_number_config)

Update phone number

### Example


```python
import time
import wallet
from wallet.api import sms_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.wtsms_update_phone_number_config import WTSMSUpdatePhoneNumberConfig
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = sms_api.SMSApi(api_client)
    phone_number_id = NanoID("C") # NanoID | 
    wtsms_update_phone_number_config = WTSMSUpdatePhoneNumberConfig(
        company_name="Wallet Inc",
        privacy_policy_url="https://example.com/privacy-policy",
        terms_of_service_url="https://example.comterms-of-service",
        message_footer="Info message from Wallet Inc",
        stop_response="Sorry to see you go",
        help_response="How can we help you?",
        help_desk_keyword="HELPME",
        help_desk_queue_response="How can we help you?",
        is_connected_to_watson=True,
        watson_username="watson_username_example",
        watson_password="watson_password_example",
        watson_conversation_workplace_id="watson_conversation_workplace_id_example",
    ) # WTSMSUpdatePhoneNumberConfig | 

    # example passing only required values which don't have defaults set
    try:
        # Update phone number
        api_response = api_instance.update_phone_number(phone_number_id, wtsms_update_phone_number_config)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SMSApi->update_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **NanoID**|  |
 **wtsms_update_phone_number_config** | [**WTSMSUpdatePhoneNumberConfig**](WTSMSUpdatePhoneNumberConfig.md)|  |

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

