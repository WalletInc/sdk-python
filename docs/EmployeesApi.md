# wallet.EmployeesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_peer_to_roles**](EmployeesApi.md#add_peer_to_roles) | **POST** /v2/employee/roles/peer/{userID} | Add peer to roles
[**create_document**](EmployeesApi.md#create_document) | **POST** /v2/employee/document | Create document
[**create_employee_peer**](EmployeesApi.md#create_employee_peer) | **POST** /v2/employee/peer | Create employee peer
[**create_file**](EmployeesApi.md#create_file) | **POST** /v2/employee/file/create | Create file
[**create_media_file**](EmployeesApi.md#create_media_file) | **POST** /v2/employee/mediaFile | Create media file
[**create_static_voucher_campaigns_group**](EmployeesApi.md#create_static_voucher_campaigns_group) | **POST** /v2/employee/staticVoucherCampaignsGroup | Create static voucher campaign group
[**delete_document**](EmployeesApi.md#delete_document) | **DELETE** /v2/employee/document/{documentID} | Delete document
[**delete_media_file**](EmployeesApi.md#delete_media_file) | **DELETE** /v2/employee/mediaFile/{mediaFileID} | Delete media file
[**download_file**](EmployeesApi.md#download_file) | **GET** /v2/employee/file/download/{fileID} | Fetch URL for file download
[**export_club_members**](EmployeesApi.md#export_club_members) | **PUT** /v2/employee/export/members | Export club members
[**export_merchant_credits**](EmployeesApi.md#export_merchant_credits) | **PUT** /v2/employee/export/merchantCredits | Export merchant credits
[**export_static_voucher_campaign**](EmployeesApi.md#export_static_voucher_campaign) | **PUT** /v2/employee/export/staticVoucherCampaign/{campaignID} | Export static voucher campaign
[**failed_import**](EmployeesApi.md#failed_import) | **GET** /v2/employee/file/imports/failed/{fileID} | Fetch URL to download a failed import
[**fetch_documents**](EmployeesApi.md#fetch_documents) | **GET** /v2/employee/documents/all | Fetch all documents
[**fetch_dynamic_vouchers**](EmployeesApi.md#fetch_dynamic_vouchers) | **GET** /v2/employee/dynamicVouchers/all | Fetch all dynamic vouchers
[**fetch_employee_static_voucher_campaign_groups**](EmployeesApi.md#fetch_employee_static_voucher_campaign_groups) | **GET** /v2/employee/staticVoucherCampaignGroups/all | Fetch static voucher campaign groups
[**fetch_employee_static_voucher_campaigns**](EmployeesApi.md#fetch_employee_static_voucher_campaigns) | **GET** /v2/employee/staticVoucherCampaigns/all | Fetch static voucher campaigns
[**fetch_media_files**](EmployeesApi.md#fetch_media_files) | **GET** /v2/employee/mediaFiles/all | Fetch all media files
[**fetch_merchant**](EmployeesApi.md#fetch_merchant) | **GET** /v2/employee/merchant | Create employee alert
[**fetch_messages**](EmployeesApi.md#fetch_messages) | **GET** /v2/employee/messages/all | Fetch all messages
[**fetch_opt_in_list_source**](EmployeesApi.md#fetch_opt_in_list_source) | **GET** /v2/employee/optInListSource/{sourceID} | Fetch opt in list source
[**fetch_opt_in_list_sources_created_by_employee**](EmployeesApi.md#fetch_opt_in_list_sources_created_by_employee) | **GET** /v2/employee/optInListSources/all | Fetch all opt in list sources
[**fetch_peer_activity**](EmployeesApi.md#fetch_peer_activity) | **GET** /v2/employee/peer/activity/{employeeID} | Fetch peer activity
[**fetch_peers_permissions**](EmployeesApi.md#fetch_peers_permissions) | **GET** /v2/employee/peer/permissions/{userID} | Fetch peer permissions
[**fetch_profile_info**](EmployeesApi.md#fetch_profile_info) | **GET** /v2/employee | Retrieve employee&#39;s webpages
[**import_club_members**](EmployeesApi.md#import_club_members) | **POST** /v2/employee/import/members | Import club members
[**import_merchant_credits**](EmployeesApi.md#import_merchant_credits) | **POST** /v2/employee/import/merchantCredits | Import merchant credits
[**load_webpages_of_employee**](EmployeesApi.md#load_webpages_of_employee) | **GET** /v2/employee/webpages/all | Retrieve employee&#39;s webpages
[**modify_peers_roles**](EmployeesApi.md#modify_peers_roles) | **PUT** /v2/employee/peer/permissions/{userID} | Modify peer&#39;s roles
[**presign_file**](EmployeesApi.md#presign_file) | **POST** /v2/employee/file/presign | Presign file for upload
[**remove_peer_from_all_roles**](EmployeesApi.md#remove_peer_from_all_roles) | **DELETE** /v2/employee/peer/permissions/{userID} | Remove peer from all roles
[**schedule_advertisement_credit**](EmployeesApi.md#schedule_advertisement_credit) | **POST** /v2/employee/sms/schedule/adCredit/{advertisementCreditID} | Schedule Ad Credit
[**schedule_dynamic_voucher**](EmployeesApi.md#schedule_dynamic_voucher) | **POST** /v2/employee/sms/schedule/dynamicVoucher/{dynamicVoucherID} | Schedule Dynamic Voucher to list
[**schedule_dynamic_voucher_to_recipient**](EmployeesApi.md#schedule_dynamic_voucher_to_recipient) | **POST** /v2/employee/sms/schedule/recipient/dynamicVoucher/{dynamicVoucherID} | Schedule Dyanamic Voucher to recipient
[**schedule_simple_sms**](EmployeesApi.md#schedule_simple_sms) | **POST** /v2/employee/sms/schedule/simple | Schedule Simple SMS broadcast to list
[**schedule_simple_smsto_recipient**](EmployeesApi.md#schedule_simple_smsto_recipient) | **POST** /v2/employee/sms/schedule/recipient/simple | Schedule Simple SMS broadcast to recipient
[**send_help_desk_response**](EmployeesApi.md#send_help_desk_response) | **POST** /v2/employee/helpDesk/response | Send help desk response
[**send_sms_campaign_broadcast**](EmployeesApi.md#send_sms_campaign_broadcast) | **POST** /v2/employee/sms/schedule/campaign/{staticVoucherCampaignID} | Schedule SMS Campaign Broadcast
[**set_alerts_read**](EmployeesApi.md#set_alerts_read) | **PATCH** /v2/employee/alerts | Mark alerts as read
[**set_export_data_files_read**](EmployeesApi.md#set_export_data_files_read) | **PUT** /v2/employee/export/dataFiles | Mark export data files as read
[**set_help_desk_request_resolved**](EmployeesApi.md#set_help_desk_request_resolved) | **PATCH** /v2/employee/helpDesk/request/{helpDeskRequestID} | Resolve help desk request
[**set_messages_read**](EmployeesApi.md#set_messages_read) | **PATCH** /v2/employee/messages | Mark messages as read
[**set_profile_picture**](EmployeesApi.md#set_profile_picture) | **PUT** /v2/employee/profile/picture | Set profile picture
[**update_club_members**](EmployeesApi.md#update_club_members) | **PUT** /v2/employee/update/members | Update club members
[**update_email_notification_preference**](EmployeesApi.md#update_email_notification_preference) | **PUT** /v2/employee/emailNotificationPreference | Changes the employee&#39;s email notification preference to enabled or disabled
[**update_employee_peer**](EmployeesApi.md#update_employee_peer) | **PUT** /v2/employee/peer/{userID} | Update peer


# **add_peer_to_roles**
> str add_peer_to_roles(user_id, wt_employee_peer_roles)

Add peer to roles

### Example


```python
import wallet
from wallet.models.wt_employee_peer_roles import WTEmployeePeerRoles
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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = None # object | 
    wt_employee_peer_roles = wallet.WTEmployeePeerRoles() # WTEmployeePeerRoles | 

    try:
        # Add peer to roles
        api_response = api_instance.add_peer_to_roles(user_id, wt_employee_peer_roles)
        print("The response of EmployeesApi->add_peer_to_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->add_peer_to_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 
 **wt_employee_peer_roles** | [**WTEmployeePeerRoles**](WTEmployeePeerRoles.md)|  | 

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

# **create_document**
> Document create_document(wt_employee_create_document)

Create document

### Example


```python
import wallet
from wallet.models.document import Document
from wallet.models.wt_employee_create_document import WTEmployeeCreateDocument
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_create_document = wallet.WTEmployeeCreateDocument() # WTEmployeeCreateDocument | 

    try:
        # Create document
        api_response = api_instance.create_document(wt_employee_create_document)
        print("The response of EmployeesApi->create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create_document** | [**WTEmployeeCreateDocument**](WTEmployeeCreateDocument.md)|  | 

### Return type

[**Document**](Document.md)

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

# **create_employee_peer**
> Employee create_employee_peer(wt_employee_create)

Create employee peer

### Example


```python
import wallet
from wallet.models.employee import Employee
from wallet.models.wt_employee_create import WTEmployeeCreate
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_create = wallet.WTEmployeeCreate() # WTEmployeeCreate | 

    try:
        # Create employee peer
        api_response = api_instance.create_employee_peer(wt_employee_create)
        print("The response of EmployeesApi->create_employee_peer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_employee_peer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create** | [**WTEmployeeCreate**](WTEmployeeCreate.md)|  | 

### Return type

[**Employee**](Employee.md)

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

# **create_file**
> CreateFile200Response create_file(wt_employee_file_create)

Create file

### Example


```python
import wallet
from wallet.models.create_file200_response import CreateFile200Response
from wallet.models.wt_employee_file_create import WTEmployeeFileCreate
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_file_create = wallet.WTEmployeeFileCreate() # WTEmployeeFileCreate | 

    try:
        # Create file
        api_response = api_instance.create_file(wt_employee_file_create)
        print("The response of EmployeesApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_file_create** | [**WTEmployeeFileCreate**](WTEmployeeFileCreate.md)|  | 

### Return type

[**CreateFile200Response**](CreateFile200Response.md)

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

# **create_media_file**
> MediaFile create_media_file(wt_employee_create_media_file)

Create media file

### Example


```python
import wallet
from wallet.models.media_file import MediaFile
from wallet.models.wt_employee_create_media_file import WTEmployeeCreateMediaFile
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_create_media_file = wallet.WTEmployeeCreateMediaFile() # WTEmployeeCreateMediaFile | 

    try:
        # Create media file
        api_response = api_instance.create_media_file(wt_employee_create_media_file)
        print("The response of EmployeesApi->create_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create_media_file** | [**WTEmployeeCreateMediaFile**](WTEmployeeCreateMediaFile.md)|  | 

### Return type

[**MediaFile**](MediaFile.md)

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

# **create_static_voucher_campaigns_group**
> StaticVoucherCampaignGroup create_static_voucher_campaigns_group(wt_employee_create_static_voucher_campaign_group)

Create static voucher campaign group

### Example


```python
import wallet
from wallet.models.static_voucher_campaign_group import StaticVoucherCampaignGroup
from wallet.models.wt_employee_create_static_voucher_campaign_group import WTEmployeeCreateStaticVoucherCampaignGroup
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_create_static_voucher_campaign_group = wallet.WTEmployeeCreateStaticVoucherCampaignGroup() # WTEmployeeCreateStaticVoucherCampaignGroup | 

    try:
        # Create static voucher campaign group
        api_response = api_instance.create_static_voucher_campaigns_group(wt_employee_create_static_voucher_campaign_group)
        print("The response of EmployeesApi->create_static_voucher_campaigns_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_static_voucher_campaigns_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create_static_voucher_campaign_group** | [**WTEmployeeCreateStaticVoucherCampaignGroup**](WTEmployeeCreateStaticVoucherCampaignGroup.md)|  | 

### Return type

[**StaticVoucherCampaignGroup**](StaticVoucherCampaignGroup.md)

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

# **delete_document**
> Document delete_document(document_id)

Delete document

### Example


```python
import wallet
from wallet.models.document import Document
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
    api_instance = wallet.EmployeesApi(api_client)
    document_id = None # object | 

    try:
        # Delete document
        api_response = api_instance.delete_document(document_id)
        print("The response of EmployeesApi->delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | [**object**](.md)|  | 

### Return type

[**Document**](Document.md)

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

# **delete_media_file**
> MediaFile delete_media_file(media_file_id)

Delete media file

### Example


```python
import wallet
from wallet.models.media_file import MediaFile
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
    api_instance = wallet.EmployeesApi(api_client)
    media_file_id = None # object | 

    try:
        # Delete media file
        api_response = api_instance.delete_media_file(media_file_id)
        print("The response of EmployeesApi->delete_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->delete_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_file_id** | [**object**](.md)|  | 

### Return type

[**MediaFile**](MediaFile.md)

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

# **download_file**
> str download_file(file_id)

Fetch URL for file download

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
    api_instance = wallet.EmployeesApi(api_client)
    file_id = 'file_id_example' # str | 

    try:
        # Fetch URL for file download
        api_response = api_instance.download_file(file_id)
        print("The response of EmployeesApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 

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

# **export_club_members**
> str export_club_members()

Export club members

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Export club members
        api_response = api_instance.export_club_members()
        print("The response of EmployeesApi->export_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->export_club_members: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **export_merchant_credits**
> str export_merchant_credits()

Export merchant credits

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Export merchant credits
        api_response = api_instance.export_merchant_credits()
        print("The response of EmployeesApi->export_merchant_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->export_merchant_credits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **export_static_voucher_campaign**
> str export_static_voucher_campaign(campaign_id)

Export static voucher campaign

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
    api_instance = wallet.EmployeesApi(api_client)
    campaign_id = None # object | 

    try:
        # Export static voucher campaign
        api_response = api_instance.export_static_voucher_campaign(campaign_id)
        print("The response of EmployeesApi->export_static_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->export_static_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

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

# **failed_import**
> str failed_import(file_id)

Fetch URL to download a failed import

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
    api_instance = wallet.EmployeesApi(api_client)
    file_id = 'file_id_example' # str | 

    try:
        # Fetch URL to download a failed import
        api_response = api_instance.failed_import(file_id)
        print("The response of EmployeesApi->failed_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->failed_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 

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

# **fetch_documents**
> List[Document] fetch_documents(folder=folder)

Fetch all documents

### Example


```python
import wallet
from wallet.models.document import Document
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
    api_instance = wallet.EmployeesApi(api_client)
    folder = 'folder_example' # str |  (optional)

    try:
        # Fetch all documents
        api_response = api_instance.fetch_documents(folder=folder)
        print("The response of EmployeesApi->fetch_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional] 

### Return type

[**List[Document]**](Document.md)

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

# **fetch_dynamic_vouchers**
> List[DynamicVoucher] fetch_dynamic_vouchers(is_archive_included=is_archive_included)

Fetch all dynamic vouchers

### Example


```python
import wallet
from wallet.models.dynamic_voucher import DynamicVoucher
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
    api_instance = wallet.EmployeesApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all dynamic vouchers
        api_response = api_instance.fetch_dynamic_vouchers(is_archive_included=is_archive_included)
        print("The response of EmployeesApi->fetch_dynamic_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_dynamic_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[DynamicVoucher]**](DynamicVoucher.md)

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

# **fetch_employee_static_voucher_campaign_groups**
> List[StaticVoucherCampaignGroup] fetch_employee_static_voucher_campaign_groups()

Fetch static voucher campaign groups

### Example


```python
import wallet
from wallet.models.static_voucher_campaign_group import StaticVoucherCampaignGroup
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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Fetch static voucher campaign groups
        api_response = api_instance.fetch_employee_static_voucher_campaign_groups()
        print("The response of EmployeesApi->fetch_employee_static_voucher_campaign_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_employee_static_voucher_campaign_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StaticVoucherCampaignGroup]**](StaticVoucherCampaignGroup.md)

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

# **fetch_employee_static_voucher_campaigns**
> List[StaticVoucherCampaign] fetch_employee_static_voucher_campaigns(is_archive_included=is_archive_included, source_id=source_id)

Fetch static voucher campaigns

### Example


```python
import wallet
from wallet.models.static_voucher_campaign import StaticVoucherCampaign
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
    api_instance = wallet.EmployeesApi(api_client)
    is_archive_included = True # bool |  (optional)
    source_id = 3.4 # float |  (optional)

    try:
        # Fetch static voucher campaigns
        api_response = api_instance.fetch_employee_static_voucher_campaigns(is_archive_included=is_archive_included, source_id=source_id)
        print("The response of EmployeesApi->fetch_employee_static_voucher_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_employee_static_voucher_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 
 **source_id** | **float**|  | [optional] 

### Return type

[**List[StaticVoucherCampaign]**](StaticVoucherCampaign.md)

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

# **fetch_media_files**
> List[MediaFile] fetch_media_files(folder=folder)

Fetch all media files

### Example


```python
import wallet
from wallet.models.media_file import MediaFile
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
    api_instance = wallet.EmployeesApi(api_client)
    folder = 'folder_example' # str |  (optional)

    try:
        # Fetch all media files
        api_response = api_instance.fetch_media_files(folder=folder)
        print("The response of EmployeesApi->fetch_media_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_media_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional] 

### Return type

[**List[MediaFile]**](MediaFile.md)

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

# **fetch_merchant**
> object fetch_merchant()

Create employee alert

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Create employee alert
        api_response = api_instance.fetch_merchant()
        print("The response of EmployeesApi->fetch_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_merchant: %s\n" % e)
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

# **fetch_messages**
> List[Message] fetch_messages()

Fetch all messages

### Example


```python
import wallet
from wallet.models.message import Message
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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Fetch all messages
        api_response = api_instance.fetch_messages()
        print("The response of EmployeesApi->fetch_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_messages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Message]**](Message.md)

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

# **fetch_opt_in_list_source**
> OptInListSource fetch_opt_in_list_source(source_id)

Fetch opt in list source

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
    api_instance = wallet.EmployeesApi(api_client)
    source_id = None # object | 

    try:
        # Fetch opt in list source
        api_response = api_instance.fetch_opt_in_list_source(source_id)
        print("The response of EmployeesApi->fetch_opt_in_list_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_opt_in_list_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | [**object**](.md)|  | 

### Return type

[**OptInListSource**](OptInListSource.md)

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

# **fetch_opt_in_list_sources_created_by_employee**
> List[OptInListSource] fetch_opt_in_list_sources_created_by_employee()

Fetch all opt in list sources

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Fetch all opt in list sources
        api_response = api_instance.fetch_opt_in_list_sources_created_by_employee()
        print("The response of EmployeesApi->fetch_opt_in_list_sources_created_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_opt_in_list_sources_created_by_employee: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **fetch_peer_activity**
> List[EmployeeActivityLog] fetch_peer_activity(employee_id)

Fetch peer activity

### Example


```python
import wallet
from wallet.models.employee_activity_log import EmployeeActivityLog
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
    api_instance = wallet.EmployeesApi(api_client)
    employee_id = None # object | 

    try:
        # Fetch peer activity
        api_response = api_instance.fetch_peer_activity(employee_id)
        print("The response of EmployeesApi->fetch_peer_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_peer_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**object**](.md)|  | 

### Return type

[**List[EmployeeActivityLog]**](EmployeeActivityLog.md)

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

# **fetch_peers_permissions**
> List[object] fetch_peers_permissions(user_id)

Fetch peer permissions

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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = None # object | 

    try:
        # Fetch peer permissions
        api_response = api_instance.fetch_peers_permissions(user_id)
        print("The response of EmployeesApi->fetch_peers_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_peers_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 

### Return type

**List[object]**

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

# **fetch_profile_info**
> Employee fetch_profile_info()

Retrieve employee's webpages

### Example


```python
import wallet
from wallet.models.employee import Employee
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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Retrieve employee's webpages
        api_response = api_instance.fetch_profile_info()
        print("The response of EmployeesApi->fetch_profile_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->fetch_profile_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Employee**](Employee.md)

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

# **import_club_members**
> str import_club_members(wt_employee_import_records)

Import club members

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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_import_records = wallet.WTEmployeeImportRecords() # WTEmployeeImportRecords | 

    try:
        # Import club members
        api_response = api_instance.import_club_members(wt_employee_import_records)
        print("The response of EmployeesApi->import_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->import_club_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **import_merchant_credits**
> str import_merchant_credits(wt_employee_import_records)

Import merchant credits

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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_import_records = wallet.WTEmployeeImportRecords() # WTEmployeeImportRecords | 

    try:
        # Import merchant credits
        api_response = api_instance.import_merchant_credits(wt_employee_import_records)
        print("The response of EmployeesApi->import_merchant_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->import_merchant_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **load_webpages_of_employee**
> List[Webpage] load_webpages_of_employee()

Retrieve employee's webpages

### Example


```python
import wallet
from wallet.models.webpage import Webpage
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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Retrieve employee's webpages
        api_response = api_instance.load_webpages_of_employee()
        print("The response of EmployeesApi->load_webpages_of_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->load_webpages_of_employee: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Webpage]**](Webpage.md)

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

# **modify_peers_roles**
> List[object] modify_peers_roles(user_id, wt_employee_peer_roles)

Modify peer's roles

### Example


```python
import wallet
from wallet.models.wt_employee_peer_roles import WTEmployeePeerRoles
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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = None # object | 
    wt_employee_peer_roles = wallet.WTEmployeePeerRoles() # WTEmployeePeerRoles | 

    try:
        # Modify peer's roles
        api_response = api_instance.modify_peers_roles(user_id, wt_employee_peer_roles)
        print("The response of EmployeesApi->modify_peers_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->modify_peers_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 
 **wt_employee_peer_roles** | [**WTEmployeePeerRoles**](WTEmployeePeerRoles.md)|  | 

### Return type

**List[object]**

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

# **presign_file**
> PresignedPost presign_file(wt_employee_s3_file_presign)

Presign file for upload

### Example


```python
import wallet
from wallet.models.presigned_post import PresignedPost
from wallet.models.wt_employee_s3_file_presign import WTEmployeeS3FilePresign
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_s3_file_presign = wallet.WTEmployeeS3FilePresign() # WTEmployeeS3FilePresign | 

    try:
        # Presign file for upload
        api_response = api_instance.presign_file(wt_employee_s3_file_presign)
        print("The response of EmployeesApi->presign_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->presign_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_s3_file_presign** | [**WTEmployeeS3FilePresign**](WTEmployeeS3FilePresign.md)|  | 

### Return type

[**PresignedPost**](PresignedPost.md)

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

# **remove_peer_from_all_roles**
> bool remove_peer_from_all_roles(user_id)

Remove peer from all roles

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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = None # object | 

    try:
        # Remove peer from all roles
        api_response = api_instance.remove_peer_from_all_roles(user_id)
        print("The response of EmployeesApi->remove_peer_from_all_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->remove_peer_from_all_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 

### Return type

**bool**

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
    api_instance = wallet.EmployeesApi(api_client)
    advertisement_credit_id = None # object | 
    wt_employee_schedule_simple_sms = wallet.WTEmployeeScheduleSimpleSMS() # WTEmployeeScheduleSimpleSMS | 

    try:
        # Schedule Ad Credit
        api_response = api_instance.schedule_advertisement_credit(advertisement_credit_id, wt_employee_schedule_simple_sms)
        print("The response of EmployeesApi->schedule_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->schedule_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisement_credit_id** | [**object**](.md)|  | 
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
    api_instance = wallet.EmployeesApi(api_client)
    dynamic_voucher_id = None # object | 
    wt_employee_schedule_simple_sms = wallet.WTEmployeeScheduleSimpleSMS() # WTEmployeeScheduleSimpleSMS | 

    try:
        # Schedule Dynamic Voucher to list
        api_response = api_instance.schedule_dynamic_voucher(dynamic_voucher_id, wt_employee_schedule_simple_sms)
        print("The response of EmployeesApi->schedule_dynamic_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->schedule_dynamic_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | [**object**](.md)|  | 
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

Schedule Dyanamic Voucher to recipient

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
    api_instance = wallet.EmployeesApi(api_client)
    dynamic_voucher_id = None # object | 
    wt_employee_schedule_simple_smsto_recipient = wallet.WTEmployeeScheduleSimpleSMSToRecipient() # WTEmployeeScheduleSimpleSMSToRecipient | 

    try:
        # Schedule Dyanamic Voucher to recipient
        api_response = api_instance.schedule_dynamic_voucher_to_recipient(dynamic_voucher_id, wt_employee_schedule_simple_smsto_recipient)
        print("The response of EmployeesApi->schedule_dynamic_voucher_to_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->schedule_dynamic_voucher_to_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | [**object**](.md)|  | 
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_schedule_simple_sms = wallet.WTEmployeeScheduleSimpleSMS() # WTEmployeeScheduleSimpleSMS | 

    try:
        # Schedule Simple SMS broadcast to list
        api_response = api_instance.schedule_simple_sms(wt_employee_schedule_simple_sms)
        print("The response of EmployeesApi->schedule_simple_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->schedule_simple_sms: %s\n" % e)
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_schedule_simple_smsto_recipient = wallet.WTEmployeeScheduleSimpleSMSToRecipient() # WTEmployeeScheduleSimpleSMSToRecipient | 

    try:
        # Schedule Simple SMS broadcast to recipient
        api_response = api_instance.schedule_simple_smsto_recipient(wt_employee_schedule_simple_smsto_recipient)
        print("The response of EmployeesApi->schedule_simple_smsto_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->schedule_simple_smsto_recipient: %s\n" % e)
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

# **send_help_desk_response**
> OutboundSMS send_help_desk_response(wt_employee_send_help_desk_response)

Send help desk response

### Example


```python
import wallet
from wallet.models.outbound_sms import OutboundSMS
from wallet.models.wt_employee_send_help_desk_response import WTEmployeeSendHelpDeskResponse
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_send_help_desk_response = wallet.WTEmployeeSendHelpDeskResponse() # WTEmployeeSendHelpDeskResponse | 

    try:
        # Send help desk response
        api_response = api_instance.send_help_desk_response(wt_employee_send_help_desk_response)
        print("The response of EmployeesApi->send_help_desk_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->send_help_desk_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_send_help_desk_response** | [**WTEmployeeSendHelpDeskResponse**](WTEmployeeSendHelpDeskResponse.md)|  | 

### Return type

[**OutboundSMS**](OutboundSMS.md)

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
    api_instance = wallet.EmployeesApi(api_client)
    static_voucher_campaign_id = None # object | 
    wt_employee_schedule_sms_campaign_broadcast = wallet.WTEmployeeScheduleSMSCampaignBroadcast() # WTEmployeeScheduleSMSCampaignBroadcast | 

    try:
        # Schedule SMS Campaign Broadcast
        api_response = api_instance.send_sms_campaign_broadcast(static_voucher_campaign_id, wt_employee_schedule_sms_campaign_broadcast)
        print("The response of EmployeesApi->send_sms_campaign_broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->send_sms_campaign_broadcast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher_campaign_id** | [**object**](.md)|  | 
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

# **set_alerts_read**
> bool set_alerts_read()

Mark alerts as read

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Mark alerts as read
        api_response = api_instance.set_alerts_read()
        print("The response of EmployeesApi->set_alerts_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_alerts_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

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

# **set_export_data_files_read**
> bool set_export_data_files_read()

Mark export data files as read

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Mark export data files as read
        api_response = api_instance.set_export_data_files_read()
        print("The response of EmployeesApi->set_export_data_files_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_export_data_files_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

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

# **set_help_desk_request_resolved**
> HelpDeskRequest set_help_desk_request_resolved(help_desk_request_id)

Resolve help desk request

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
    api_instance = wallet.EmployeesApi(api_client)
    help_desk_request_id = None # object | 

    try:
        # Resolve help desk request
        api_response = api_instance.set_help_desk_request_resolved(help_desk_request_id)
        print("The response of EmployeesApi->set_help_desk_request_resolved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_help_desk_request_resolved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **help_desk_request_id** | [**object**](.md)|  | 

### Return type

[**HelpDeskRequest**](HelpDeskRequest.md)

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

# **set_messages_read**
> bool set_messages_read()

Mark messages as read

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
    api_instance = wallet.EmployeesApi(api_client)

    try:
        # Mark messages as read
        api_response = api_instance.set_messages_read()
        print("The response of EmployeesApi->set_messages_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_messages_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

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

# **set_profile_picture**
> str set_profile_picture(wt_employee_create_media_file)

Set profile picture

### Example


```python
import wallet
from wallet.models.wt_employee_create_media_file import WTEmployeeCreateMediaFile
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_create_media_file = wallet.WTEmployeeCreateMediaFile() # WTEmployeeCreateMediaFile | 

    try:
        # Set profile picture
        api_response = api_instance.set_profile_picture(wt_employee_create_media_file)
        print("The response of EmployeesApi->set_profile_picture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->set_profile_picture: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create_media_file** | [**WTEmployeeCreateMediaFile**](WTEmployeeCreateMediaFile.md)|  | 

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

# **update_club_members**
> str update_club_members(wt_employee_update_records)

Update club members

### Example


```python
import wallet
from wallet.models.wt_employee_update_records import WTEmployeeUpdateRecords
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
    api_instance = wallet.EmployeesApi(api_client)
    wt_employee_update_records = wallet.WTEmployeeUpdateRecords() # WTEmployeeUpdateRecords | 

    try:
        # Update club members
        api_response = api_instance.update_club_members(wt_employee_update_records)
        print("The response of EmployeesApi->update_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->update_club_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_update_records** | [**WTEmployeeUpdateRecords**](WTEmployeeUpdateRecords.md)|  | 

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

# **update_email_notification_preference**
> Employee update_email_notification_preference(update_email_notification_preference_request)

Changes the employee's email notification preference to enabled or disabled

### Example


```python
import wallet
from wallet.models.employee import Employee
from wallet.models.update_email_notification_preference_request import UpdateEmailNotificationPreferenceRequest
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
    api_instance = wallet.EmployeesApi(api_client)
    update_email_notification_preference_request = wallet.UpdateEmailNotificationPreferenceRequest() # UpdateEmailNotificationPreferenceRequest | 

    try:
        # Changes the employee's email notification preference to enabled or disabled
        api_response = api_instance.update_email_notification_preference(update_email_notification_preference_request)
        print("The response of EmployeesApi->update_email_notification_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->update_email_notification_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_email_notification_preference_request** | [**UpdateEmailNotificationPreferenceRequest**](UpdateEmailNotificationPreferenceRequest.md)|  | 

### Return type

[**Employee**](Employee.md)

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

# **update_employee_peer**
> Employee update_employee_peer(user_id, wt_employee_update)

Update peer

### Example


```python
import wallet
from wallet.models.employee import Employee
from wallet.models.wt_employee_update import WTEmployeeUpdate
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
    api_instance = wallet.EmployeesApi(api_client)
    user_id = 'user_id_example' # str | 
    wt_employee_update = wallet.WTEmployeeUpdate() # WTEmployeeUpdate | 

    try:
        # Update peer
        api_response = api_instance.update_employee_peer(user_id, wt_employee_update)
        print("The response of EmployeesApi->update_employee_peer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->update_employee_peer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **wt_employee_update** | [**WTEmployeeUpdate**](WTEmployeeUpdate.md)|  | 

### Return type

[**Employee**](Employee.md)

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

