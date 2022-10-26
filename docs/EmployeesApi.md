# wallet.EmployeesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_peer_to_roles**](EmployeesApi.md#add_peer_to_roles) | **POST** /v2/employee/roles/peer/{userID} | Add peer to roles
[**create_alert**](EmployeesApi.md#create_alert) | **POST** /v2/employee/alert | Create employee alert
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
[**fetch_merchant**](EmployeesApi.md#fetch_merchant) | **GET** /v2/employee/merchant | Fetch merchant information
[**fetch_messages**](EmployeesApi.md#fetch_messages) | **GET** /v2/employee/messages/all | Fetch all messages
[**fetch_opt_in_list_source**](EmployeesApi.md#fetch_opt_in_list_source) | **GET** /v2/employee/optInListSource/{sourceID} | Fetch opt in list source
[**fetch_opt_in_list_sources_created_by_employee**](EmployeesApi.md#fetch_opt_in_list_sources_created_by_employee) | **GET** /v2/employee/optInListSources/all | Fetch all opt in list sources
[**fetch_peer_activity**](EmployeesApi.md#fetch_peer_activity) | **GET** /v2/employee/peer/activity/{employeeID} | Fetch peer activity
[**fetch_peers_permissions**](EmployeesApi.md#fetch_peers_permissions) | **GET** /v2/employee/peer/permissions/{userID} | Fetch peer permissions
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
[**update_employee_peer**](EmployeesApi.md#update_employee_peer) | **PUT** /v2/employee/peer/{userID} | Update peer


# **add_peer_to_roles**
> str add_peer_to_roles(user_id, wt_employee_peer_roles)

Add peer to roles

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_peer_roles import WTEmployeePeerRoles
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
    api_instance = employees_api.EmployeesApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_employee_peer_roles = WTEmployeePeerRoles(
        roles_array=[
            None,
        ],
    ) # WTEmployeePeerRoles | 

    # example passing only required values which don't have defaults set
    try:
        # Add peer to roles
        api_response = api_instance.add_peer_to_roles(user_id, wt_employee_peer_roles)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->add_peer_to_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

# **create_alert**
> Alert create_alert(wt_employee_create_alert)

Create employee alert

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_create_alert import WTEmployeeCreateAlert
from wallet.model.auth_error import AuthError
from wallet.model.alert import Alert
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_create_alert = WTEmployeeCreateAlert(
        title="Alert Title",
        message="Alert Content",
    ) # WTEmployeeCreateAlert | 

    # example passing only required values which don't have defaults set
    try:
        # Create employee alert
        api_response = api_instance.create_alert(wt_employee_create_alert)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->create_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_create_alert** | [**WTEmployeeCreateAlert**](WTEmployeeCreateAlert.md)|  |

### Return type

[**Alert**](Alert.md)

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_create_document import WTEmployeeCreateDocument
from wallet.model.document import Document
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_create_document = WTEmployeeCreateDocument(
        file_name="document.pdf",
        file_data=None,
        folder="folder_example",
    ) # WTEmployeeCreateDocument | 

    # example passing only required values which don't have defaults set
    try:
        # Create document
        api_response = api_instance.create_document(wt_employee_create_document)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.wt_employee_create import WTEmployeeCreate
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.employee import Employee
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_create = WTEmployeeCreate(
        first_name="John",
        last_name="Doe",
        email="email_example",
        phone_number="+1809898765",
        is_public_representative=True,
        wallet_sequence_number=1,
        employee_id="EMP005",
        job_title="Marketing Executive",
        department="Sales & Marketing",
    ) # WTEmployeeCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create employee peer
        api_response = api_instance.create_employee_peer(wt_employee_create)
        pprint(api_response)
    except wallet.ApiException as e:
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
> InlineResponse2001 create_file(wt_employee_file_create)

Create file

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_file_create import WTEmployeeFileCreate
from wallet.model.inline_response2001 import InlineResponse2001
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_file_create = WTEmployeeFileCreate(
        file_name="club-members-upload.csv",
        file_data="file_data_example",
    ) # WTEmployeeFileCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create file
        api_response = api_instance.create_file(wt_employee_file_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_file_create** | [**WTEmployeeFileCreate**](WTEmployeeFileCreate.md)|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.media_file import MediaFile
from wallet.model.wt_employee_create_media_file import WTEmployeeCreateMediaFile
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_create_media_file = WTEmployeeCreateMediaFile(
        file_name="picture.jpeg",
        file_data=None,
        folder="folder_example",
    ) # WTEmployeeCreateMediaFile | 

    # example passing only required values which don't have defaults set
    try:
        # Create media file
        api_response = api_instance.create_media_file(wt_employee_create_media_file)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.wt_employee_create_static_voucher_campaign_group import WTEmployeeCreateStaticVoucherCampaignGroup
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.static_voucher_campaign_group import StaticVoucherCampaignGroup
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_create_static_voucher_campaign_group = WTEmployeeCreateStaticVoucherCampaignGroup(
        name="Christmas Static Voucher Campaign Group",
    ) # WTEmployeeCreateStaticVoucherCampaignGroup | 

    # example passing only required values which don't have defaults set
    try:
        # Create static voucher campaign group
        api_response = api_instance.create_static_voucher_campaigns_group(wt_employee_create_static_voucher_campaign_group)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.document import Document
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
    api_instance = employees_api.EmployeesApi(api_client)
    document_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Delete document
        api_response = api_instance.delete_document(document_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->delete_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.media_file import MediaFile
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    media_file_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Delete media file
        api_response = api_instance.delete_media_file(media_file_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->delete_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_file_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)
    file_id = "fileID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch URL for file download
        api_response = api_instance.download_file(file_id)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export club members
        api_response = api_instance.export_club_members()
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export merchant credits
        api_response = api_instance.export_merchant_credits()
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Export static voucher campaign
        api_response = api_instance.export_static_voucher_campaign(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->export_static_voucher_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)
    file_id = "fileID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch URL to download a failed import
        api_response = api_instance.failed_import(file_id)
        pprint(api_response)
    except wallet.ApiException as e:
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
> [Document] fetch_documents()

Fetch all documents

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.document import Document
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
    api_instance = employees_api.EmployeesApi(api_client)
    folder = "folder_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all documents
        api_response = api_instance.fetch_documents(folder=folder)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional]

### Return type

[**[Document]**](Document.md)

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
> [DynamicVoucher] fetch_dynamic_vouchers()

Fetch all dynamic vouchers

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.dynamic_voucher import DynamicVoucher
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all dynamic vouchers
        api_response = api_instance.fetch_dynamic_vouchers(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_dynamic_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[DynamicVoucher]**](DynamicVoucher.md)

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
> [StaticVoucherCampaignGroup] fetch_employee_static_voucher_campaign_groups()

Fetch static voucher campaign groups

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.static_voucher_campaign_group import StaticVoucherCampaignGroup
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch static voucher campaign groups
        api_response = api_instance.fetch_employee_static_voucher_campaign_groups()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_employee_static_voucher_campaign_groups: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[StaticVoucherCampaignGroup]**](StaticVoucherCampaignGroup.md)

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
> [StaticVoucherCampaign] fetch_employee_static_voucher_campaigns()

Fetch static voucher campaigns

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher_campaign import StaticVoucherCampaign
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
    api_instance = employees_api.EmployeesApi(api_client)
    is_archive_included = True # bool |  (optional)
    source_id = 3.14 # float |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch static voucher campaigns
        api_response = api_instance.fetch_employee_static_voucher_campaigns(is_archive_included=is_archive_included, source_id=source_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_employee_static_voucher_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]
 **source_id** | **float**|  | [optional]

### Return type

[**[StaticVoucherCampaign]**](StaticVoucherCampaign.md)

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
> [MediaFile] fetch_media_files()

Fetch all media files

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.media_file import MediaFile
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    folder = "folder_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all media files
        api_response = api_instance.fetch_media_files(folder=folder)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_media_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional]

### Return type

[**[MediaFile]**](MediaFile.md)

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
> bool, date, datetime, dict, float, int, list, str, none_type fetch_merchant()

Fetch merchant information

### Example


```python
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch merchant information
        api_response = api_instance.fetch_merchant()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_merchant: %s\n" % e)
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

# **fetch_messages**
> [Message] fetch_messages()

Fetch all messages

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.message import Message
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all messages
        api_response = api_instance.fetch_messages()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_messages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Message]**](Message.md)

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.opt_in_list_source import OptInListSource
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
    api_instance = employees_api.EmployeesApi(api_client)
    source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch opt in list source
        api_response = api_instance.fetch_opt_in_list_source(source_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_opt_in_list_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> [OptInListSource] fetch_opt_in_list_sources_created_by_employee()

Fetch all opt in list sources

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.opt_in_list_source import OptInListSource
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all opt in list sources
        api_response = api_instance.fetch_opt_in_list_sources_created_by_employee()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_opt_in_list_sources_created_by_employee: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **fetch_peer_activity**
> [EmployeeActivityLog] fetch_peer_activity(employee_id)

Fetch peer activity

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.employee_activity_log import EmployeeActivityLog
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    employee_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch peer activity
        api_response = api_instance.fetch_peer_activity(employee_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_peer_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[EmployeeActivityLog]**](EmployeeActivityLog.md)

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
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_peers_permissions(user_id)

Fetch peer permissions

### Example


```python
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch peer permissions
        api_response = api_instance.fetch_peers_permissions(user_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->fetch_peers_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_import_records = WTEmployeeImportRecords(
        file_name="club-members-upload.csv",
        bucket="members",
    ) # WTEmployeeImportRecords | 

    # example passing only required values which don't have defaults set
    try:
        # Import club members
        api_response = api_instance.import_club_members(wt_employee_import_records)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_import_records = WTEmployeeImportRecords(
        file_name="club-members-upload.csv",
        bucket="members",
    ) # WTEmployeeImportRecords | 

    # example passing only required values which don't have defaults set
    try:
        # Import merchant credits
        api_response = api_instance.import_merchant_credits(wt_employee_import_records)
        pprint(api_response)
    except wallet.ApiException as e:
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
> [Webpage] load_webpages_of_employee()

Retrieve employee's webpages

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.webpage import Webpage
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve employee's webpages
        api_response = api_instance.load_webpages_of_employee()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->load_webpages_of_employee: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Webpage]**](Webpage.md)

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
> [bool, date, datetime, dict, float, int, list, str, none_type] modify_peers_roles(user_id, wt_employee_peer_roles)

Modify peer's roles

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_peer_roles import WTEmployeePeerRoles
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
    api_instance = employees_api.EmployeesApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_employee_peer_roles = WTEmployeePeerRoles(
        roles_array=[
            None,
        ],
    ) # WTEmployeePeerRoles | 

    # example passing only required values which don't have defaults set
    try:
        # Modify peer's roles
        api_response = api_instance.modify_peers_roles(user_id, wt_employee_peer_roles)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->modify_peers_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_employee_peer_roles** | [**WTEmployeePeerRoles**](WTEmployeePeerRoles.md)|  |

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.presigned_post import PresignedPost
from wallet.model.wt_employee_s3_file_presign import WTEmployeeS3FilePresign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_s3_file_presign = WTEmployeeS3FilePresign(
        file_name="club-members-upload.csv",
        file_type="csv",
        context=None,
    ) # WTEmployeeS3FilePresign | 

    # example passing only required values which don't have defaults set
    try:
        # Presign file for upload
        api_response = api_instance.presign_file(wt_employee_s3_file_presign)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Remove peer from all roles
        api_response = api_instance.remove_peer_from_all_roles(user_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->remove_peer_from_all_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.entity_too_large import EntityTooLarge
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_schedule_simple_sms import WTEmployeeScheduleSimpleSMS
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
    api_instance = employees_api.EmployeesApi(api_client)
    advertisement_credit_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_employee_schedule_simple_sms = WTEmployeeScheduleSimpleSMS(
        phone_number_id=NanoID("C"),
        message_template="We're running a year end promo of flat 50% off!",
        media_urls=["https://example.com/media.jpeg"],
        broadcast_scheduled_at=dateutil_parser('2022-08-17T18:42:50.713Z'),
        list_type=None,
        list_id=NanoID("C"),
    ) # WTEmployeeScheduleSimpleSMS | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule Ad Credit
        api_response = api_instance.schedule_advertisement_credit(advertisement_credit_id, wt_employee_schedule_simple_sms)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->schedule_advertisement_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisement_credit_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.entity_too_large import EntityTooLarge
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_schedule_simple_sms import WTEmployeeScheduleSimpleSMS
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
    api_instance = employees_api.EmployeesApi(api_client)
    dynamic_voucher_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_employee_schedule_simple_sms = WTEmployeeScheduleSimpleSMS(
        phone_number_id=NanoID("C"),
        message_template="We're running a year end promo of flat 50% off!",
        media_urls=["https://example.com/media.jpeg"],
        broadcast_scheduled_at=dateutil_parser('2022-08-17T18:42:50.713Z'),
        list_type=None,
        list_id=NanoID("C"),
    ) # WTEmployeeScheduleSimpleSMS | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule Dynamic Voucher to list
        api_response = api_instance.schedule_dynamic_voucher(dynamic_voucher_id, wt_employee_schedule_simple_sms)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->schedule_dynamic_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.entity_too_large import EntityTooLarge
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_employee_schedule_simple_smsto_recipient import WTEmployeeScheduleSimpleSMSToRecipient
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
    api_instance = employees_api.EmployeesApi(api_client)
    dynamic_voucher_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_employee_schedule_simple_smsto_recipient = WTEmployeeScheduleSimpleSMSToRecipient(
        phone_number_id=NanoID("C"),
        message_template="We're running a year end promo of flat 50% off!",
        media_urls=["https://example.com/media.jpeg"],
        broadcast_scheduled_at=dateutil_parser('2022-08-17T18:42:50.713Z'),
        to_cell_phone="+1809898989",
    ) # WTEmployeeScheduleSimpleSMSToRecipient | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule Dyanamic Voucher to recipient
        api_response = api_instance.schedule_dynamic_voucher_to_recipient(dynamic_voucher_id, wt_employee_schedule_simple_smsto_recipient)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->schedule_dynamic_voucher_to_recipient: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
> SimpleSMSBroadcast schedule_simple_sms(wt_employee_schedule_simple_sms)

Schedule Simple SMS broadcast to list

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.simple_sms_broadcast import SimpleSMSBroadcast
from wallet.model.entity_too_large import EntityTooLarge
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_schedule_simple_sms import WTEmployeeScheduleSimpleSMS
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_schedule_simple_sms = WTEmployeeScheduleSimpleSMS(
        phone_number_id=NanoID("C"),
        message_template="We're running a year end promo of flat 50% off!",
        media_urls=["https://example.com/media.jpeg"],
        broadcast_scheduled_at=dateutil_parser('2022-08-17T18:42:50.713Z'),
        list_type=None,
        list_id=NanoID("C"),
    ) # WTEmployeeScheduleSimpleSMS | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule Simple SMS broadcast to list
        api_response = api_instance.schedule_simple_sms(wt_employee_schedule_simple_sms)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->schedule_simple_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_schedule_simple_sms** | [**WTEmployeeScheduleSimpleSMS**](WTEmployeeScheduleSimpleSMS.md)|  |

### Return type

[**SimpleSMSBroadcast**](SimpleSMSBroadcast.md)

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
> SimpleSMSBroadcast schedule_simple_smsto_recipient(wt_employee_schedule_simple_smsto_recipient)

Schedule Simple SMS broadcast to recipient

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.simple_sms_broadcast import SimpleSMSBroadcast
from wallet.model.entity_too_large import EntityTooLarge
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_employee_schedule_simple_smsto_recipient import WTEmployeeScheduleSimpleSMSToRecipient
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_schedule_simple_smsto_recipient = WTEmployeeScheduleSimpleSMSToRecipient(
        phone_number_id=NanoID("C"),
        message_template="We're running a year end promo of flat 50% off!",
        media_urls=["https://example.com/media.jpeg"],
        broadcast_scheduled_at=dateutil_parser('2022-08-17T18:42:50.713Z'),
        to_cell_phone="+1809898989",
    ) # WTEmployeeScheduleSimpleSMSToRecipient | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule Simple SMS broadcast to recipient
        api_response = api_instance.schedule_simple_smsto_recipient(wt_employee_schedule_simple_smsto_recipient)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->schedule_simple_smsto_recipient: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_schedule_simple_smsto_recipient** | [**WTEmployeeScheduleSimpleSMSToRecipient**](WTEmployeeScheduleSimpleSMSToRecipient.md)|  |

### Return type

[**SimpleSMSBroadcast**](SimpleSMSBroadcast.md)

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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_send_help_desk_response import WTEmployeeSendHelpDeskResponse
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_send_help_desk_response = WTEmployeeSendHelpDeskResponse(
        help_desk_request_id=NanoID("C"),
        message="Good morning! How can I help you today?",
        media_urls=["https://example.com/media.jpeg"],
    ) # WTEmployeeSendHelpDeskResponse | 

    # example passing only required values which don't have defaults set
    try:
        # Send help desk response
        api_response = api_instance.send_help_desk_response(wt_employee_send_help_desk_response)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.wt_employee_schedule_sms_campaign_broadcast import WTEmployeeScheduleSMSCampaignBroadcast
from wallet.model.entity_too_large import EntityTooLarge
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
    api_instance = employees_api.EmployeesApi(api_client)
    static_voucher_campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_employee_schedule_sms_campaign_broadcast = WTEmployeeScheduleSMSCampaignBroadcast(
        phone_number_id=NanoID("C"),
        message_template="Here's your link to your voucher: [link]",
        send_qr_code=True,
        media_urls=["https://example.com/media.jpeg"],
        broadcast_scheduled_at=dateutil_parser('2022-08-17T18:42:50.713Z'),
        locale="en-US",
        timezone="America/New_York",
    ) # WTEmployeeScheduleSMSCampaignBroadcast | 

    # example passing only required values which don't have defaults set
    try:
        # Schedule SMS Campaign Broadcast
        api_response = api_instance.send_sms_campaign_broadcast(static_voucher_campaign_id, wt_employee_schedule_sms_campaign_broadcast)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->send_sms_campaign_broadcast: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher_campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Mark alerts as read
        api_response = api_instance.set_alerts_read()
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Mark export data files as read
        api_response = api_instance.set_export_data_files_read()
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)
    help_desk_request_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Resolve help desk request
        api_response = api_instance.set_help_desk_request_resolved(help_desk_request_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->set_help_desk_request_resolved: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **help_desk_request_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import employees_api
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
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Mark messages as read
        api_response = api_instance.set_messages_read()
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_employee_create_media_file import WTEmployeeCreateMediaFile
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_create_media_file = WTEmployeeCreateMediaFile(
        file_name="picture.jpeg",
        file_data=None,
        folder="folder_example",
    ) # WTEmployeeCreateMediaFile | 

    # example passing only required values which don't have defaults set
    try:
        # Set profile picture
        api_response = api_instance.set_profile_picture(wt_employee_create_media_file)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_update_records import WTEmployeeUpdateRecords
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
    api_instance = employees_api.EmployeesApi(api_client)
    wt_employee_update_records = WTEmployeeUpdateRecords(
        file_name="club-members-upload.csv",
        bucket="members",
    ) # WTEmployeeUpdateRecords | 

    # example passing only required values which don't have defaults set
    try:
        # Update club members
        api_response = api_instance.update_club_members(wt_employee_update_records)
        pprint(api_response)
    except wallet.ApiException as e:
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

# **update_employee_peer**
> Employee update_employee_peer(user_id, wt_employee_update)

Update peer

### Example


```python
import time
import wallet
from wallet.api import employees_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_update import WTEmployeeUpdate
from wallet.model.employee import Employee
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
    api_instance = employees_api.EmployeesApi(api_client)
    user_id = NanoID("C") # NanoID | 
    wt_employee_update = WTEmployeeUpdate(
        employee_id="EMP005",
        first_name="John",
        last_name="Doe",
        phone_number="+1809898765",
        is_public_representative=True,
        wallet_sequence_number=1,
        job_title="Marketing Executive",
        department="Sales & Marketing",
    ) # WTEmployeeUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update peer
        api_response = api_instance.update_employee_peer(user_id, wt_employee_update)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeesApi->update_employee_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **NanoID**|  |
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

