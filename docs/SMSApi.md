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
[**fetch_sms_agreement**](SMSApi.md#fetch_sms_agreement) | **GET** /v2/sms/agreement | Accept SMS agreement (DEPRECATED)
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
import wallet
from wallet.models.phone_number import PhoneNumber
from wallet.models.wtsms_acquire_phone_number import WTSMSAcquirePhoneNumber
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
    api_instance = wallet.SMSApi(api_client)
    wtsms_acquire_phone_number = wallet.WTSMSAcquirePhoneNumber() # WTSMSAcquirePhoneNumber | 

    try:
        # Acquire phone number
        api_response = api_instance.acquire_phone_number(wtsms_acquire_phone_number)
        print("The response of SMSApi->acquire_phone_number:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Archive phone number
        api_response = api_instance.archive_phone_number(phone_number_id)
        print("The response of SMSApi->archive_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->archive_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

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
import wallet
from wallet.models.imported_list_recipient import ImportedListRecipient
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
    api_instance = wallet.SMSApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive recipient
        api_response = api_instance.archive_recipient(id)
        print("The response of SMSApi->archive_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->archive_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
> WTCountResult count_imported_list_recipients(list_id, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)

Count imported list recipients

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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    is_archive_included = True # bool |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count imported list recipients
        api_response = api_instance.count_imported_list_recipients(list_id, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        print("The response of SMSApi->count_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->count_imported_list_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
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
> WTCountResult count_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)

Count opt in list subscribers

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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count opt in list subscribers
        api_response = api_instance.count_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        print("The response of SMSApi->count_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->count_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
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
> WTCountResult count_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)

Count opt in source subscribers

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
    api_instance = wallet.SMSApi(api_client)
    source_id = 'source_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count opt in source subscribers
        api_response = api_instance.count_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        print("The response of SMSApi->count_opt_in_source_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->count_opt_in_source_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
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
> WTCountResult count_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)

Count outbound SMS

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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)

    try:
        # Count outbound SMS
        api_response = api_instance.count_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)
        print("The response of SMSApi->count_outbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->count_outbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **to_phone_number** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **payment_object_broadcast_id** | **str**|  | [optional] 

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
import wallet
from wallet.models.imported_list import ImportedList
from wallet.models.wtsms_imported_list_create import WTSMSImportedListCreate
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
    api_instance = wallet.SMSApi(api_client)
    wtsms_imported_list_create = wallet.WTSMSImportedListCreate() # WTSMSImportedListCreate | 

    try:
        # Create imported list
        api_response = api_instance.create_imported_list(wtsms_imported_list_create)
        print("The response of SMSApi->create_imported_list:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.opt_in_list import OptInList
from wallet.models.wt_opt_in_list_creation_params import WTOptInListCreationParams
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
    api_instance = wallet.SMSApi(api_client)
    wt_opt_in_list_creation_params = wallet.WTOptInListCreationParams() # WTOptInListCreationParams | 

    try:
        # Create opt in list
        api_response = api_instance.create_opt_in_list(wt_opt_in_list_creation_params)
        print("The response of SMSApi->create_opt_in_list:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.opt_in_list_source import OptInListSource
from wallet.models.wtsms_opt_in_list_source_create import WTSMSOptInListSourceCreate
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
    api_instance = wallet.SMSApi(api_client)
    wtsms_opt_in_list_source_create = wallet.WTSMSOptInListSourceCreate() # WTSMSOptInListSourceCreate | 

    try:
        # Send SMS to opt in list
        api_response = api_instance.create_opt_in_list_source(wtsms_opt_in_list_source_create)
        print("The response of SMSApi->create_opt_in_list_source:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.imported_list_recipient import ImportedListRecipient
from wallet.models.ss_imported_list_recipient_create_params import SSImportedListRecipientCreateParams
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
    api_instance = wallet.SMSApi(api_client)
    ss_imported_list_recipient_create_params = wallet.SSImportedListRecipientCreateParams() # SSImportedListRecipientCreateParams | 

    try:
        # Add new recipient in an imported list
        api_response = api_instance.create_recipient_in_imported_list(ss_imported_list_recipient_create_params)
        print("The response of SMSApi->create_recipient_in_imported_list:\n")
        pprint(api_response)
    except Exception as e:
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

# **export_imported_list_recipients**
> str export_imported_list_recipients(imported_list_id)

Export imported list recipients

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
    api_instance = wallet.SMSApi(api_client)
    imported_list_id = 'imported_list_id_example' # str | 

    try:
        # Export imported list recipients
        api_response = api_instance.export_imported_list_recipients(imported_list_id)
        print("The response of SMSApi->export_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->export_imported_list_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_list_id** | **str**|  | 

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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Export opt in list subscribers
        api_response = api_instance.export_opt_in_list_subscribers(list_id)
        print("The response of SMSApi->export_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->export_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

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
> List[Tcpa] fetch_blocked_tcpa_entries(phone_number_id)

Fetch blocked TCPA entries

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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Fetch blocked TCPA entries
        api_response = api_instance.fetch_blocked_tcpa_entries(phone_number_id)
        print("The response of SMSApi->fetch_blocked_tcpa_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_blocked_tcpa_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

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

# **fetch_imported_list_recipients**
> List[ImportedListRecipient] fetch_imported_list_recipients(list_id)

Fetch imported list recipients

### Example


```python
import wallet
from wallet.models.imported_list_recipient import ImportedListRecipient
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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Fetch imported list recipients
        api_response = api_instance.fetch_imported_list_recipients(list_id)
        print("The response of SMSApi->fetch_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_imported_list_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

[**List[ImportedListRecipient]**](ImportedListRecipient.md)

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
> FetchImportedListRecipientsByPage200Response fetch_imported_list_recipients_by_page(list_id, page_size=page_size, page_num=page_num, is_archive_included=is_archive_included)

Fetch imported list recipients by page

### Example


```python
import wallet
from wallet.models.fetch_imported_list_recipients_by_page200_response import FetchImportedListRecipientsByPage200Response
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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch imported list recipients by page
        api_response = api_instance.fetch_imported_list_recipients_by_page(list_id, page_size=page_size, page_num=page_num, is_archive_included=is_archive_included)
        print("The response of SMSApi->fetch_imported_list_recipients_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_imported_list_recipients_by_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **page_size** | **float**|  | [optional] 
 **page_num** | **float**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**FetchImportedListRecipientsByPage200Response**](FetchImportedListRecipientsByPage200Response.md)

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
> object fetch_opt_in_list_sources(is_archive_included=is_archive_included)

Fetch all opt in list sources

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
    api_instance = wallet.SMSApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all opt in list sources
        api_response = api_instance.fetch_opt_in_list_sources(is_archive_included=is_archive_included)
        print("The response of SMSApi->fetch_opt_in_list_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_sources: %s\n" % e)
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

# **fetch_opt_in_list_subscribers**
> List[OptInListSubscriber] fetch_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)

Fetch opt in list subscribers

### Example


```python
import wallet
from wallet.models.opt_in_list_subscriber import OptInListSubscriber
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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch opt in list subscribers
        api_response = api_instance.fetch_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        print("The response of SMSApi->fetch_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[OptInListSubscriber]**](OptInListSubscriber.md)

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
> FetchOptInListSubscribersByPage200Response fetch_opt_in_list_subscribers_by_page(list_id, page_size=page_size, page_num=page_num, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)

Fetch opt in list subscribers by page

### Example


```python
import wallet
from wallet.models.fetch_opt_in_list_subscribers_by_page200_response import FetchOptInListSubscribersByPage200Response
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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch opt in list subscribers by page
        api_response = api_instance.fetch_opt_in_list_subscribers_by_page(list_id, page_size=page_size, page_num=page_num, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        print("The response of SMSApi->fetch_opt_in_list_subscribers_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_opt_in_list_subscribers_by_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **page_size** | **float**|  | [optional] 
 **page_num** | **float**|  | [optional] 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**FetchOptInListSubscribersByPage200Response**](FetchOptInListSubscribersByPage200Response.md)

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
> List[OptInList] fetch_opt_in_lists_associated_with_phone_number(phone_number_id)

Fetch opt in lists

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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Fetch opt in lists
        api_response = api_instance.fetch_opt_in_lists_associated_with_phone_number(phone_number_id)
        print("The response of SMSApi->fetch_opt_in_lists_associated_with_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_opt_in_lists_associated_with_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**List[OptInList]**](OptInList.md)

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
> List[OptInListSubscriber] fetch_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)

Fetch opt in source subscribers

### Example


```python
import wallet
from wallet.models.opt_in_list_subscriber import OptInListSubscriber
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
    api_instance = wallet.SMSApi(api_client)
    source_id = 'source_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch opt in source subscribers
        api_response = api_instance.fetch_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        print("The response of SMSApi->fetch_opt_in_source_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_opt_in_source_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[OptInListSubscriber]**](OptInListSubscriber.md)

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
> List[OptInListSource] fetch_opt_in_sources_associated_with_phone_number(phone_number_id)

Fetch opt in sources

### Example


```python
import wallet
from wallet.models.opt_in_list_source import OptInListSource
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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Fetch opt in sources
        api_response = api_instance.fetch_opt_in_sources_associated_with_phone_number(phone_number_id)
        print("The response of SMSApi->fetch_opt_in_sources_associated_with_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_opt_in_sources_associated_with_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**List[OptInListSource]**](OptInListSource.md)

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
> List[OutboundSMS] fetch_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)

Fetch outbound SMS

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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)

    try:
        # Fetch outbound SMS
        api_response = api_instance.fetch_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)
        print("The response of SMSApi->fetch_outbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_outbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **to_phone_number** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **payment_object_broadcast_id** | **str**|  | [optional] 

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

# **fetch_outbound_smsby_page**
> FetchOutboundSMSByPage200Response fetch_outbound_smsby_page(phone_number_id, to_phone_number=to_phone_number, payment_object_broadcast_id=payment_object_broadcast_id, page_size=page_size, page_num=page_num, status=status)

Fetch outbound SMSes by page

### Example


```python
import wallet
from wallet.models.fetch_outbound_smsby_page200_response import FetchOutboundSMSByPage200Response
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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)
    status = wallet.SSOutboundStatuses() # SSOutboundStatuses |  (optional)

    try:
        # Fetch outbound SMSes by page
        api_response = api_instance.fetch_outbound_smsby_page(phone_number_id, to_phone_number=to_phone_number, payment_object_broadcast_id=payment_object_broadcast_id, page_size=page_size, page_num=page_num, status=status)
        print("The response of SMSApi->fetch_outbound_smsby_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_outbound_smsby_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **to_phone_number** | **str**|  | [optional] 
 **payment_object_broadcast_id** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **page_num** | **float**|  | [optional] 
 **status** | [**SSOutboundStatuses**](.md)|  | [optional] 

### Return type

[**FetchOutboundSMSByPage200Response**](FetchOutboundSMSByPage200Response.md)

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
> List[StaticVoucherCampaignBroadcast] fetch_payment_object_broadcasts(phone_number_id)

Fetch payment object broadcasts

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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Fetch payment object broadcasts
        api_response = api_instance.fetch_payment_object_broadcasts(phone_number_id)
        print("The response of SMSApi->fetch_payment_object_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_payment_object_broadcasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

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

# **fetch_sms_agreement**
> object fetch_sms_agreement()

Accept SMS agreement (DEPRECATED)

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
    api_instance = wallet.SMSApi(api_client)

    try:
        # Accept SMS agreement (DEPRECATED)
        api_response = api_instance.fetch_sms_agreement()
        print("The response of SMSApi->fetch_sms_agreement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->fetch_sms_agreement: %s\n" % e)
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

# **import_imported_list_recipients**
> str import_imported_list_recipients(imported_list_id, wt_employee_import_records)

Import imported list recipients

### Example


```python
import wallet
from wallet.models.wt_employee_import_records import WTEmployeeImportRecords
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
    api_instance = wallet.SMSApi(api_client)
    imported_list_id = 'imported_list_id_example' # str | 
    wt_employee_import_records = wallet.WTEmployeeImportRecords() # WTEmployeeImportRecords | 

    try:
        # Import imported list recipients
        api_response = api_instance.import_imported_list_recipients(imported_list_id, wt_employee_import_records)
        print("The response of SMSApi->import_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->import_imported_list_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imported_list_id** | **str**|  | 
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
import wallet
from wallet.models.wt_imported_list_recipient_from_membership_tier_import import WTImportedListRecipientFromMembershipTierImport
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
    api_instance = wallet.SMSApi(api_client)
    wt_imported_list_recipient_from_membership_tier_import = wallet.WTImportedListRecipientFromMembershipTierImport() # WTImportedListRecipientFromMembershipTierImport | 

    try:
        # Import imported list recipients from a given membership tier
        api_response = api_instance.import_imported_list_recipients_from_membership_tier(wt_imported_list_recipient_from_membership_tier_import)
        print("The response of SMSApi->import_imported_list_recipients_from_membership_tier:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wtsms_import_opt_in_list_subscribers import WTSMSImportOptInListSubscribers
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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    wtsms_import_opt_in_list_subscribers = wallet.WTSMSImportOptInListSubscribers() # WTSMSImportOptInListSubscribers | 

    try:
        # Import opt in list subscribers
        api_response = api_instance.import_opt_in_list_subscribers(list_id, wtsms_import_opt_in_list_subscribers)
        print("The response of SMSApi->import_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->import_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Restore phone number
        api_response = api_instance.restore_phone_number(phone_number_id)
        print("The response of SMSApi->restore_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->restore_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

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
import wallet
from wallet.models.imported_list_recipient import ImportedListRecipient
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
    api_instance = wallet.SMSApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore recipient
        api_response = api_instance.restore_recipient(id)
        print("The response of SMSApi->restore_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->restore_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
> object retrieve_sent_and_max_count_of_messages()

Retrieve the number of messages sent by the merchant within the current billing cycle

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
    api_instance = wallet.SMSApi(api_client)

    try:
        # Retrieve the number of messages sent by the merchant within the current billing cycle
        api_response = api_instance.retrieve_sent_and_max_count_of_messages()
        print("The response of SMSApi->retrieve_sent_and_max_count_of_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->retrieve_sent_and_max_count_of_messages: %s\n" % e)
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

# **save_imported_list**
> ImportedList save_imported_list(list_id, wtsms_imported_list_create)

Save imported list

### Example


```python
import wallet
from wallet.models.imported_list import ImportedList
from wallet.models.wtsms_imported_list_create import WTSMSImportedListCreate
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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    wtsms_imported_list_create = wallet.WTSMSImportedListCreate() # WTSMSImportedListCreate | 

    try:
        # Save imported list
        api_response = api_instance.save_imported_list(list_id, wtsms_imported_list_create)
        print("The response of SMSApi->save_imported_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->save_imported_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
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
import wallet
from wallet.models.opt_in_list import OptInList
from wallet.models.wt_opt_in_list_creation_params import WTOptInListCreationParams
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
    api_instance = wallet.SMSApi(api_client)
    list_id = 'list_id_example' # str | 
    wt_opt_in_list_creation_params = wallet.WTOptInListCreationParams() # WTOptInListCreationParams | 

    try:
        # Save opt in list
        api_response = api_instance.save_opt_in_list(list_id, wt_opt_in_list_creation_params)
        print("The response of SMSApi->save_opt_in_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->save_opt_in_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
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
import wallet
from wallet.models.opt_in_list_source import OptInListSource
from wallet.models.wtsms_opt_in_list_source_create import WTSMSOptInListSourceCreate
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
    api_instance = wallet.SMSApi(api_client)
    source_id = 'source_id_example' # str | 
    wtsms_opt_in_list_source_create = wallet.WTSMSOptInListSourceCreate() # WTSMSOptInListSourceCreate | 

    try:
        # Save opt in list source
        api_response = api_instance.save_opt_in_list_source(source_id, wtsms_opt_in_list_source_create)
        print("The response of SMSApi->save_opt_in_list_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->save_opt_in_list_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
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
import wallet
from wallet.models.wtsms_update_phone_number_config import WTSMSUpdatePhoneNumberConfig
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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    wtsms_update_phone_number_config = wallet.WTSMSUpdatePhoneNumberConfig() # WTSMSUpdatePhoneNumberConfig | 

    try:
        # Request phone number verification
        api_response = api_instance.send_phone_number_for_verification(phone_number_id, wtsms_update_phone_number_config)
        print("The response of SMSApi->send_phone_number_for_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->send_phone_number_for_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
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
import wallet
from wallet.models.phone_number import PhoneNumber
from wallet.models.wtsms_update_phone_number_config import WTSMSUpdatePhoneNumberConfig
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
    api_instance = wallet.SMSApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    wtsms_update_phone_number_config = wallet.WTSMSUpdatePhoneNumberConfig() # WTSMSUpdatePhoneNumberConfig | 

    try:
        # Update phone number
        api_response = api_instance.update_phone_number(phone_number_id, wtsms_update_phone_number_config)
        print("The response of SMSApi->update_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSApi->update_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
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

