# wallet.BroadcastsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_payment_object_broadcast**](BroadcastsApi.md#archive_payment_object_broadcast) | **DELETE** /v2/merchant/paymentObjectBroadcast/{broadcastID} | Archive payment object broadcast
[**fetch_advertisement_credit_broadcasts**](BroadcastsApi.md#fetch_advertisement_credit_broadcasts) | **GET** /v2/merchant/broadcasts/adCredits/all | Get all ad credit broadcasts
[**fetch_dynamic_voucher_broadcasts**](BroadcastsApi.md#fetch_dynamic_voucher_broadcasts) | **GET** /v2/merchant/broadcasts/dynamicVouchers/all | Get all dynamic voucher broadcasts
[**fetch_payment_object_broadcasts**](BroadcastsApi.md#fetch_payment_object_broadcasts) | **GET** /v2/sms/paymentObjectBroadcasts/{phoneNumberID} | Get payment object broadcasts
[**fetch_simple_sms_broadcasts**](BroadcastsApi.md#fetch_simple_sms_broadcasts) | **GET** /v2/merchant/broadcasts/simpleSMS/all | Get all simple SMS broadcasts
[**fetch_static_voucher_campaign_broadcasts**](BroadcastsApi.md#fetch_static_voucher_campaign_broadcasts) | **GET** /v2/merchant/broadcasts/staticVoucherCampaign/all | Get all static voucher campaign broadcasts
[**schedule_advertisement_credit**](BroadcastsApi.md#schedule_advertisement_credit) | **POST** /v2/employee/sms/schedule/adCredit/{advertisementCreditID} | Schedule Ad Credit
[**schedule_dynamic_voucher**](BroadcastsApi.md#schedule_dynamic_voucher) | **POST** /v2/employee/sms/schedule/dynamicVoucher/{dynamicVoucherID} | Schedule Dynamic Voucher to list
[**schedule_dynamic_voucher_to_recipient**](BroadcastsApi.md#schedule_dynamic_voucher_to_recipient) | **POST** /v2/employee/sms/schedule/recipient/dynamicVoucher/{dynamicVoucherID} | Schedule Dynamic Voucher to recipient
[**schedule_simple_sms**](BroadcastsApi.md#schedule_simple_sms) | **POST** /v2/employee/sms/schedule/simple | Schedule Simple SMS broadcast to list
[**schedule_simple_smsto_recipient**](BroadcastsApi.md#schedule_simple_smsto_recipient) | **POST** /v2/employee/sms/schedule/recipient/simple | Schedule Simple SMS broadcast to recipient
[**send_sms_campaign_broadcast**](BroadcastsApi.md#send_sms_campaign_broadcast) | **POST** /v2/employee/sms/schedule/campaign/{staticVoucherCampaignID} | Schedule SMS Campaign Broadcast


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
    api_instance = wallet.BroadcastsApi(api_client)
    broadcast_id = 'broadcast_id_example' # str | 

    try:
        # Archive payment object broadcast
        api_response = api_instance.archive_payment_object_broadcast(broadcast_id)
        print("The response of BroadcastsApi->archive_payment_object_broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->archive_payment_object_broadcast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_id** | **str**|  | 

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

# **fetch_advertisement_credit_broadcasts**
> List[AdvertisementCreditBroadcast] fetch_advertisement_credit_broadcasts(is_archive_included=is_archive_included)

Get all ad credit broadcasts

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
    api_instance = wallet.BroadcastsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all ad credit broadcasts
        api_response = api_instance.fetch_advertisement_credit_broadcasts(is_archive_included=is_archive_included)
        print("The response of BroadcastsApi->fetch_advertisement_credit_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->fetch_advertisement_credit_broadcasts: %s\n" % e)
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

# **fetch_dynamic_voucher_broadcasts**
> List[DynamicVoucherBroadcast] fetch_dynamic_voucher_broadcasts(is_archive_included=is_archive_included)

Get all dynamic voucher broadcasts

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
    api_instance = wallet.BroadcastsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all dynamic voucher broadcasts
        api_response = api_instance.fetch_dynamic_voucher_broadcasts(is_archive_included=is_archive_included)
        print("The response of BroadcastsApi->fetch_dynamic_voucher_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->fetch_dynamic_voucher_broadcasts: %s\n" % e)
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

# **fetch_payment_object_broadcasts**
> List[StaticVoucherCampaignBroadcast] fetch_payment_object_broadcasts(phone_number_id)

Get payment object broadcasts

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
    api_instance = wallet.BroadcastsApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Get payment object broadcasts
        api_response = api_instance.fetch_payment_object_broadcasts(phone_number_id)
        print("The response of BroadcastsApi->fetch_payment_object_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->fetch_payment_object_broadcasts: %s\n" % e)
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

# **fetch_simple_sms_broadcasts**
> List[SimpleSMSBroadcast] fetch_simple_sms_broadcasts(is_archive_included=is_archive_included)

Get all simple SMS broadcasts

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
    api_instance = wallet.BroadcastsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all simple SMS broadcasts
        api_response = api_instance.fetch_simple_sms_broadcasts(is_archive_included=is_archive_included)
        print("The response of BroadcastsApi->fetch_simple_sms_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->fetch_simple_sms_broadcasts: %s\n" % e)
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

Get all static voucher campaign broadcasts

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
    api_instance = wallet.BroadcastsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all static voucher campaign broadcasts
        api_response = api_instance.fetch_static_voucher_campaign_broadcasts(is_archive_included=is_archive_included)
        print("The response of BroadcastsApi->fetch_static_voucher_campaign_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->fetch_static_voucher_campaign_broadcasts: %s\n" % e)
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

# **schedule_advertisement_credit**
> AdvertisementCreditBroadcast schedule_advertisement_credit(advertisement_credit_id, wt_employee_schedule_simple_sms)

Schedule Ad Credit

### Example


```python
import wallet
from wallet.models.advertisement_credit_broadcast import AdvertisementCreditBroadcast
from wallet.models.wt_employee_schedule_simple_sms import WTEmployeeScheduleSimpleSMS
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
    api_instance = wallet.BroadcastsApi(api_client)
    advertisement_credit_id = 'advertisement_credit_id_example' # str | 
    wt_employee_schedule_simple_sms = wallet.WTEmployeeScheduleSimpleSMS() # WTEmployeeScheduleSimpleSMS | 

    try:
        # Schedule Ad Credit
        api_response = api_instance.schedule_advertisement_credit(advertisement_credit_id, wt_employee_schedule_simple_sms)
        print("The response of BroadcastsApi->schedule_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->schedule_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisement_credit_id** | **str**|  | 
 **wt_employee_schedule_simple_sms** | [**WTEmployeeScheduleSimpleSMS**](WTEmployeeScheduleSimpleSMS.md)|  | 

### Return type

[**AdvertisementCreditBroadcast**](AdvertisementCreditBroadcast.md)

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
**413** | Entity Too Large |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_dynamic_voucher**
> DynamicVoucherBroadcast schedule_dynamic_voucher(dynamic_voucher_id, wt_employee_schedule_simple_sms)

Schedule Dynamic Voucher to list

### Example


```python
import wallet
from wallet.models.dynamic_voucher_broadcast import DynamicVoucherBroadcast
from wallet.models.wt_employee_schedule_simple_sms import WTEmployeeScheduleSimpleSMS
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
    api_instance = wallet.BroadcastsApi(api_client)
    dynamic_voucher_id = 'dynamic_voucher_id_example' # str | 
    wt_employee_schedule_simple_sms = wallet.WTEmployeeScheduleSimpleSMS() # WTEmployeeScheduleSimpleSMS | 

    try:
        # Schedule Dynamic Voucher to list
        api_response = api_instance.schedule_dynamic_voucher(dynamic_voucher_id, wt_employee_schedule_simple_sms)
        print("The response of BroadcastsApi->schedule_dynamic_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->schedule_dynamic_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | **str**|  | 
 **wt_employee_schedule_simple_sms** | [**WTEmployeeScheduleSimpleSMS**](WTEmployeeScheduleSimpleSMS.md)|  | 

### Return type

[**DynamicVoucherBroadcast**](DynamicVoucherBroadcast.md)

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
**413** | Entity Too Large |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_dynamic_voucher_to_recipient**
> DynamicVoucherBroadcast schedule_dynamic_voucher_to_recipient(dynamic_voucher_id, wt_employee_schedule_simple_smsto_recipient)

Schedule Dynamic Voucher to recipient

### Example


```python
import wallet
from wallet.models.dynamic_voucher_broadcast import DynamicVoucherBroadcast
from wallet.models.wt_employee_schedule_simple_smsto_recipient import WTEmployeeScheduleSimpleSMSToRecipient
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
    api_instance = wallet.BroadcastsApi(api_client)
    dynamic_voucher_id = 'dynamic_voucher_id_example' # str | 
    wt_employee_schedule_simple_smsto_recipient = wallet.WTEmployeeScheduleSimpleSMSToRecipient() # WTEmployeeScheduleSimpleSMSToRecipient | 

    try:
        # Schedule Dynamic Voucher to recipient
        api_response = api_instance.schedule_dynamic_voucher_to_recipient(dynamic_voucher_id, wt_employee_schedule_simple_smsto_recipient)
        print("The response of BroadcastsApi->schedule_dynamic_voucher_to_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->schedule_dynamic_voucher_to_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | **str**|  | 
 **wt_employee_schedule_simple_smsto_recipient** | [**WTEmployeeScheduleSimpleSMSToRecipient**](WTEmployeeScheduleSimpleSMSToRecipient.md)|  | 

### Return type

[**DynamicVoucherBroadcast**](DynamicVoucherBroadcast.md)

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
**413** | Entity Too Large |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_simple_sms**
> bool schedule_simple_sms(wt_employee_schedule_simple_sms)

Schedule Simple SMS broadcast to list

### Example


```python
import wallet
from wallet.models.wt_employee_schedule_simple_sms import WTEmployeeScheduleSimpleSMS
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
    api_instance = wallet.BroadcastsApi(api_client)
    wt_employee_schedule_simple_sms = wallet.WTEmployeeScheduleSimpleSMS() # WTEmployeeScheduleSimpleSMS | 

    try:
        # Schedule Simple SMS broadcast to list
        api_response = api_instance.schedule_simple_sms(wt_employee_schedule_simple_sms)
        print("The response of BroadcastsApi->schedule_simple_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->schedule_simple_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_schedule_simple_sms** | [**WTEmployeeScheduleSimpleSMS**](WTEmployeeScheduleSimpleSMS.md)|  | 

### Return type

**bool**

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
**413** | Entity Too Large |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_simple_smsto_recipient**
> bool schedule_simple_smsto_recipient(wt_employee_schedule_simple_smsto_recipient)

Schedule Simple SMS broadcast to recipient

### Example


```python
import wallet
from wallet.models.wt_employee_schedule_simple_smsto_recipient import WTEmployeeScheduleSimpleSMSToRecipient
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
    api_instance = wallet.BroadcastsApi(api_client)
    wt_employee_schedule_simple_smsto_recipient = wallet.WTEmployeeScheduleSimpleSMSToRecipient() # WTEmployeeScheduleSimpleSMSToRecipient | 

    try:
        # Schedule Simple SMS broadcast to recipient
        api_response = api_instance.schedule_simple_smsto_recipient(wt_employee_schedule_simple_smsto_recipient)
        print("The response of BroadcastsApi->schedule_simple_smsto_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->schedule_simple_smsto_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_schedule_simple_smsto_recipient** | [**WTEmployeeScheduleSimpleSMSToRecipient**](WTEmployeeScheduleSimpleSMSToRecipient.md)|  | 

### Return type

**bool**

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
**413** | Entity Too Large |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_campaign_broadcast**
> StaticVoucherCampaignBroadcast send_sms_campaign_broadcast(static_voucher_campaign_id, wt_employee_schedule_sms_campaign_broadcast)

Schedule SMS Campaign Broadcast

### Example


```python
import wallet
from wallet.models.static_voucher_campaign_broadcast import StaticVoucherCampaignBroadcast
from wallet.models.wt_employee_schedule_sms_campaign_broadcast import WTEmployeeScheduleSMSCampaignBroadcast
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
    api_instance = wallet.BroadcastsApi(api_client)
    static_voucher_campaign_id = 'static_voucher_campaign_id_example' # str | 
    wt_employee_schedule_sms_campaign_broadcast = wallet.WTEmployeeScheduleSMSCampaignBroadcast() # WTEmployeeScheduleSMSCampaignBroadcast | 

    try:
        # Schedule SMS Campaign Broadcast
        api_response = api_instance.send_sms_campaign_broadcast(static_voucher_campaign_id, wt_employee_schedule_sms_campaign_broadcast)
        print("The response of BroadcastsApi->send_sms_campaign_broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastsApi->send_sms_campaign_broadcast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher_campaign_id** | **str**|  | 
 **wt_employee_schedule_sms_campaign_broadcast** | [**WTEmployeeScheduleSMSCampaignBroadcast**](WTEmployeeScheduleSMSCampaignBroadcast.md)|  | 

### Return type

[**StaticVoucherCampaignBroadcast**](StaticVoucherCampaignBroadcast.md)

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
**413** | Entity Too Large |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

