# wallet.SMSMessagesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_inbound_sms**](SMSMessagesApi.md#count_inbound_sms) | **GET** /v2/merchant/sms/inbound/count/{phoneNumberID} | Count inbound SMSes
[**count_outbound_sms**](SMSMessagesApi.md#count_outbound_sms) | **GET** /v2/sms/outbound/count/{phoneNumberID} | Count outbound SMS
[**estimate_sms_segments**](SMSMessagesApi.md#estimate_sms_segments) | **POST** /sms/segment-estimate | Estimate SMS/MMS segments for a message
[**export_inbound_messages**](SMSMessagesApi.md#export_inbound_messages) | **PUT** /v2/merchant/sms/inbound/export/{phoneNumberID} | Export inbound messages
[**export_outbound_messages**](SMSMessagesApi.md#export_outbound_messages) | **PUT** /v2/merchant/sms/outbound/export/{phoneNumberID} | Export outbound messages
[**fetch_inbound_sms**](SMSMessagesApi.md#fetch_inbound_sms) | **GET** /v2/merchant/sms/inbound/{phoneNumberID} | Get inbound SMSes
[**fetch_inbound_smsby_page**](SMSMessagesApi.md#fetch_inbound_smsby_page) | **GET** /v2/merchant/sms/inbound/page/{phoneNumberID} | Get inbound SMSes by page
[**fetch_merchant_outbound_sms**](SMSMessagesApi.md#fetch_merchant_outbound_sms) | **GET** /v2/merchant/sms/outbound/{phoneNumberID} | Get outbound SMSes
[**fetch_outbound_sms**](SMSMessagesApi.md#fetch_outbound_sms) | **GET** /v2/sms/outbound/{phoneNumberID} | Get outbound SMS
[**fetch_outbound_smsby_page**](SMSMessagesApi.md#fetch_outbound_smsby_page) | **GET** /v2/sms/outbound/page/{phoneNumberID} | Get outbound SMSes by page
[**retrieve_sent_and_max_count_of_messages**](SMSMessagesApi.md#retrieve_sent_and_max_count_of_messages) | **GET** /v2/sms/sent | Retrieve the number of messages sent by the merchant within the current billing cycle


# **count_inbound_sms**
> WTCountResult count_inbound_sms(phone_number_id, from_phone_number=from_phone_number, body=body, start_date=start_date, end_date=end_date)

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    from_phone_number = 'from_phone_number_example' # str |  (optional)
    body = 'body_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count inbound SMSes
        api_response = api_instance.count_inbound_sms(phone_number_id, from_phone_number=from_phone_number, body=body, start_date=start_date, end_date=end_date)
        print("The response of SMSMessagesApi->count_inbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->count_inbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **from_phone_number** | **str**|  | [optional] 
 **body** | **str**|  | [optional] 
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
> WTCountResult count_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id, start_date=start_date, end_date=end_date)

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count outbound SMS
        api_response = api_instance.count_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id, start_date=start_date, end_date=end_date)
        print("The response of SMSMessagesApi->count_outbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->count_outbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **to_phone_number** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **payment_object_broadcast_id** | **str**|  | [optional] 
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

# **estimate_sms_segments**
> WTSegmentEstimate estimate_sms_segments(wt_segment_estimate_request)

Estimate SMS/MMS segments for a message

### Example


```python
import wallet
from wallet.models.wt_segment_estimate import WTSegmentEstimate
from wallet.models.wt_segment_estimate_request import WTSegmentEstimateRequest
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
    api_instance = wallet.SMSMessagesApi(api_client)
    wt_segment_estimate_request = wallet.WTSegmentEstimateRequest() # WTSegmentEstimateRequest | 

    try:
        # Estimate SMS/MMS segments for a message
        api_response = api_instance.estimate_sms_segments(wt_segment_estimate_request)
        print("The response of SMSMessagesApi->estimate_sms_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->estimate_sms_segments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_segment_estimate_request** | [**WTSegmentEstimateRequest**](WTSegmentEstimateRequest.md)|  | 

### Return type

[**WTSegmentEstimate**](WTSegmentEstimate.md)

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    locale = 'locale_example' # str | 

    try:
        # Export inbound messages
        api_response = api_instance.export_inbound_messages(phone_number_id, locale)
        print("The response of SMSMessagesApi->export_inbound_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->export_inbound_messages: %s\n" % e)
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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    locale = 'locale_example' # str | 
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)

    try:
        # Export outbound messages
        api_response = api_instance.export_outbound_messages(phone_number_id, locale, payment_object_broadcast_id=payment_object_broadcast_id)
        print("The response of SMSMessagesApi->export_outbound_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->export_outbound_messages: %s\n" % e)
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

# **fetch_inbound_sms**
> List[InboundSMS] fetch_inbound_sms(phone_number_id, from_phone_number=from_phone_number)

Get inbound SMSes

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    from_phone_number = 'from_phone_number_example' # str |  (optional)

    try:
        # Get inbound SMSes
        api_response = api_instance.fetch_inbound_sms(phone_number_id, from_phone_number=from_phone_number)
        print("The response of SMSMessagesApi->fetch_inbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->fetch_inbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
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
> FetchInboundSMSByPage200Response fetch_inbound_smsby_page(phone_number_id, from_phone_number=from_phone_number, page_size=page_size, page_num=page_num, start_date=start_date, end_date=end_date)

Get inbound SMSes by page

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    from_phone_number = 'from_phone_number_example' # str |  (optional)
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get inbound SMSes by page
        api_response = api_instance.fetch_inbound_smsby_page(phone_number_id, from_phone_number=from_phone_number, page_size=page_size, page_num=page_num, start_date=start_date, end_date=end_date)
        print("The response of SMSMessagesApi->fetch_inbound_smsby_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->fetch_inbound_smsby_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
 **from_phone_number** | **str**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **page_num** | **float**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

Get outbound SMSes

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    to_phone_number = 'to_phone_number_example' # str | 

    try:
        # Get outbound SMSes
        api_response = api_instance.fetch_merchant_outbound_sms(phone_number_id, to_phone_number)
        print("The response of SMSMessagesApi->fetch_merchant_outbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->fetch_merchant_outbound_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 
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

# **fetch_outbound_sms**
> List[OutboundSMS] fetch_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)

Get outbound SMS

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)

    try:
        # Get outbound SMS
        api_response = api_instance.fetch_outbound_sms(phone_number_id, to_phone_number=to_phone_number, status=status, payment_object_broadcast_id=payment_object_broadcast_id)
        print("The response of SMSMessagesApi->fetch_outbound_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->fetch_outbound_sms: %s\n" % e)
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
> FetchOutboundSMSByPage200Response fetch_outbound_smsby_page(phone_number_id, to_phone_number=to_phone_number, payment_object_broadcast_id=payment_object_broadcast_id, page_size=page_size, page_num=page_num, status=status, start_date=start_date, end_date=end_date)

Get outbound SMSes by page

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
    api_instance = wallet.SMSMessagesApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)
    payment_object_broadcast_id = 'payment_object_broadcast_id_example' # str |  (optional)
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)
    status = wallet.SSOutboundStatuses() # SSOutboundStatuses |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get outbound SMSes by page
        api_response = api_instance.fetch_outbound_smsby_page(phone_number_id, to_phone_number=to_phone_number, payment_object_broadcast_id=payment_object_broadcast_id, page_size=page_size, page_num=page_num, status=status, start_date=start_date, end_date=end_date)
        print("The response of SMSMessagesApi->fetch_outbound_smsby_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->fetch_outbound_smsby_page: %s\n" % e)
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
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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
    api_instance = wallet.SMSMessagesApi(api_client)

    try:
        # Retrieve the number of messages sent by the merchant within the current billing cycle
        api_response = api_instance.retrieve_sent_and_max_count_of_messages()
        print("The response of SMSMessagesApi->retrieve_sent_and_max_count_of_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSMessagesApi->retrieve_sent_and_max_count_of_messages: %s\n" % e)
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

