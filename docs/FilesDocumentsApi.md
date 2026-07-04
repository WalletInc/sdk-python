# wallet.FilesDocumentsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](FilesDocumentsApi.md#create_document) | **POST** /v2/employee/document | Create document
[**create_file**](FilesDocumentsApi.md#create_file) | **POST** /v2/employee/file/create | Create file
[**create_media_file**](FilesDocumentsApi.md#create_media_file) | **POST** /v2/employee/mediaFile | Create media file
[**delete_document**](FilesDocumentsApi.md#delete_document) | **DELETE** /v2/employee/document/{documentID} | Delete document
[**delete_media_file**](FilesDocumentsApi.md#delete_media_file) | **DELETE** /v2/employee/mediaFile/{mediaFileID} | Delete media file
[**download_file**](FilesDocumentsApi.md#download_file) | **GET** /v2/employee/file/download/{fileID} | Get URL for file download
[**failed_import**](FilesDocumentsApi.md#failed_import) | **GET** /v2/employee/file/imports/failed/{fileID} | Get URL to download a failed import
[**fetch_documents**](FilesDocumentsApi.md#fetch_documents) | **GET** /v2/employee/documents/all | Get all documents
[**fetch_media_files**](FilesDocumentsApi.md#fetch_media_files) | **GET** /v2/employee/mediaFiles/all | Get all media files
[**presign_file**](FilesDocumentsApi.md#presign_file) | **POST** /v2/employee/file/presign | Presign file for upload


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
    api_instance = wallet.FilesDocumentsApi(api_client)
    wt_employee_create_document = wallet.WTEmployeeCreateDocument() # WTEmployeeCreateDocument | 

    try:
        # Create document
        api_response = api_instance.create_document(wt_employee_create_document)
        print("The response of FilesDocumentsApi->create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->create_document: %s\n" % e)
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
    api_instance = wallet.FilesDocumentsApi(api_client)
    wt_employee_file_create = wallet.WTEmployeeFileCreate() # WTEmployeeFileCreate | 

    try:
        # Create file
        api_response = api_instance.create_file(wt_employee_file_create)
        print("The response of FilesDocumentsApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->create_file: %s\n" % e)
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
    api_instance = wallet.FilesDocumentsApi(api_client)
    wt_employee_create_media_file = wallet.WTEmployeeCreateMediaFile() # WTEmployeeCreateMediaFile | 

    try:
        # Create media file
        api_response = api_instance.create_media_file(wt_employee_create_media_file)
        print("The response of FilesDocumentsApi->create_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->create_media_file: %s\n" % e)
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
    api_instance = wallet.FilesDocumentsApi(api_client)
    document_id = 'document_id_example' # str | 

    try:
        # Delete document
        api_response = api_instance.delete_document(document_id)
        print("The response of FilesDocumentsApi->delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 

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
    api_instance = wallet.FilesDocumentsApi(api_client)
    media_file_id = 'media_file_id_example' # str | 

    try:
        # Delete media file
        api_response = api_instance.delete_media_file(media_file_id)
        print("The response of FilesDocumentsApi->delete_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->delete_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_file_id** | **str**|  | 

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

Get URL for file download

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
    api_instance = wallet.FilesDocumentsApi(api_client)
    file_id = 'file_id_example' # str | 

    try:
        # Get URL for file download
        api_response = api_instance.download_file(file_id)
        print("The response of FilesDocumentsApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->download_file: %s\n" % e)
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

# **failed_import**
> str failed_import(file_id)

Get URL to download a failed import

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
    api_instance = wallet.FilesDocumentsApi(api_client)
    file_id = 'file_id_example' # str | 

    try:
        # Get URL to download a failed import
        api_response = api_instance.failed_import(file_id)
        print("The response of FilesDocumentsApi->failed_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->failed_import: %s\n" % e)
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

Get all documents

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
    api_instance = wallet.FilesDocumentsApi(api_client)
    folder = 'folder_example' # str |  (optional)

    try:
        # Get all documents
        api_response = api_instance.fetch_documents(folder=folder)
        print("The response of FilesDocumentsApi->fetch_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->fetch_documents: %s\n" % e)
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

# **fetch_media_files**
> List[MediaFile] fetch_media_files(folder=folder)

Get all media files

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
    api_instance = wallet.FilesDocumentsApi(api_client)
    folder = 'folder_example' # str |  (optional)

    try:
        # Get all media files
        api_response = api_instance.fetch_media_files(folder=folder)
        print("The response of FilesDocumentsApi->fetch_media_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->fetch_media_files: %s\n" % e)
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
    api_instance = wallet.FilesDocumentsApi(api_client)
    wt_employee_s3_file_presign = wallet.WTEmployeeS3FilePresign() # WTEmployeeS3FilePresign | 

    try:
        # Presign file for upload
        api_response = api_instance.presign_file(wt_employee_s3_file_presign)
        print("The response of FilesDocumentsApi->presign_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesDocumentsApi->presign_file: %s\n" % e)
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

