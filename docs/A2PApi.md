# wallet.A2PApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a2_p_application**](A2PApi.md#create_a2_p_application) | **POST** /v2/a2p/application | Create A2P Application
[**create_a2_p_registration**](A2PApi.md#create_a2_p_registration) | **POST** /v2/a2p/registration | Create A2P Registration
[**fetch_a2_p_application**](A2PApi.md#fetch_a2_p_application) | **GET** /v2/a2p/application | Fetch A2P Application
[**fetch_a2_p_registration**](A2PApi.md#fetch_a2_p_registration) | **GET** /v2/a2p/registration | Fetch A2P Registration


# **create_a2_p_application**
> bool, date, datetime, dict, float, int, list, str, none_type create_a2_p_application(wta2_p_application_create_params)

Create A2P Application

### Example


```python
import time
import wallet
from wallet.api import a2_p_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wta2_p_application_create_params import WTA2PApplicationCreateParams
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
    wta2_p_application_create_params = WTA2PApplicationCreateParams(
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
        messaging_volume_high=True,
        address1="address1_example",
        address2="address2_example",
        city="city_example",
        state="state_example",
        postal_code="postal_code_example",
        country="country_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        job_title="job_title_example",
        job_position=JobPosition("Director"),
        phone_number="phone_number_example",
    ) # WTA2PApplicationCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create A2P Application
        api_response = api_instance.create_a2_p_application(wta2_p_application_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling A2PApi->create_a2_p_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wta2_p_application_create_params** | [**WTA2PApplicationCreateParams**](WTA2PApplicationCreateParams.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **create_a2_p_registration**
> bool, date, datetime, dict, float, int, list, str, none_type create_a2_p_registration()

Create A2P Registration

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
        # Create A2P Registration
        api_response = api_instance.create_a2_p_registration()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling A2PApi->create_a2_p_registration: %s\n" % e)
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

