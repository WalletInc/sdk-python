# wallet.KeywordAutoRespondersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_auto_responder**](KeywordAutoRespondersApi.md#archive_auto_responder) | **POST** /autoresponders/archive/{autoResponderID} | Archive a keyword auto-responder
[**create_auto_responder**](KeywordAutoRespondersApi.md#create_auto_responder) | **POST** /autoresponders/create | Create a keyword auto-responder
[**fetch_all_auto_responders**](KeywordAutoRespondersApi.md#fetch_all_auto_responders) | **GET** /autoresponders/fetchAll | List keyword auto-responders
[**fetch_auto_responder_hits**](KeywordAutoRespondersApi.md#fetch_auto_responder_hits) | **GET** /autoresponders/hits | List keyword auto-responder activity
[**restore_auto_responder**](KeywordAutoRespondersApi.md#restore_auto_responder) | **POST** /autoresponders/restore/{autoResponderID} | Restore a keyword auto-responder
[**update_auto_responder**](KeywordAutoRespondersApi.md#update_auto_responder) | **POST** /autoresponders/update | Update a keyword auto-responder


# **archive_auto_responder**
> WTAutoResponder archive_auto_responder(auto_responder_id)

Archive a keyword auto-responder

### Example


```python
import wallet
from wallet.models.wt_auto_responder import WTAutoResponder
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
    api_instance = wallet.KeywordAutoRespondersApi(api_client)
    auto_responder_id = 'auto_responder_id_example' # str | 

    try:
        # Archive a keyword auto-responder
        api_response = api_instance.archive_auto_responder(auto_responder_id)
        print("The response of KeywordAutoRespondersApi->archive_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeywordAutoRespondersApi->archive_auto_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_responder_id** | **str**|  | 

### Return type

[**WTAutoResponder**](WTAutoResponder.md)

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
**422** | Validation Failed. A refused keyword names the rule it broke in the failing field&#39;s message: reserved-compliance-keyword, opt-out-phrase, date-shaped, help-desk-keyword, opt-in-list-keyword (with a listID field), duplicate (with an existingID field), empty, too-long, or empty-response (on responseBody). |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auto_responder**
> WTAutoResponder create_auto_responder(wt_auto_responder_create_params)

Create a keyword auto-responder

### Example


```python
import wallet
from wallet.models.wt_auto_responder import WTAutoResponder
from wallet.models.wt_auto_responder_create_params import WTAutoResponderCreateParams
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
    api_instance = wallet.KeywordAutoRespondersApi(api_client)
    wt_auto_responder_create_params = wallet.WTAutoResponderCreateParams() # WTAutoResponderCreateParams | 

    try:
        # Create a keyword auto-responder
        api_response = api_instance.create_auto_responder(wt_auto_responder_create_params)
        print("The response of KeywordAutoRespondersApi->create_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeywordAutoRespondersApi->create_auto_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_auto_responder_create_params** | [**WTAutoResponderCreateParams**](WTAutoResponderCreateParams.md)|  | 

### Return type

[**WTAutoResponder**](WTAutoResponder.md)

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
**422** | Validation Failed. A refused keyword names the rule it broke in the failing field&#39;s message: reserved-compliance-keyword, opt-out-phrase, date-shaped, help-desk-keyword, opt-in-list-keyword (with a listID field), duplicate (with an existingID field), empty, too-long, or empty-response (on responseBody). |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_auto_responders**
> List[WTAutoResponder] fetch_all_auto_responders(phone_number_id=phone_number_id, is_archive_included=is_archive_included)

List keyword auto-responders

### Example


```python
import wallet
from wallet.models.wt_auto_responder import WTAutoResponder
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
    api_instance = wallet.KeywordAutoRespondersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # List keyword auto-responders
        api_response = api_instance.fetch_all_auto_responders(phone_number_id=phone_number_id, is_archive_included=is_archive_included)
        print("The response of KeywordAutoRespondersApi->fetch_all_auto_responders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeywordAutoRespondersApi->fetch_all_auto_responders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTAutoResponder]**](WTAutoResponder.md)

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
**422** | Validation Failed. A refused keyword names the rule it broke in the failing field&#39;s message: reserved-compliance-keyword, opt-out-phrase, date-shaped, help-desk-keyword, opt-in-list-keyword (with a listID field), duplicate (with an existingID field), empty, too-long, or empty-response (on responseBody). |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_auto_responder_hits**
> List[WTAutoResponderHit] fetch_auto_responder_hits(auto_responder_id=auto_responder_id, limit=limit, offset=offset)

List keyword auto-responder activity

### Example


```python
import wallet
from wallet.models.wt_auto_responder_hit import WTAutoResponderHit
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
    api_instance = wallet.KeywordAutoRespondersApi(api_client)
    auto_responder_id = 'auto_responder_id_example' # str |  (optional)
    limit = 56 # int | Maximum number of records to return (optional)
    offset = 56 # int | Number of records to skip (optional)

    try:
        # List keyword auto-responder activity
        api_response = api_instance.fetch_auto_responder_hits(auto_responder_id=auto_responder_id, limit=limit, offset=offset)
        print("The response of KeywordAutoRespondersApi->fetch_auto_responder_hits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeywordAutoRespondersApi->fetch_auto_responder_hits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_responder_id** | **str**|  | [optional] 
 **limit** | **int**| Maximum number of records to return | [optional] 
 **offset** | **int**| Number of records to skip | [optional] 

### Return type

[**List[WTAutoResponderHit]**](WTAutoResponderHit.md)

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
**422** | Validation Failed. A refused keyword names the rule it broke in the failing field&#39;s message: reserved-compliance-keyword, opt-out-phrase, date-shaped, help-desk-keyword, opt-in-list-keyword (with a listID field), duplicate (with an existingID field), empty, too-long, or empty-response (on responseBody). |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_auto_responder**
> WTAutoResponder restore_auto_responder(auto_responder_id)

Restore a keyword auto-responder

### Example


```python
import wallet
from wallet.models.wt_auto_responder import WTAutoResponder
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
    api_instance = wallet.KeywordAutoRespondersApi(api_client)
    auto_responder_id = 'auto_responder_id_example' # str | 

    try:
        # Restore a keyword auto-responder
        api_response = api_instance.restore_auto_responder(auto_responder_id)
        print("The response of KeywordAutoRespondersApi->restore_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeywordAutoRespondersApi->restore_auto_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_responder_id** | **str**|  | 

### Return type

[**WTAutoResponder**](WTAutoResponder.md)

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
**422** | Validation Failed. A refused keyword names the rule it broke in the failing field&#39;s message: reserved-compliance-keyword, opt-out-phrase, date-shaped, help-desk-keyword, opt-in-list-keyword (with a listID field), duplicate (with an existingID field), empty, too-long, or empty-response (on responseBody). |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_responder**
> WTAutoResponder update_auto_responder(wt_auto_responder_update_params)

Update a keyword auto-responder

### Example


```python
import wallet
from wallet.models.wt_auto_responder import WTAutoResponder
from wallet.models.wt_auto_responder_update_params import WTAutoResponderUpdateParams
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
    api_instance = wallet.KeywordAutoRespondersApi(api_client)
    wt_auto_responder_update_params = wallet.WTAutoResponderUpdateParams() # WTAutoResponderUpdateParams | 

    try:
        # Update a keyword auto-responder
        api_response = api_instance.update_auto_responder(wt_auto_responder_update_params)
        print("The response of KeywordAutoRespondersApi->update_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeywordAutoRespondersApi->update_auto_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_auto_responder_update_params** | [**WTAutoResponderUpdateParams**](WTAutoResponderUpdateParams.md)|  | 

### Return type

[**WTAutoResponder**](WTAutoResponder.md)

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
**422** | Validation Failed. A refused keyword names the rule it broke in the failing field&#39;s message: reserved-compliance-keyword, opt-out-phrase, date-shaped, help-desk-keyword, opt-in-list-keyword (with a listID field), duplicate (with an existingID field), empty, too-long, or empty-response (on responseBody). |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

