# wallet.A2PApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**begin_a2_p_application**](A2PApi.md#begin_a2_p_application) | **POST** /v2/a2p/application | Create A2P Application
[**fetch_a2_p_application**](A2PApi.md#fetch_a2_p_application) | **GET** /v2/a2p/application | Fetch A2P Application
[**fetch_a2_p_registration**](A2PApi.md#fetch_a2_p_registration) | **GET** /v2/a2p/registration | Fetch A2P Registration
[**update_a2_p_application**](A2PApi.md#update_a2_p_application) | **PUT** /v2/a2p/application/{applicationID} | Update A2P Application


# **begin_a2_p_application**
> bool begin_a2_p_application(a2_p_application_submission)

Create A2P Application

### Example


```python
import time
import wallet
from wallet.api import a2_p_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.a2_p_application_submission import A2PApplicationSubmission
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = a2_p_api.A2PApi(api_client)
    a2_p_application_submission = A2PApplicationSubmission(
        is_twilio_terms_read=True,
        is_privacy_policy_on_website=True,
        is_tos_on_website=True,
        is_stop_understood=True,
        is_manual_read=True,
        is_ctia_short_code_read=True,
        is_standards_understood=True,
        is_short_code_understood=True,
        is_opt_in_out_understood=True,
        is_short_code_transfer_understood=True,
        is_pricing_understood=True,
        is_short_code_timeline_understood=True,
        business_name="Acme Corp",
        business_type=BusinessType("Partnership"),
        business_classification=BusinessClassification("public"),
        business_industry=BusinessIndustry("AUTOMOTIVE"),
        tax_id_type=BusinessRegistrationIdentifier("EIN"),
        tax_id="23-235235",
        website_url="https://google.com",
        social_media_url="https://instagram.com/your_business",
        regions_of_operation=[
            BusinessRegionsOfOperation("AFRICA"),
        ],
        stock_exchange=BusinessStockExchanges("NONE"),
        stock_ticker="stock_ticker_example",
        messaging_volume_high=True,
        address1="21 Jump Street",
        address2="https://google.com",
        city="Los Angeles",
        state="California",
        postal_code="90210",
        country="US",
        first_name="John",
        last_name="Doe",
        email="email_example",
        job_title="VP of Marketing",
        job_position=JobPosition("Director"),
        phone_number="+1 800 123 4567",
    ) # A2PApplicationSubmission | 

    # example passing only required values which don't have defaults set
    try:
        # Create A2P Application
        api_response = api_instance.begin_a2_p_application(a2_p_application_submission)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling A2PApi->begin_a2_p_application: %s\n" % e)
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

# **fetch_a2_p_application**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_a2_p_application()

Fetch A2P Application

### Example


```python
import time
import wallet
from wallet.api import a2_p_api
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
    api_instance = a2_p_api.A2PApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch A2P Application
        api_response = api_instance.fetch_a2_p_application()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling A2PApi->fetch_a2_p_application: %s\n" % e)
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

# **fetch_a2_p_registration**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_a2_p_registration()

Fetch A2P Registration

### Example


```python
import time
import wallet
from wallet.api import a2_p_api
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
    api_instance = a2_p_api.A2PApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch A2P Registration
        api_response = api_instance.fetch_a2_p_registration()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling A2PApi->fetch_a2_p_registration: %s\n" % e)
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

# **update_a2_p_application**
> bool update_a2_p_application(application_id, wta2_p_application_update_params)

Update A2P Application

### Example


```python
import time
import wallet
from wallet.api import a2_p_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wta2_p_application_update_params import WTA2PApplicationUpdateParams
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
    api_instance = a2_p_api.A2PApi(api_client)
    application_id = NanoID("C") # NanoID | 
    wta2_p_application_update_params = WTA2PApplicationUpdateParams(
        business_name="Acme Corp",
        business_type=BusinessType("Partnership"),
        business_classification=BusinessClassification("public"),
        business_industry=BusinessIndustry("AUTOMOTIVE"),
        tax_id_type=BusinessRegistrationIdentifier("EIN"),
        tax_id="23-235235",
        website_url="https://google.com",
        social_media_url="https://instagram.com/your_business",
        regions_of_operation=[
            BusinessRegionsOfOperation("AFRICA"),
        ],
        stock_exchange=BusinessStockExchanges("NONE"),
        stock_ticker="stock_ticker_example",
        messaging_volume_high=True,
        address1="21 Jump Street",
        address2="https://google.com",
        city="Los Angeles",
        state="California",
        postal_code="90210",
        country="US",
        first_name="John",
        last_name="Doe",
        email="email_example",
        job_title="VP of Marketing",
        job_position=JobPosition("Director"),
        phone_number="+1 800 123 4567",
    ) # WTA2PApplicationUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update A2P Application
        api_response = api_instance.update_a2_p_application(application_id, wta2_p_application_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling A2PApi->update_a2_p_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **NanoID**|  |
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

