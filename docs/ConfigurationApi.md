# wallet.ConfigurationApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_public_chat_room**](ConfigurationApi.md#create_public_chat_room) | **POST** /v2/wallet/createPublicChatRoom | 
[**save_merchant_credit_payment_design**](ConfigurationApi.md#save_merchant_credit_payment_design) | **PUT** /v2/wallet/merchantCredit/paymentDesign | Update wallet record
[**save_wallet_record**](ConfigurationApi.md#save_wallet_record) | **PUT** /v2/wallet | Update wallet record


# **create_public_chat_room**
> str create_public_chat_room()



Save wallet record

### Example


```python
import time
import wallet
from wallet.api import configuration_api
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
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_public_chat_room()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ConfigurationApi->create_public_chat_room: %s\n" % e)
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

# **save_merchant_credit_payment_design**
> bool, date, datetime, dict, float, int, list, str, none_type save_merchant_credit_payment_design(inline_object1)

Update wallet record

### Example


```python
import time
import wallet
from wallet.api import configuration_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.inline_object1 import InlineObject1
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    inline_object1 = InlineObject1(
        payment_design_id=NanoID("C"),
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Update wallet record
        api_response = api_instance.save_merchant_credit_payment_design(inline_object1)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ConfigurationApi->save_merchant_credit_payment_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

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

# **save_wallet_record**
> WalletConfiguration save_wallet_record(wt_wallet_configuration_save_wallet_record)

Update wallet record

### Example


```python
import time
import wallet
from wallet.api import configuration_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wallet_configuration import WalletConfiguration
from wallet.model.auth_error import AuthError
from wallet.model.wt_wallet_configuration_save_wallet_record import WTWalletConfigurationSaveWalletRecord
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    wt_wallet_configuration_save_wallet_record = WTWalletConfigurationSaveWalletRecord(
        header_background_color="#F10A44",
        header_button_color="#FFFFFF",
        left_menu_section_color="#050343",
        left_menu_arrow_color="#812934",
        company_logo_url="https://example.com/company-info/logo.png",
        header_image_url="https://example.com/company-info/logo.png",
        header_custom_icon="header_custom_icon_example",
        welcome_message="Welcome to Company!",
        is_apple_enabled=True,
        is_google_enabled=True,
        is_samsung_enabled=True,
        is_ad_credits=True,
        is_static_vouchers=True,
        is_dynamic_vouchers=True,
        is_membership_tier=True,
        is_membership_points=True,
        is_membership_level=True,
        is_gift_cards=True,
        is_gift_certificates=True,
        is_promotions=True,
        is_merchant_credit=True,
        is_tickets=True,
        is_news_articles=True,
        is_performances=True,
        is_messages=True,
        is_call=True,
        is_representatives=True,
        is_map_directions=True,
        is_link_book=True,
        is_image_grid=True,
        is_transaction_history=True,
        is_profile=True,
        is_settings=True,
        is_chat_room=True,
        is_sms_opt_in=True,
        sms_opt_in_source_id=NanoID("C"),
        is_email_subscriber=True,
        google_analytics_id="google_analytics_id_example",
        facebook_pixel_id="facebook_pixel_id_example",
        public_chat_room_channel_id=3.14,
        vanity_handle="vanity_handle_example",
        vanity_page_wallet_prefix="vanity_page_wallet_prefix_example",
        merchant_credit_payment_design_id="merchant_credit_payment_design_id_example",
    ) # WTWalletConfigurationSaveWalletRecord | 

    # example passing only required values which don't have defaults set
    try:
        # Update wallet record
        api_response = api_instance.save_wallet_record(wt_wallet_configuration_save_wallet_record)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ConfigurationApi->save_wallet_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_wallet_configuration_save_wallet_record** | [**WTWalletConfigurationSaveWalletRecord**](WTWalletConfigurationSaveWalletRecord.md)|  |

### Return type

[**WalletConfiguration**](WalletConfiguration.md)

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

