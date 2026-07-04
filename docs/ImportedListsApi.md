# wallet.ImportedListsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_recipient**](ImportedListsApi.md#archive_recipient) | **DELETE** /v2/sms/importedList/recipients/{id} | Archive recipient
[**count_imported_list_recipients**](ImportedListsApi.md#count_imported_list_recipients) | **GET** /v2/sms/importedList/recipients/count/{listID} | Count imported list recipients
[**create_imported_list**](ImportedListsApi.md#create_imported_list) | **POST** /v2/sms/importedList | Create imported list
[**create_recipient_in_imported_list**](ImportedListsApi.md#create_recipient_in_imported_list) | **POST** /v2/sms/importedList/recipients/create | Add new recipient in an imported list
[**export_imported_list_recipients**](ImportedListsApi.md#export_imported_list_recipients) | **POST** /v2/sms/importedList/recipients/export/{importedListID} | Export imported list recipients
[**fetch_imported_list**](ImportedListsApi.md#fetch_imported_list) | **GET** /v2/merchant/lists/imported/{listID} | Get imported list
[**fetch_imported_list_recipients**](ImportedListsApi.md#fetch_imported_list_recipients) | **GET** /v2/sms/importedList/recipients/{listID} | Get imported list recipients
[**fetch_imported_list_recipients_by_page**](ImportedListsApi.md#fetch_imported_list_recipients_by_page) | **GET** /v2/sms/importedList/recipients/page/{listID} | Get imported list recipients by page
[**fetch_imported_lists**](ImportedListsApi.md#fetch_imported_lists) | **GET** /v2/merchant/lists/imported/all | Get all imported lists
[**import_imported_list_recipients**](ImportedListsApi.md#import_imported_list_recipients) | **POST** /v2/sms/importedList/recipients/import/{importedListID} | Import imported list recipients
[**import_imported_list_recipients_from_membership_tier**](ImportedListsApi.md#import_imported_list_recipients_from_membership_tier) | **POST** /v2/sms/importedList/recipients/import-from-tier | Import imported list recipients from a given membership tier
[**restore_recipient**](ImportedListsApi.md#restore_recipient) | **PATCH** /v2/sms/importedList/recipients/{id} | Restore recipient
[**save_imported_list**](ImportedListsApi.md#save_imported_list) | **PUT** /v2/sms/importedList/{listID} | Save imported list


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
    api_instance = wallet.ImportedListsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive recipient
        api_response = api_instance.archive_recipient(id)
        print("The response of ImportedListsApi->archive_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->archive_recipient: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    list_id = 'list_id_example' # str | 
    is_archive_included = True # bool |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count imported list recipients
        api_response = api_instance.count_imported_list_recipients(list_id, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        print("The response of ImportedListsApi->count_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->count_imported_list_recipients: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    wtsms_imported_list_create = wallet.WTSMSImportedListCreate() # WTSMSImportedListCreate | 

    try:
        # Create imported list
        api_response = api_instance.create_imported_list(wtsms_imported_list_create)
        print("The response of ImportedListsApi->create_imported_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->create_imported_list: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    ss_imported_list_recipient_create_params = wallet.SSImportedListRecipientCreateParams() # SSImportedListRecipientCreateParams | 

    try:
        # Add new recipient in an imported list
        api_response = api_instance.create_recipient_in_imported_list(ss_imported_list_recipient_create_params)
        print("The response of ImportedListsApi->create_recipient_in_imported_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->create_recipient_in_imported_list: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    imported_list_id = 'imported_list_id_example' # str | 

    try:
        # Export imported list recipients
        api_response = api_instance.export_imported_list_recipients(imported_list_id)
        print("The response of ImportedListsApi->export_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->export_imported_list_recipients: %s\n" % e)
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

# **fetch_imported_list**
> ImportedList fetch_imported_list(list_id)

Get imported list

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
    api_instance = wallet.ImportedListsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Get imported list
        api_response = api_instance.fetch_imported_list(list_id)
        print("The response of ImportedListsApi->fetch_imported_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->fetch_imported_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

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

# **fetch_imported_list_recipients**
> List[ImportedListRecipient] fetch_imported_list_recipients(list_id)

Get imported list recipients

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
    api_instance = wallet.ImportedListsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Get imported list recipients
        api_response = api_instance.fetch_imported_list_recipients(list_id)
        print("The response of ImportedListsApi->fetch_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->fetch_imported_list_recipients: %s\n" % e)
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

Get imported list recipients by page

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
    api_instance = wallet.ImportedListsApi(api_client)
    list_id = 'list_id_example' # str | 
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Get imported list recipients by page
        api_response = api_instance.fetch_imported_list_recipients_by_page(list_id, page_size=page_size, page_num=page_num, is_archive_included=is_archive_included)
        print("The response of ImportedListsApi->fetch_imported_list_recipients_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->fetch_imported_list_recipients_by_page: %s\n" % e)
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

# **fetch_imported_lists**
> object fetch_imported_lists(is_archive_included=is_archive_included)

Get all imported lists

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
    api_instance = wallet.ImportedListsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all imported lists
        api_response = api_instance.fetch_imported_lists(is_archive_included=is_archive_included)
        print("The response of ImportedListsApi->fetch_imported_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->fetch_imported_lists: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    imported_list_id = 'imported_list_id_example' # str | 
    wt_employee_import_records = wallet.WTEmployeeImportRecords() # WTEmployeeImportRecords | 

    try:
        # Import imported list recipients
        api_response = api_instance.import_imported_list_recipients(imported_list_id, wt_employee_import_records)
        print("The response of ImportedListsApi->import_imported_list_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->import_imported_list_recipients: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    wt_imported_list_recipient_from_membership_tier_import = wallet.WTImportedListRecipientFromMembershipTierImport() # WTImportedListRecipientFromMembershipTierImport | 

    try:
        # Import imported list recipients from a given membership tier
        api_response = api_instance.import_imported_list_recipients_from_membership_tier(wt_imported_list_recipient_from_membership_tier_import)
        print("The response of ImportedListsApi->import_imported_list_recipients_from_membership_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->import_imported_list_recipients_from_membership_tier: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore recipient
        api_response = api_instance.restore_recipient(id)
        print("The response of ImportedListsApi->restore_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->restore_recipient: %s\n" % e)
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
    api_instance = wallet.ImportedListsApi(api_client)
    list_id = 'list_id_example' # str | 
    wtsms_imported_list_create = wallet.WTSMSImportedListCreate() # WTSMSImportedListCreate | 

    try:
        # Save imported list
        api_response = api_instance.save_imported_list(list_id, wtsms_imported_list_create)
        print("The response of ImportedListsApi->save_imported_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportedListsApi->save_imported_list: %s\n" % e)
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

