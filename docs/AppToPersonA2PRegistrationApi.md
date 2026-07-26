# wallet.AppToPersonA2PRegistrationApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**begin_a2_p_application**](AppToPersonA2PRegistrationApi.md#begin_a2_p_application) | **POST** /v2/a2p/application | Create A2P Application
[**begin_a2_p_application_government**](AppToPersonA2PRegistrationApi.md#begin_a2_p_application_government) | **POST** /a2p/application/government | Begin A2P Application (Government)
[**begin_a2_p_application_non_profit**](AppToPersonA2PRegistrationApi.md#begin_a2_p_application_non_profit) | **POST** /a2p/application/nonprofit | Begin A2P Application (Non-profit)
[**begin_a2_p_application_public**](AppToPersonA2PRegistrationApi.md#begin_a2_p_application_public) | **POST** /a2p/application/public | Begin A2P Application (Public: a publicly-traded company; requires stock exchange, ticker, and brand contact email)
[**begin_a2_p_application_sole_proprietor**](AppToPersonA2PRegistrationApi.md#begin_a2_p_application_sole_proprietor) | **POST** /a2p/application/sole-proprietor | Begin A2P Application (Sole Proprietor: no EIN; requires a mobile number for OTP verification)
[**begin_a2_p_application_standard**](AppToPersonA2PRegistrationApi.md#begin_a2_p_application_standard) | **POST** /a2p/application/standard | Begin A2P Application (Standard: a private, for-profit business with an EIN)
[**fetch_a2_p_application**](AppToPersonA2PRegistrationApi.md#fetch_a2_p_application) | **GET** /v2/a2p/application | Get A2P Application
[**fetch_a2_p_registration**](AppToPersonA2PRegistrationApi.md#fetch_a2_p_registration) | **GET** /v2/a2p/registration | Get A2P Registration
[**update_a2_p_application**](AppToPersonA2PRegistrationApi.md#update_a2_p_application) | **PUT** /v2/a2p/application/{applicationID} | Update A2P Application


# **begin_a2_p_application**
> bool begin_a2_p_application(a2_p_application_submission)

Create A2P Application

### Example


```python
import wallet
from wallet.models.a2_p_application_submission import A2PApplicationSubmission
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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)
    a2_p_application_submission = wallet.A2PApplicationSubmission() # A2PApplicationSubmission | 

    try:
        # Create A2P Application
        api_response = api_instance.begin_a2_p_application(a2_p_application_submission)
        print("The response of AppToPersonA2PRegistrationApi->begin_a2_p_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->begin_a2_p_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a2_p_application_submission** | [**A2PApplicationSubmission**](A2PApplicationSubmission.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_a2_p_application_government**
> bool begin_a2_p_application_government(a2_p_government_submission)

Begin A2P Application (Government)

### Example


```python
import wallet
from wallet.models.a2_p_government_submission import A2PGovernmentSubmission
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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)
    a2_p_government_submission = wallet.A2PGovernmentSubmission() # A2PGovernmentSubmission | 

    try:
        # Begin A2P Application (Government)
        api_response = api_instance.begin_a2_p_application_government(a2_p_government_submission)
        print("The response of AppToPersonA2PRegistrationApi->begin_a2_p_application_government:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->begin_a2_p_application_government: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a2_p_government_submission** | [**A2PGovernmentSubmission**](A2PGovernmentSubmission.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_a2_p_application_non_profit**
> bool begin_a2_p_application_non_profit(a2_p_non_profit_submission)

Begin A2P Application (Non-profit)

### Example


```python
import wallet
from wallet.models.a2_p_non_profit_submission import A2PNonProfitSubmission
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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)
    a2_p_non_profit_submission = wallet.A2PNonProfitSubmission() # A2PNonProfitSubmission | 

    try:
        # Begin A2P Application (Non-profit)
        api_response = api_instance.begin_a2_p_application_non_profit(a2_p_non_profit_submission)
        print("The response of AppToPersonA2PRegistrationApi->begin_a2_p_application_non_profit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->begin_a2_p_application_non_profit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a2_p_non_profit_submission** | [**A2PNonProfitSubmission**](A2PNonProfitSubmission.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_a2_p_application_public**
> bool begin_a2_p_application_public(a2_p_public_submission)

Begin A2P Application (Public: a publicly-traded company; requires stock exchange, ticker, and brand contact email)

### Example


```python
import wallet
from wallet.models.a2_p_public_submission import A2PPublicSubmission
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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)
    a2_p_public_submission = wallet.A2PPublicSubmission() # A2PPublicSubmission | 

    try:
        # Begin A2P Application (Public: a publicly-traded company; requires stock exchange, ticker, and brand contact email)
        api_response = api_instance.begin_a2_p_application_public(a2_p_public_submission)
        print("The response of AppToPersonA2PRegistrationApi->begin_a2_p_application_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->begin_a2_p_application_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a2_p_public_submission** | [**A2PPublicSubmission**](A2PPublicSubmission.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_a2_p_application_sole_proprietor**
> bool begin_a2_p_application_sole_proprietor(a2_p_sole_proprietor_submission)

Begin A2P Application (Sole Proprietor: no EIN; requires a mobile number for OTP verification)

### Example


```python
import wallet
from wallet.models.a2_p_sole_proprietor_submission import A2PSoleProprietorSubmission
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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)
    a2_p_sole_proprietor_submission = wallet.A2PSoleProprietorSubmission() # A2PSoleProprietorSubmission | 

    try:
        # Begin A2P Application (Sole Proprietor: no EIN; requires a mobile number for OTP verification)
        api_response = api_instance.begin_a2_p_application_sole_proprietor(a2_p_sole_proprietor_submission)
        print("The response of AppToPersonA2PRegistrationApi->begin_a2_p_application_sole_proprietor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->begin_a2_p_application_sole_proprietor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a2_p_sole_proprietor_submission** | [**A2PSoleProprietorSubmission**](A2PSoleProprietorSubmission.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_a2_p_application_standard**
> bool begin_a2_p_application_standard(a2_p_standard_submission)

Begin A2P Application (Standard: a private, for-profit business with an EIN)

### Example


```python
import wallet
from wallet.models.a2_p_standard_submission import A2PStandardSubmission
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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)
    a2_p_standard_submission = wallet.A2PStandardSubmission() # A2PStandardSubmission | 

    try:
        # Begin A2P Application (Standard: a private, for-profit business with an EIN)
        api_response = api_instance.begin_a2_p_application_standard(a2_p_standard_submission)
        print("The response of AppToPersonA2PRegistrationApi->begin_a2_p_application_standard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->begin_a2_p_application_standard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a2_p_standard_submission** | [**A2PStandardSubmission**](A2PStandardSubmission.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_a2_p_application**
> object fetch_a2_p_application()

Get A2P Application

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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)

    try:
        # Get A2P Application
        api_response = api_instance.fetch_a2_p_application()
        print("The response of AppToPersonA2PRegistrationApi->fetch_a2_p_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->fetch_a2_p_application: %s\n" % e)
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

# **fetch_a2_p_registration**
> object fetch_a2_p_registration()

Get A2P Registration

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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)

    try:
        # Get A2P Registration
        api_response = api_instance.fetch_a2_p_registration()
        print("The response of AppToPersonA2PRegistrationApi->fetch_a2_p_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->fetch_a2_p_registration: %s\n" % e)
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

# **update_a2_p_application**
> bool update_a2_p_application(application_id, wta2_p_application_update_params)

Update A2P Application

### Example


```python
import wallet
from wallet.models.wta2_p_application_update_params import WTA2PApplicationUpdateParams
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
    api_instance = wallet.AppToPersonA2PRegistrationApi(api_client)
    application_id = 'application_id_example' # str | 
    wta2_p_application_update_params = wallet.WTA2PApplicationUpdateParams() # WTA2PApplicationUpdateParams | 

    try:
        # Update A2P Application
        api_response = api_instance.update_a2_p_application(application_id, wta2_p_application_update_params)
        print("The response of AppToPersonA2PRegistrationApi->update_a2_p_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppToPersonA2PRegistrationApi->update_a2_p_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **wta2_p_application_update_params** | [**WTA2PApplicationUpdateParams**](WTA2PApplicationUpdateParams.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

