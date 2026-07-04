# wallet.ImportExportApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_club_members**](ImportExportApi.md#export_club_members) | **PUT** /v2/employee/export/members | Export club members
[**export_merchant_credits**](ImportExportApi.md#export_merchant_credits) | **PUT** /v2/employee/export/merchantCredits | Export merchant credits
[**export_static_voucher_campaign**](ImportExportApi.md#export_static_voucher_campaign) | **PUT** /v2/employee/export/staticVoucherCampaign/{campaignID} | Export static voucher campaign
[**import_club_members**](ImportExportApi.md#import_club_members) | **POST** /v2/employee/import/members | Import club members
[**import_merchant_credits**](ImportExportApi.md#import_merchant_credits) | **POST** /v2/employee/import/merchantCredits | Import merchant credits
[**set_export_data_files_read**](ImportExportApi.md#set_export_data_files_read) | **PUT** /v2/employee/export/dataFiles | Mark export data files as read
[**update_club_members**](ImportExportApi.md#update_club_members) | **PUT** /v2/employee/update/members | Update club members


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
    api_instance = wallet.ImportExportApi(api_client)

    try:
        # Export club members
        api_response = api_instance.export_club_members()
        print("The response of ImportExportApi->export_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->export_club_members: %s\n" % e)
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
    api_instance = wallet.ImportExportApi(api_client)

    try:
        # Export merchant credits
        api_response = api_instance.export_merchant_credits()
        print("The response of ImportExportApi->export_merchant_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->export_merchant_credits: %s\n" % e)
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
    api_instance = wallet.ImportExportApi(api_client)
    campaign_id = 'campaign_id_example' # str | 

    try:
        # Export static voucher campaign
        api_response = api_instance.export_static_voucher_campaign(campaign_id)
        print("The response of ImportExportApi->export_static_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->export_static_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**|  | 

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
    api_instance = wallet.ImportExportApi(api_client)
    wt_employee_import_records = wallet.WTEmployeeImportRecords() # WTEmployeeImportRecords | 

    try:
        # Import club members
        api_response = api_instance.import_club_members(wt_employee_import_records)
        print("The response of ImportExportApi->import_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->import_club_members: %s\n" % e)
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
    api_instance = wallet.ImportExportApi(api_client)
    wt_employee_import_records = wallet.WTEmployeeImportRecords() # WTEmployeeImportRecords | 

    try:
        # Import merchant credits
        api_response = api_instance.import_merchant_credits(wt_employee_import_records)
        print("The response of ImportExportApi->import_merchant_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->import_merchant_credits: %s\n" % e)
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
    api_instance = wallet.ImportExportApi(api_client)

    try:
        # Mark export data files as read
        api_response = api_instance.set_export_data_files_read()
        print("The response of ImportExportApi->set_export_data_files_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->set_export_data_files_read: %s\n" % e)
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
    api_instance = wallet.ImportExportApi(api_client)
    wt_employee_update_records = wallet.WTEmployeeUpdateRecords() # WTEmployeeUpdateRecords | 

    try:
        # Update club members
        api_response = api_instance.update_club_members(wt_employee_update_records)
        print("The response of ImportExportApi->update_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportExportApi->update_club_members: %s\n" % e)
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

