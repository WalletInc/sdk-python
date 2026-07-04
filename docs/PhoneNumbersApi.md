# wallet.PhoneNumbersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquire_phone_number**](PhoneNumbersApi.md#acquire_phone_number) | **POST** /v2/sms/phoneNumber/acquire | Acquire phone number
[**archive_phone_number**](PhoneNumbersApi.md#archive_phone_number) | **DELETE** /v2/sms/phoneNumber/{phoneNumberID} | Archive phone number
[**fetch_blocked_tcpa_entries**](PhoneNumbersApi.md#fetch_blocked_tcpa_entries) | **GET** /v2/sms/phoneNumber/blocked/{phoneNumberID} | Get blocked TCPA entries
[**fetch_merchant_phone_numbers**](PhoneNumbersApi.md#fetch_merchant_phone_numbers) | **GET** /v2/merchant/phoneNumbers/all | Get all phone numbers
[**fetch_phone_number**](PhoneNumbersApi.md#fetch_phone_number) | **GET** /v2/merchant/phoneNumber/{phoneNumberID} | Get phone number
[**fetch_sms_agreement**](PhoneNumbersApi.md#fetch_sms_agreement) | **GET** /v2/sms/agreement | Get SMS Agreement
[**fetch_tcpa_filter**](PhoneNumbersApi.md#fetch_tcpa_filter) | **GET** /v2/merchant/tcpa/filter/all | Get all TCPA Filters
[**restore_phone_number**](PhoneNumbersApi.md#restore_phone_number) | **PATCH** /v2/sms/phoneNumber/{phoneNumberID} | Restore phone number
[**send_phone_number_for_verification**](PhoneNumbersApi.md#send_phone_number_for_verification) | **PUT** /v2/sms/phoneNumber/verification/{phoneNumberID} | Request phone number verification
[**update_phone_number**](PhoneNumbersApi.md#update_phone_number) | **PUT** /v2/sms/phoneNumber/{phoneNumberID} | Update phone number


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
    api_instance = wallet.PhoneNumbersApi(api_client)
    wtsms_acquire_phone_number = wallet.WTSMSAcquirePhoneNumber() # WTSMSAcquirePhoneNumber | 

    try:
        # Acquire phone number
        api_response = api_instance.acquire_phone_number(wtsms_acquire_phone_number)
        print("The response of PhoneNumbersApi->acquire_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->acquire_phone_number: %s\n" % e)
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
    api_instance = wallet.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Archive phone number
        api_response = api_instance.archive_phone_number(phone_number_id)
        print("The response of PhoneNumbersApi->archive_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->archive_phone_number: %s\n" % e)
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

# **fetch_blocked_tcpa_entries**
> List[Tcpa] fetch_blocked_tcpa_entries(phone_number_id)

Get blocked TCPA entries

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
    api_instance = wallet.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Get blocked TCPA entries
        api_response = api_instance.fetch_blocked_tcpa_entries(phone_number_id)
        print("The response of PhoneNumbersApi->fetch_blocked_tcpa_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->fetch_blocked_tcpa_entries: %s\n" % e)
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

# **fetch_merchant_phone_numbers**
> object fetch_merchant_phone_numbers(is_archive_included=is_archive_included, is_approved=is_approved)

Get all phone numbers

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
    api_instance = wallet.PhoneNumbersApi(api_client)
    is_archive_included = True # bool |  (optional)
    is_approved = True # bool |  (optional)

    try:
        # Get all phone numbers
        api_response = api_instance.fetch_merchant_phone_numbers(is_archive_included=is_archive_included, is_approved=is_approved)
        print("The response of PhoneNumbersApi->fetch_merchant_phone_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->fetch_merchant_phone_numbers: %s\n" % e)
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

# **fetch_phone_number**
> PhoneNumber fetch_phone_number(phone_number_id)

Get phone number

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
    api_instance = wallet.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Get phone number
        api_response = api_instance.fetch_phone_number(phone_number_id)
        print("The response of PhoneNumbersApi->fetch_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->fetch_phone_number: %s\n" % e)
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

# **fetch_sms_agreement**
> object fetch_sms_agreement()

Get SMS Agreement

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
    api_instance = wallet.PhoneNumbersApi(api_client)

    try:
        # Get SMS Agreement
        api_response = api_instance.fetch_sms_agreement()
        print("The response of PhoneNumbersApi->fetch_sms_agreement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->fetch_sms_agreement: %s\n" % e)
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

# **fetch_tcpa_filter**
> List[Tcpa] fetch_tcpa_filter()

Get all TCPA Filters

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
    api_instance = wallet.PhoneNumbersApi(api_client)

    try:
        # Get all TCPA Filters
        api_response = api_instance.fetch_tcpa_filter()
        print("The response of PhoneNumbersApi->fetch_tcpa_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->fetch_tcpa_filter: %s\n" % e)
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
    api_instance = wallet.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Restore phone number
        api_response = api_instance.restore_phone_number(phone_number_id)
        print("The response of PhoneNumbersApi->restore_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->restore_phone_number: %s\n" % e)
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
    api_instance = wallet.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    wtsms_update_phone_number_config = wallet.WTSMSUpdatePhoneNumberConfig() # WTSMSUpdatePhoneNumberConfig | 

    try:
        # Request phone number verification
        api_response = api_instance.send_phone_number_for_verification(phone_number_id, wtsms_update_phone_number_config)
        print("The response of PhoneNumbersApi->send_phone_number_for_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->send_phone_number_for_verification: %s\n" % e)
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
    api_instance = wallet.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 
    wtsms_update_phone_number_config = wallet.WTSMSUpdatePhoneNumberConfig() # WTSMSUpdatePhoneNumberConfig | 

    try:
        # Update phone number
        api_response = api_instance.update_phone_number(phone_number_id, wtsms_update_phone_number_config)
        print("The response of PhoneNumbersApi->update_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->update_phone_number: %s\n" % e)
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

