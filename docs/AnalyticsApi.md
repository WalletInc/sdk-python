# wallet.AnalyticsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_all_subscribers**](AnalyticsApi.md#count_all_subscribers) | **GET** /v2/analytics/sms/all/subscribers/count | Count opt in list subscribers
[**count_authenticated_sessions**](AnalyticsApi.md#count_authenticated_sessions) | **GET** /v2/analytics/walletPageViews/sessions/count/distinct/authenticated | Count authenticated sessions
[**count_distinct_redemptions**](AnalyticsApi.md#count_distinct_redemptions) | **GET** /v2/analytics/ledger/paymentObject/distinct/count | Fetch refund amount of campaigns by Campaign
[**count_help_desk_requests**](AnalyticsApi.md#count_help_desk_requests) | **GET** /v2/analytics/helpdeskrequests/count | Count help desk requests by date
[**count_inbound_messages**](AnalyticsApi.md#count_inbound_messages) | **GET** /v2/analytics/sms/inbound/count | Count opt in list subscribers
[**count_new_sessions**](AnalyticsApi.md#count_new_sessions) | **GET** /v2/analytics/walletPageViews/sessions/count/distinct/first | Count new sessions
[**count_opt_in_list_subscribers_partitioned_by_date**](AnalyticsApi.md#count_opt_in_list_subscribers_partitioned_by_date) | **GET** /v2/analytics/sms/all/subscribers/count/date | Count opt in list subscribers by date
[**count_outbound_messages**](AnalyticsApi.md#count_outbound_messages) | **GET** /v2/analytics/sms/outbound/count | Count opt in list subscribers
[**count_total_sessions**](AnalyticsApi.md#count_total_sessions) | **GET** /v2/analytics/walletPageViews/sessions/count/distinct | Count total sessions
[**count_transactions**](AnalyticsApi.md#count_transactions) | **GET** /v2/analytics/ledger/transactions/count | Fetch refund amount of campaigns by Campaign
[**count_verified_wallet_page_views**](AnalyticsApi.md#count_verified_wallet_page_views) | **GET** /v2/analytics/walletPageViews/sessions/verified/distinct/walletObjectsCount | Fetch wallet object counts within a given time frame that have a valid phone verification token
[**count_wallet_page_views**](AnalyticsApi.md#count_wallet_page_views) | **GET** /v2/analytics/walletPageViews/sessions/distinct/walletObjectsCount | Fetch wallet object counts within a given time frame
[**exit_link_summary**](AnalyticsApi.md#exit_link_summary) | **GET** /v2/analytics/walletPageViews/exitLinkSummary | Count exit clicks
[**fetch_analytics_ad_credits_count_partitioned_by_employee**](AnalyticsApi.md#fetch_analytics_ad_credits_count_partitioned_by_employee) | **GET** /v2/analytics/advertisementCredits/count/employee | Count ad credits by employee
[**fetch_analytics_ad_credits_count_partitioned_by_payment_design**](AnalyticsApi.md#fetch_analytics_ad_credits_count_partitioned_by_payment_design) | **GET** /v2/analytics/advertisementCredits/count/paymentDesign | Count ad credits by payment design
[**fetch_analytics_ad_credits_count_partitioned_by_value_type**](AnalyticsApi.md#fetch_analytics_ad_credits_count_partitioned_by_value_type) | **GET** /v2/analytics/advertisementCredits/count/valueType | Count ad credits by value type
[**fetch_analytics_ad_credits_redemptions_amount_partitioned_by_ad_credit_id**](AnalyticsApi.md#fetch_analytics_ad_credits_redemptions_amount_partitioned_by_ad_credit_id) | **GET** /v2/analytics/advertisementCredits/redemptions/amount/adCredit | Fetch redemption amount of ad credits by Ad Credit
[**fetch_analytics_ad_credits_redemptions_amount_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_ad_credits_redemptions_amount_partitioned_by_date) | **GET** /v2/analytics/advertisementCredits/redemptions/amount/date | Fetch redemption amount of ad credits by date
[**fetch_analytics_ad_credits_redemptions_count_partitioned_by_ad_credit_id**](AnalyticsApi.md#fetch_analytics_ad_credits_redemptions_count_partitioned_by_ad_credit_id) | **GET** /v2/analytics/advertisementCredits/redemptions/count/adCredit | Count redemptions of ad credits by Ad Credit
[**fetch_analytics_ad_credits_redemptions_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_ad_credits_redemptions_count_partitioned_by_date) | **GET** /v2/analytics/advertisementCredits/redemptions/count/date | Count redemptions of ad credits by date
[**fetch_analytics_ad_credits_refunds_amount_partitioned_by_ad_credit_id**](AnalyticsApi.md#fetch_analytics_ad_credits_refunds_amount_partitioned_by_ad_credit_id) | **GET** /v2/analytics/advertisementCredits/refunds/amount/adCredit | Fetch refund amount of ad credits by Ad Credit
[**fetch_analytics_ad_credits_refunds_amount_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_ad_credits_refunds_amount_partitioned_by_date) | **GET** /v2/analytics/advertisementCredits/refunds/amount/date | Fetch refund amount of ad credits by date
[**fetch_analytics_ad_credits_refunds_count_partitioned_by_ad_credit_id**](AnalyticsApi.md#fetch_analytics_ad_credits_refunds_count_partitioned_by_ad_credit_id) | **GET** /v2/analytics/advertisementCredits/refunds/count/adCredit | Count refunds of ad credits by Ad Credit
[**fetch_analytics_ad_credits_refunds_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_ad_credits_refunds_count_partitioned_by_date) | **GET** /v2/analytics/advertisementCredits/refunds/count/date | Count refunds of ad credits by date
[**fetch_analytics_ad_credits_scans_count_partitioned_by_ad_credit_id**](AnalyticsApi.md#fetch_analytics_ad_credits_scans_count_partitioned_by_ad_credit_id) | **GET** /v2/analytics/advertisementCredits/scans/count/adCredit | Count scans of ad credits by Ad Credit
[**fetch_analytics_ad_credits_scans_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_ad_credits_scans_count_partitioned_by_date) | **GET** /v2/analytics/advertisementCredits/scans/count/date | Count scans of ad credits by date
[**fetch_analytics_campaign_wallet_page_views**](AnalyticsApi.md#fetch_analytics_campaign_wallet_page_views) | **GET** /v2/analytics/walletPageViews/campaign/{campaignID} | Fetch a campaign&#39;s wallet page views
[**fetch_analytics_campaigns_count_partitioned_by_campaign_id**](AnalyticsApi.md#fetch_analytics_campaigns_count_partitioned_by_campaign_id) | **GET** /v2/analytics/campaigns/count/campaign/created | Count created campaigns by campaign
[**fetch_analytics_campaigns_count_partitioned_by_employee**](AnalyticsApi.md#fetch_analytics_campaigns_count_partitioned_by_employee) | **GET** /v2/analytics/campaigns/count/employee | Count campaigns by employee
[**fetch_analytics_campaigns_count_partitioned_by_payment_design**](AnalyticsApi.md#fetch_analytics_campaigns_count_partitioned_by_payment_design) | **GET** /v2/analytics/campaigns/count/paymentDesign | Count campaigns by payment design
[**fetch_analytics_campaigns_count_partitioned_by_value_type**](AnalyticsApi.md#fetch_analytics_campaigns_count_partitioned_by_value_type) | **GET** /v2/analytics/campaigns/count/valueType | Count campaigns by value type
[**fetch_analytics_campaigns_redemptions_amount_partitioned_by_campaign_id**](AnalyticsApi.md#fetch_analytics_campaigns_redemptions_amount_partitioned_by_campaign_id) | **GET** /v2/analytics/campaigns/redemptions/amount/campaign | Fetch redemption amount of campaigns by Campaign
[**fetch_analytics_campaigns_redemptions_amount_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_campaigns_redemptions_amount_partitioned_by_date) | **GET** /v2/analytics/campaigns/redemptions/amount/date | Fetch redemption amount of campaigns by date
[**fetch_analytics_campaigns_redemptions_count_partitioned_by_campaign_id**](AnalyticsApi.md#fetch_analytics_campaigns_redemptions_count_partitioned_by_campaign_id) | **GET** /v2/analytics/campaigns/redemptions/count/campaign | Count redemptions of campaigns by Campaign
[**fetch_analytics_campaigns_redemptions_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_campaigns_redemptions_count_partitioned_by_date) | **GET** /v2/analytics/campaigns/redemptions/count/date | Count redemptions of campaigns by date
[**fetch_analytics_campaigns_refunds_amount_partitioned_by_campaign_id**](AnalyticsApi.md#fetch_analytics_campaigns_refunds_amount_partitioned_by_campaign_id) | **GET** /v2/analytics/campaigns/refunds/amount/campaign | Fetch refund amount of campaigns by Campaign
[**fetch_analytics_campaigns_refunds_amount_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_campaigns_refunds_amount_partitioned_by_date) | **GET** /v2/analytics/campaigns/refunds/amount/date | Fetch refund amount of campaigns by date
[**fetch_analytics_campaigns_refunds_count_partitioned_by_campaign_id**](AnalyticsApi.md#fetch_analytics_campaigns_refunds_count_partitioned_by_campaign_id) | **GET** /v2/analytics/campaigns/refunds/count/campaign | Fetch refund amount of campaigns by Campaign
[**fetch_analytics_campaigns_refunds_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_campaigns_refunds_count_partitioned_by_date) | **GET** /v2/analytics/campaigns/refunds/count/date | Fetch refund amount of campaigns by date
[**fetch_analytics_delivered_outbound_messages_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_delivered_outbound_messages_count_partitioned_by_date) | **GET** /v2/analytics/outboundSMS/count/date/delivered | Count delivered outbound messages by date
[**fetch_analytics_delivered_outbound_messages_count_partitioned_by_phone_number**](AnalyticsApi.md#fetch_analytics_delivered_outbound_messages_count_partitioned_by_phone_number) | **GET** /v2/analytics/outboundSMS/count/phoneNumber/delivered | Count delivered outbound messages by phone number
[**fetch_analytics_distinct_wallet_sessions**](AnalyticsApi.md#fetch_analytics_distinct_wallet_sessions) | **GET** /v2/analytics/walletPageViews/sessions/distinct | Fetch distinct wallet sessions
[**fetch_analytics_dynamic_vouchers_count_partitioned_by_employee**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_count_partitioned_by_employee) | **GET** /v2/analytics/dynamicVouchers/count/employee | Count dynamic vouchers by employee
[**fetch_analytics_dynamic_vouchers_count_partitioned_by_payment_design**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_count_partitioned_by_payment_design) | **GET** /v2/analytics/dynamicVouchers/count/paymentDesign | Count dynamic vouchers by payment design
[**fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_date) | **GET** /v2/analytics/dynamicVouchers/redemptions/amount/date | Fetch redemption amount of dynamic vouchers by date
[**fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_dynamic_voucher_id**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_dynamic_voucher_id) | **GET** /v2/analytics/dynamicVouchers/redemptions/amount/dynamicVoucher | Fetch redemption amount of dynamic vouchers by dynamic voucher
[**fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_date) | **GET** /v2/analytics/dynamicVouchers/redemptions/count/date | Count redemptions of dynamic vouchers by date
[**fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_dynamic_voucher_id**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_dynamic_voucher_id) | **GET** /v2/analytics/dynamicVouchers/redemptions/count/dynamicVoucher | Count redemptions of dynamic vouchers by dynamic voucher
[**fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_date) | **GET** /v2/analytics/dynamicVouchers/refunds/amount/date | Fetch refund amount of dynamic vouchers by date
[**fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_dynamic_voucher_id**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_dynamic_voucher_id) | **GET** /v2/analytics/dynamicVouchers/refunds/amount/dynamicVoucher | Fetch refund amount of dynamic vouchers by dynamic voucher
[**fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_date) | **GET** /v2/analytics/dynamicVouchers/refunds/count/date | Count refunds of dynamic vouchers by date
[**fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_dynamic_voucher_id**](AnalyticsApi.md#fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_dynamic_voucher_id) | **GET** /v2/analytics/dynamicVouchers/refunds/count/dynamicVoucher | Count refunds of dynamic vouchers by dynamic voucher
[**fetch_analytics_help_desk_requests_created_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_help_desk_requests_created_count_partitioned_by_date) | **GET** /v2/analytics/helpdeskrequests/count/date/created | Count help desk requests by date
[**fetch_analytics_help_desk_requests_resolved_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_help_desk_requests_resolved_count_partitioned_by_date) | **GET** /v2/analytics/helpdeskrequests/count/date/resolved | Count resolved help desk requests by date
[**fetch_analytics_help_desk_requests_resolved_count_partitioned_by_employee**](AnalyticsApi.md#fetch_analytics_help_desk_requests_resolved_count_partitioned_by_employee) | **GET** /v2/analytics/helpdeskrequests/count/employee/resolved | Count resolved help desk requests by employee
[**fetch_analytics_help_desk_requests_unresolved_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_help_desk_requests_unresolved_count_partitioned_by_date) | **GET** /v2/analytics/helpdeskrequests/count/date/unresolved | Count unresolved help desk requests by date
[**fetch_analytics_item_wallet_page_views**](AnalyticsApi.md#fetch_analytics_item_wallet_page_views) | **GET** /v2/analytics/walletPageViews/item/{itemID} | Fetch wallet page views of item
[**fetch_analytics_member_count**](AnalyticsApi.md#fetch_analytics_member_count) | **GET** /v2/analytics/membership/member/count | Count members
[**fetch_analytics_merchant_credit_count**](AnalyticsApi.md#fetch_analytics_merchant_credit_count) | **GET** /v2/analytics/membership/merchantCredit/count | Count merchant credits
[**fetch_analytics_offer_vs_redeemed_amount_partitioned_by_campaign_id**](AnalyticsApi.md#fetch_analytics_offer_vs_redeemed_amount_partitioned_by_campaign_id) | **GET** /v2/analytics/campaigns/amount/campaign/offerVsRedeemed | Fetch offer vs redeemed amount by campaign
[**fetch_analytics_payment_object_broadcasts_created_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_payment_object_broadcasts_created_count_partitioned_by_date) | **GET** /v2/analytics/paymentObjectBroadcasts/count/date/created | Count created broadcasts by date
[**fetch_analytics_payment_object_broadcasts_individual_execution_time_of_completed_broadcasts**](AnalyticsApi.md#fetch_analytics_payment_object_broadcasts_individual_execution_time_of_completed_broadcasts) | **GET** /v2/analytics/paymentObjectBroadcasts/executionTime/completed | Fetch execution time of completed broadcasts
[**fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_date) | **GET** /v2/analytics/paymentObjectBroadcasts/count/date/scheduled | Count scheduled broadcasts by date
[**fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_employee**](AnalyticsApi.md#fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_employee) | **GET** /v2/analytics/paymentObjectBroadcasts/count/employee/scheduled | Count scheduled broadcasts by employee
[**fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_phone_number**](AnalyticsApi.md#fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_phone_number) | **GET** /v2/analytics/paymentObjectBroadcasts/count/phoneNumber/scheduled | Count scheduled broadcasts by phone number
[**fetch_analytics_payment_object_broadcasts_scheduled_sms_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_payment_object_broadcasts_scheduled_sms_count_partitioned_by_date) | **GET** /v2/analytics/paymentObjectBroadcasts/sms/count/date/scheduled | Count scheduled SMS broadcasts by date
[**fetch_analytics_sent_outbound_messages_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_sent_outbound_messages_count_partitioned_by_date) | **GET** /v2/analytics/outboundSMS/count/date/sent | Count sent outbound messages by date
[**fetch_analytics_sent_outbound_messages_count_partitioned_by_phone_number**](AnalyticsApi.md#fetch_analytics_sent_outbound_messages_count_partitioned_by_phone_number) | **GET** /v2/analytics/outboundSMS/count/phoneNumber/sent | Count sent outbound messages by phone number
[**fetch_analytics_static_voucher_wallet_page_views**](AnalyticsApi.md#fetch_analytics_static_voucher_wallet_page_views) | **GET** /v2/analytics/walletPageViews/staticVoucher/{voucherID} | Fetch a static voucher&#39;s wallet page views
[**fetch_analytics_tcpa_filters_create_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_tcpa_filters_create_count_partitioned_by_date) | **GET** /v2/analytics/tcpafilters/count/date/create | Count created TCPA Filter entries by date
[**fetch_analytics_tcpa_filters_delete_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_tcpa_filters_delete_count_partitioned_by_date) | **GET** /v2/analytics/tcpafilters/count/date/delete | Count deleted TCPA Filter entries by date
[**fetch_analytics_tcpa_stop_count_partitioned_by_date**](AnalyticsApi.md#fetch_analytics_tcpa_stop_count_partitioned_by_date) | **GET** /v2/analytics/tcpa/count/date/stop | Count TCPA (STOP) entries by date
[**fetch_analytics_tcpa_stop_count_partitioned_by_phone_number**](AnalyticsApi.md#fetch_analytics_tcpa_stop_count_partitioned_by_phone_number) | **GET** /v2/analytics/tcpa/count/phoneNumber/stop | Count TCPA (STOP) entries by phone number
[**fetch_analytics_total_amount_redeemed_per_merchant_credit**](AnalyticsApi.md#fetch_analytics_total_amount_redeemed_per_merchant_credit) | **GET** /v2/analytics/membership/merchantCredit/amount/redeemed | Fetch redeemed amount of merchant credits
[**fetch_analytics_total_amount_redeemed_per_tier**](AnalyticsApi.md#fetch_analytics_total_amount_redeemed_per_tier) | **GET** /v2/analytics/membership/tier/amount/redeemed | Fetch redeemed amoun̥t of tiers
[**fetch_analytics_total_amount_refunded_per_merchant_credit**](AnalyticsApi.md#fetch_analytics_total_amount_refunded_per_merchant_credit) | **GET** /v2/analytics/membership/merchantCredit/amount/refunded | Fetch refunded amount of merchant credits
[**fetch_analytics_total_amount_refunded_per_tier**](AnalyticsApi.md#fetch_analytics_total_amount_refunded_per_tier) | **GET** /v2/analytics/membership/tier/amount/refunded | Fetch refunded amount of tiers
[**fetch_analytics_total_points_redeemed**](AnalyticsApi.md#fetch_analytics_total_points_redeemed) | **GET** /v2/analytics/membership/member/points/redeemed | Count redeemed points
[**fetch_analytics_total_points_refunded**](AnalyticsApi.md#fetch_analytics_total_points_refunded) | **GET** /v2/analytics/membership/member/points/refunded | Count refunded points
[**fetch_analytics_wallet_session_activity**](AnalyticsApi.md#fetch_analytics_wallet_session_activity) | **GET** /v2/analytics/walletPageViews/session/activity/{sessionID} | Fetch session activity
[**fetch_wallet_page_view_by_id**](AnalyticsApi.md#fetch_wallet_page_view_by_id) | **GET** /v2/analytics/walletPageViews/activity/{id} | Fetch session activity by wallet page view ID
[**referring_sites_summary**](AnalyticsApi.md#referring_sites_summary) | **GET** /v2/analytics/walletPageViews/referringSitesSummary | Count referring sites
[**sum_revenue**](AnalyticsApi.md#sum_revenue) | **GET** /v2/analytics/ledger/revenue/sum | Fetch refund amount of campaigns by Campaign
[**sum_transactions**](AnalyticsApi.md#sum_transactions) | **GET** /v2/analytics/ledger/transactions/sum | Fetch refund amount of campaigns by Campaign


# **count_all_subscribers**
> WTCountResult count_all_subscribers(is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)

Count opt in list subscribers

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
    api_instance = wallet.AnalyticsApi(api_client)
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count opt in list subscribers
        api_response = api_instance.count_all_subscribers(is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->count_all_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_all_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
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

# **count_authenticated_sessions**
> object count_authenticated_sessions(start_date=start_date, end_date=end_date)

Count authenticated sessions

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count authenticated sessions
        api_response = api_instance.count_authenticated_sessions(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->count_authenticated_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_authenticated_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **count_distinct_redemptions**
> object count_distinct_redemptions(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)

Fetch refund amount of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    transaction_type = 'transaction_type_example' # str |  (optional)
    segment_type = 'segment_type_example' # str |  (optional)

    try:
        # Fetch refund amount of campaigns by Campaign
        api_response = api_instance.count_distinct_redemptions(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)
        print("The response of AnalyticsApi->count_distinct_redemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_distinct_redemptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **transaction_type** | **str**|  | [optional] 
 **segment_type** | **str**|  | [optional] 

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

# **count_help_desk_requests**
> object count_help_desk_requests(start_date, end_date, locale, timezone, is_resolved=is_resolved)

Count help desk requests by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 
    is_resolved = True # bool |  (optional)

    try:
        # Count help desk requests by date
        api_response = api_instance.count_help_desk_requests(start_date, end_date, locale, timezone, is_resolved=is_resolved)
        print("The response of AnalyticsApi->count_help_desk_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_help_desk_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 
 **is_resolved** | **bool**|  | [optional] 

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

# **count_inbound_messages**
> WTCountResult count_inbound_messages(start_date=start_date, end_date=end_date)

Count opt in list subscribers

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count opt in list subscribers
        api_response = api_instance.count_inbound_messages(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->count_inbound_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_inbound_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **count_new_sessions**
> object count_new_sessions(start_date=start_date, end_date=end_date)

Count new sessions

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count new sessions
        api_response = api_instance.count_new_sessions(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->count_new_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_new_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **count_opt_in_list_subscribers_partitioned_by_date**
> object count_opt_in_list_subscribers_partitioned_by_date(start_date, end_date)

Count opt in list subscribers by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count opt in list subscribers by date
        api_response = api_instance.count_opt_in_list_subscribers_partitioned_by_date(start_date, end_date)
        print("The response of AnalyticsApi->count_opt_in_list_subscribers_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_opt_in_list_subscribers_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **count_outbound_messages**
> WTCountResult count_outbound_messages(start_date=start_date, end_date=end_date)

Count opt in list subscribers

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count opt in list subscribers
        api_response = api_instance.count_outbound_messages(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->count_outbound_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_outbound_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **count_total_sessions**
> object count_total_sessions(start_date=start_date, end_date=end_date)

Count total sessions

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count total sessions
        api_response = api_instance.count_total_sessions(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->count_total_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_total_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **count_transactions**
> object count_transactions(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)

Fetch refund amount of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    transaction_type = 'transaction_type_example' # str |  (optional)
    segment_type = 'segment_type_example' # str |  (optional)

    try:
        # Fetch refund amount of campaigns by Campaign
        api_response = api_instance.count_transactions(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)
        print("The response of AnalyticsApi->count_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **transaction_type** | **str**|  | [optional] 
 **segment_type** | **str**|  | [optional] 

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

# **count_verified_wallet_page_views**
> List[WTWalletObjectPrefixCounts] count_verified_wallet_page_views(start_date, end_date)

Fetch wallet object counts within a given time frame that have a valid phone verification token

### Example


```python
import wallet
from wallet.models.wt_wallet_object_prefix_counts import WTWalletObjectPrefixCounts
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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch wallet object counts within a given time frame that have a valid phone verification token
        api_response = api_instance.count_verified_wallet_page_views(start_date, end_date)
        print("The response of AnalyticsApi->count_verified_wallet_page_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_verified_wallet_page_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

### Return type

[**List[WTWalletObjectPrefixCounts]**](WTWalletObjectPrefixCounts.md)

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

# **count_wallet_page_views**
> List[WTWalletObjectPrefixCounts] count_wallet_page_views(start_date, end_date)

Fetch wallet object counts within a given time frame

### Example


```python
import wallet
from wallet.models.wt_wallet_object_prefix_counts import WTWalletObjectPrefixCounts
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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch wallet object counts within a given time frame
        api_response = api_instance.count_wallet_page_views(start_date, end_date)
        print("The response of AnalyticsApi->count_wallet_page_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->count_wallet_page_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

### Return type

[**List[WTWalletObjectPrefixCounts]**](WTWalletObjectPrefixCounts.md)

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

# **exit_link_summary**
> object exit_link_summary(start_date=start_date, end_date=end_date)

Count exit clicks

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count exit clicks
        api_response = api_instance.exit_link_summary(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->exit_link_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->exit_link_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **fetch_analytics_ad_credits_count_partitioned_by_employee**
> List[object] fetch_analytics_ad_credits_count_partitioned_by_employee(start_date, end_date)

Count ad credits by employee

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count ad credits by employee
        api_response = api_instance.fetch_analytics_ad_credits_count_partitioned_by_employee(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_count_partitioned_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_count_partitioned_by_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_count_partitioned_by_payment_design**
> List[object] fetch_analytics_ad_credits_count_partitioned_by_payment_design(start_date, end_date)

Count ad credits by payment design

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count ad credits by payment design
        api_response = api_instance.fetch_analytics_ad_credits_count_partitioned_by_payment_design(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_count_partitioned_by_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_count_partitioned_by_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_count_partitioned_by_value_type**
> object fetch_analytics_ad_credits_count_partitioned_by_value_type(start_date, end_date)

Count ad credits by value type

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count ad credits by value type
        api_response = api_instance.fetch_analytics_ad_credits_count_partitioned_by_value_type(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_count_partitioned_by_value_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_count_partitioned_by_value_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_redemptions_amount_partitioned_by_ad_credit_id**
> List[object] fetch_analytics_ad_credits_redemptions_amount_partitioned_by_ad_credit_id(start_date, end_date)

Fetch redemption amount of ad credits by Ad Credit

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch redemption amount of ad credits by Ad Credit
        api_response = api_instance.fetch_analytics_ad_credits_redemptions_amount_partitioned_by_ad_credit_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_redemptions_amount_partitioned_by_ad_credit_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_redemptions_amount_partitioned_by_ad_credit_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_redemptions_amount_partitioned_by_date**
> object fetch_analytics_ad_credits_redemptions_amount_partitioned_by_date(start_date, end_date, locale, timezone)

Fetch redemption amount of ad credits by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch redemption amount of ad credits by date
        api_response = api_instance.fetch_analytics_ad_credits_redemptions_amount_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_redemptions_amount_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_redemptions_amount_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_ad_credits_redemptions_count_partitioned_by_ad_credit_id**
> List[object] fetch_analytics_ad_credits_redemptions_count_partitioned_by_ad_credit_id(start_date, end_date)

Count redemptions of ad credits by Ad Credit

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count redemptions of ad credits by Ad Credit
        api_response = api_instance.fetch_analytics_ad_credits_redemptions_count_partitioned_by_ad_credit_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_redemptions_count_partitioned_by_ad_credit_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_redemptions_count_partitioned_by_ad_credit_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_redemptions_count_partitioned_by_date**
> object fetch_analytics_ad_credits_redemptions_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count redemptions of ad credits by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count redemptions of ad credits by date
        api_response = api_instance.fetch_analytics_ad_credits_redemptions_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_redemptions_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_redemptions_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_ad_credits_refunds_amount_partitioned_by_ad_credit_id**
> List[object] fetch_analytics_ad_credits_refunds_amount_partitioned_by_ad_credit_id(start_date, end_date)

Fetch refund amount of ad credits by Ad Credit

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch refund amount of ad credits by Ad Credit
        api_response = api_instance.fetch_analytics_ad_credits_refunds_amount_partitioned_by_ad_credit_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_refunds_amount_partitioned_by_ad_credit_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_refunds_amount_partitioned_by_ad_credit_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_refunds_amount_partitioned_by_date**
> object fetch_analytics_ad_credits_refunds_amount_partitioned_by_date(start_date, end_date, locale, timezone)

Fetch refund amount of ad credits by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch refund amount of ad credits by date
        api_response = api_instance.fetch_analytics_ad_credits_refunds_amount_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_refunds_amount_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_refunds_amount_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_ad_credits_refunds_count_partitioned_by_ad_credit_id**
> List[object] fetch_analytics_ad_credits_refunds_count_partitioned_by_ad_credit_id(start_date, end_date)

Count refunds of ad credits by Ad Credit

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count refunds of ad credits by Ad Credit
        api_response = api_instance.fetch_analytics_ad_credits_refunds_count_partitioned_by_ad_credit_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_refunds_count_partitioned_by_ad_credit_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_refunds_count_partitioned_by_ad_credit_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_refunds_count_partitioned_by_date**
> object fetch_analytics_ad_credits_refunds_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count refunds of ad credits by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count refunds of ad credits by date
        api_response = api_instance.fetch_analytics_ad_credits_refunds_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_refunds_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_refunds_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_ad_credits_scans_count_partitioned_by_ad_credit_id**
> List[object] fetch_analytics_ad_credits_scans_count_partitioned_by_ad_credit_id(start_date, end_date)

Count scans of ad credits by Ad Credit

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count scans of ad credits by Ad Credit
        api_response = api_instance.fetch_analytics_ad_credits_scans_count_partitioned_by_ad_credit_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_scans_count_partitioned_by_ad_credit_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_scans_count_partitioned_by_ad_credit_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_ad_credits_scans_count_partitioned_by_date**
> object fetch_analytics_ad_credits_scans_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count scans of ad credits by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count scans of ad credits by date
        api_response = api_instance.fetch_analytics_ad_credits_scans_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_ad_credits_scans_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_ad_credits_scans_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_campaign_wallet_page_views**
> List[WTWalletPageView] fetch_analytics_campaign_wallet_page_views(campaign_id)

Fetch a campaign's wallet page views

### Example


```python
import wallet
from wallet.models.wt_wallet_page_view import WTWalletPageView
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
    api_instance = wallet.AnalyticsApi(api_client)
    campaign_id = None # object | 

    try:
        # Fetch a campaign's wallet page views
        api_response = api_instance.fetch_analytics_campaign_wallet_page_views(campaign_id)
        print("The response of AnalyticsApi->fetch_analytics_campaign_wallet_page_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaign_wallet_page_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**List[WTWalletPageView]**](WTWalletPageView.md)

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

# **fetch_analytics_campaigns_count_partitioned_by_campaign_id**
> List[object] fetch_analytics_campaigns_count_partitioned_by_campaign_id(start_date, end_date)

Count created campaigns by campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count created campaigns by campaign
        api_response = api_instance.fetch_analytics_campaigns_count_partitioned_by_campaign_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_campaign_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_campaign_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_count_partitioned_by_employee**
> List[object] fetch_analytics_campaigns_count_partitioned_by_employee(start_date, end_date)

Count campaigns by employee

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count campaigns by employee
        api_response = api_instance.fetch_analytics_campaigns_count_partitioned_by_employee(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_count_partitioned_by_payment_design**
> List[object] fetch_analytics_campaigns_count_partitioned_by_payment_design(start_date, end_date)

Count campaigns by payment design

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count campaigns by payment design
        api_response = api_instance.fetch_analytics_campaigns_count_partitioned_by_payment_design(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_count_partitioned_by_value_type**
> object fetch_analytics_campaigns_count_partitioned_by_value_type(start_date, end_date)

Count campaigns by value type

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count campaigns by value type
        api_response = api_instance.fetch_analytics_campaigns_count_partitioned_by_value_type(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_value_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_count_partitioned_by_value_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_redemptions_amount_partitioned_by_campaign_id**
> List[object] fetch_analytics_campaigns_redemptions_amount_partitioned_by_campaign_id(start_date, end_date)

Fetch redemption amount of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch redemption amount of campaigns by Campaign
        api_response = api_instance.fetch_analytics_campaigns_redemptions_amount_partitioned_by_campaign_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_redemptions_amount_partitioned_by_campaign_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_redemptions_amount_partitioned_by_campaign_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_redemptions_amount_partitioned_by_date**
> object fetch_analytics_campaigns_redemptions_amount_partitioned_by_date(start_date, end_date, locale, timezone)

Fetch redemption amount of campaigns by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch redemption amount of campaigns by date
        api_response = api_instance.fetch_analytics_campaigns_redemptions_amount_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_redemptions_amount_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_redemptions_amount_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_campaigns_redemptions_count_partitioned_by_campaign_id**
> List[object] fetch_analytics_campaigns_redemptions_count_partitioned_by_campaign_id(start_date, end_date)

Count redemptions of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count redemptions of campaigns by Campaign
        api_response = api_instance.fetch_analytics_campaigns_redemptions_count_partitioned_by_campaign_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_redemptions_count_partitioned_by_campaign_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_redemptions_count_partitioned_by_campaign_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_redemptions_count_partitioned_by_date**
> object fetch_analytics_campaigns_redemptions_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count redemptions of campaigns by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count redemptions of campaigns by date
        api_response = api_instance.fetch_analytics_campaigns_redemptions_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_redemptions_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_redemptions_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_campaigns_refunds_amount_partitioned_by_campaign_id**
> List[object] fetch_analytics_campaigns_refunds_amount_partitioned_by_campaign_id(start_date, end_date)

Fetch refund amount of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch refund amount of campaigns by Campaign
        api_response = api_instance.fetch_analytics_campaigns_refunds_amount_partitioned_by_campaign_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_refunds_amount_partitioned_by_campaign_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_refunds_amount_partitioned_by_campaign_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_refunds_amount_partitioned_by_date**
> object fetch_analytics_campaigns_refunds_amount_partitioned_by_date(start_date, end_date, locale, timezone)

Fetch refund amount of campaigns by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch refund amount of campaigns by date
        api_response = api_instance.fetch_analytics_campaigns_refunds_amount_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_refunds_amount_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_refunds_amount_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_campaigns_refunds_count_partitioned_by_campaign_id**
> List[object] fetch_analytics_campaigns_refunds_count_partitioned_by_campaign_id(start_date, end_date)

Fetch refund amount of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch refund amount of campaigns by Campaign
        api_response = api_instance.fetch_analytics_campaigns_refunds_count_partitioned_by_campaign_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_refunds_count_partitioned_by_campaign_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_refunds_count_partitioned_by_campaign_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_campaigns_refunds_count_partitioned_by_date**
> object fetch_analytics_campaigns_refunds_count_partitioned_by_date(start_date, end_date, locale, timezone)

Fetch refund amount of campaigns by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch refund amount of campaigns by date
        api_response = api_instance.fetch_analytics_campaigns_refunds_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_campaigns_refunds_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_campaigns_refunds_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_delivered_outbound_messages_count_partitioned_by_date**
> object fetch_analytics_delivered_outbound_messages_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count delivered outbound messages by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count delivered outbound messages by date
        api_response = api_instance.fetch_analytics_delivered_outbound_messages_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_delivered_outbound_messages_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_delivered_outbound_messages_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_delivered_outbound_messages_count_partitioned_by_phone_number**
> List[object] fetch_analytics_delivered_outbound_messages_count_partitioned_by_phone_number(start_date, end_date)

Count delivered outbound messages by phone number

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count delivered outbound messages by phone number
        api_response = api_instance.fetch_analytics_delivered_outbound_messages_count_partitioned_by_phone_number(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_delivered_outbound_messages_count_partitioned_by_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_delivered_outbound_messages_count_partitioned_by_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_distinct_wallet_sessions**
> object fetch_analytics_distinct_wallet_sessions(start_date=start_date, end_date=end_date)

Fetch distinct wallet sessions

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Fetch distinct wallet sessions
        api_response = api_instance.fetch_analytics_distinct_wallet_sessions(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->fetch_analytics_distinct_wallet_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_distinct_wallet_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **fetch_analytics_dynamic_vouchers_count_partitioned_by_employee**
> List[object] fetch_analytics_dynamic_vouchers_count_partitioned_by_employee(start_date, end_date)

Count dynamic vouchers by employee

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count dynamic vouchers by employee
        api_response = api_instance.fetch_analytics_dynamic_vouchers_count_partitioned_by_employee(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_count_partitioned_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_count_partitioned_by_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_dynamic_vouchers_count_partitioned_by_payment_design**
> List[object] fetch_analytics_dynamic_vouchers_count_partitioned_by_payment_design(start_date, end_date)

Count dynamic vouchers by payment design

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count dynamic vouchers by payment design
        api_response = api_instance.fetch_analytics_dynamic_vouchers_count_partitioned_by_payment_design(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_count_partitioned_by_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_count_partitioned_by_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_date**
> object fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_date(start_date, end_date, locale, timezone)

Fetch redemption amount of dynamic vouchers by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch redemption amount of dynamic vouchers by date
        api_response = api_instance.fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_dynamic_voucher_id**
> List[object] fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_dynamic_voucher_id(start_date, end_date)

Fetch redemption amount of dynamic vouchers by dynamic voucher

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch redemption amount of dynamic vouchers by dynamic voucher
        api_response = api_instance.fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_dynamic_voucher_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_dynamic_voucher_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_amount_partitioned_by_dynamic_voucher_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_date**
> List[object] fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count redemptions of dynamic vouchers by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count redemptions of dynamic vouchers by date
        api_response = api_instance.fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_dynamic_voucher_id**
> List[object] fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_dynamic_voucher_id(start_date, end_date)

Count redemptions of dynamic vouchers by dynamic voucher

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count redemptions of dynamic vouchers by dynamic voucher
        api_response = api_instance.fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_dynamic_voucher_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_dynamic_voucher_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_redemptions_count_partitioned_by_dynamic_voucher_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_date**
> object fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_date(start_date, end_date, locale, timezone)

Fetch refund amount of dynamic vouchers by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch refund amount of dynamic vouchers by date
        api_response = api_instance.fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_dynamic_voucher_id**
> List[object] fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_dynamic_voucher_id(start_date, end_date)

Fetch refund amount of dynamic vouchers by dynamic voucher

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch refund amount of dynamic vouchers by dynamic voucher
        api_response = api_instance.fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_dynamic_voucher_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_dynamic_voucher_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_amount_partitioned_by_dynamic_voucher_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_date**
> object fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count refunds of dynamic vouchers by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count refunds of dynamic vouchers by date
        api_response = api_instance.fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_dynamic_voucher_id**
> List[object] fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_dynamic_voucher_id(start_date, end_date)

Count refunds of dynamic vouchers by dynamic voucher

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count refunds of dynamic vouchers by dynamic voucher
        api_response = api_instance.fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_dynamic_voucher_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_dynamic_voucher_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_dynamic_vouchers_refunds_count_partitioned_by_dynamic_voucher_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_help_desk_requests_created_count_partitioned_by_date**
> object fetch_analytics_help_desk_requests_created_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count help desk requests by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count help desk requests by date
        api_response = api_instance.fetch_analytics_help_desk_requests_created_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_help_desk_requests_created_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_help_desk_requests_created_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_help_desk_requests_resolved_count_partitioned_by_date**
> object fetch_analytics_help_desk_requests_resolved_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count resolved help desk requests by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count resolved help desk requests by date
        api_response = api_instance.fetch_analytics_help_desk_requests_resolved_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_help_desk_requests_resolved_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_help_desk_requests_resolved_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_help_desk_requests_resolved_count_partitioned_by_employee**
> List[object] fetch_analytics_help_desk_requests_resolved_count_partitioned_by_employee(start_date, end_date)

Count resolved help desk requests by employee

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count resolved help desk requests by employee
        api_response = api_instance.fetch_analytics_help_desk_requests_resolved_count_partitioned_by_employee(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_help_desk_requests_resolved_count_partitioned_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_help_desk_requests_resolved_count_partitioned_by_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_help_desk_requests_unresolved_count_partitioned_by_date**
> object fetch_analytics_help_desk_requests_unresolved_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count unresolved help desk requests by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count unresolved help desk requests by date
        api_response = api_instance.fetch_analytics_help_desk_requests_unresolved_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_help_desk_requests_unresolved_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_help_desk_requests_unresolved_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_item_wallet_page_views**
> object fetch_analytics_item_wallet_page_views(item_id)

Fetch wallet page views of item

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
    api_instance = wallet.AnalyticsApi(api_client)
    item_id = 'item_id_example' # str | 

    try:
        # Fetch wallet page views of item
        api_response = api_instance.fetch_analytics_item_wallet_page_views(item_id)
        print("The response of AnalyticsApi->fetch_analytics_item_wallet_page_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_item_wallet_page_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 

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

# **fetch_analytics_member_count**
> List[MSAnalyticsMemberCountPartitionedByDate] fetch_analytics_member_count(start_date, end_date, locale, timezone)

Count members

### Example


```python
import wallet
from wallet.models.ms_analytics_member_count_partitioned_by_date import MSAnalyticsMemberCountPartitionedByDate
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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count members
        api_response = api_instance.fetch_analytics_member_count(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_member_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_member_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

### Return type

[**List[MSAnalyticsMemberCountPartitionedByDate]**](MSAnalyticsMemberCountPartitionedByDate.md)

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

# **fetch_analytics_merchant_credit_count**
> object fetch_analytics_merchant_credit_count(start_date, end_date, locale, timezone)

Count merchant credits

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count merchant credits
        api_response = api_instance.fetch_analytics_merchant_credit_count(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_merchant_credit_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_merchant_credit_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_offer_vs_redeemed_amount_partitioned_by_campaign_id**
> List[object] fetch_analytics_offer_vs_redeemed_amount_partitioned_by_campaign_id(start_date, end_date)

Fetch offer vs redeemed amount by campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch offer vs redeemed amount by campaign
        api_response = api_instance.fetch_analytics_offer_vs_redeemed_amount_partitioned_by_campaign_id(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_offer_vs_redeemed_amount_partitioned_by_campaign_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_offer_vs_redeemed_amount_partitioned_by_campaign_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_payment_object_broadcasts_created_count_partitioned_by_date**
> object fetch_analytics_payment_object_broadcasts_created_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count created broadcasts by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count created broadcasts by date
        api_response = api_instance.fetch_analytics_payment_object_broadcasts_created_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_payment_object_broadcasts_created_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_payment_object_broadcasts_created_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_payment_object_broadcasts_individual_execution_time_of_completed_broadcasts**
> object fetch_analytics_payment_object_broadcasts_individual_execution_time_of_completed_broadcasts(start_date, end_date)

Fetch execution time of completed broadcasts

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch execution time of completed broadcasts
        api_response = api_instance.fetch_analytics_payment_object_broadcasts_individual_execution_time_of_completed_broadcasts(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_payment_object_broadcasts_individual_execution_time_of_completed_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_payment_object_broadcasts_individual_execution_time_of_completed_broadcasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_date**
> object fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count scheduled broadcasts by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count scheduled broadcasts by date
        api_response = api_instance.fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_employee**
> List[object] fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_employee(start_date, end_date)

Count scheduled broadcasts by employee

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count scheduled broadcasts by employee
        api_response = api_instance.fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_employee(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_phone_number**
> List[object] fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_phone_number(start_date, end_date)

Count scheduled broadcasts by phone number

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count scheduled broadcasts by phone number
        api_response = api_instance.fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_phone_number(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_count_partitioned_by_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_payment_object_broadcasts_scheduled_sms_count_partitioned_by_date**
> object fetch_analytics_payment_object_broadcasts_scheduled_sms_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count scheduled SMS broadcasts by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count scheduled SMS broadcasts by date
        api_response = api_instance.fetch_analytics_payment_object_broadcasts_scheduled_sms_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_sms_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_payment_object_broadcasts_scheduled_sms_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_sent_outbound_messages_count_partitioned_by_date**
> object fetch_analytics_sent_outbound_messages_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count sent outbound messages by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count sent outbound messages by date
        api_response = api_instance.fetch_analytics_sent_outbound_messages_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_sent_outbound_messages_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_sent_outbound_messages_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_sent_outbound_messages_count_partitioned_by_phone_number**
> List[object] fetch_analytics_sent_outbound_messages_count_partitioned_by_phone_number(start_date, end_date)

Count sent outbound messages by phone number

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count sent outbound messages by phone number
        api_response = api_instance.fetch_analytics_sent_outbound_messages_count_partitioned_by_phone_number(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_sent_outbound_messages_count_partitioned_by_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_sent_outbound_messages_count_partitioned_by_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_static_voucher_wallet_page_views**
> List[WTWalletPageView] fetch_analytics_static_voucher_wallet_page_views(voucher_id)

Fetch a static voucher's wallet page views

### Example


```python
import wallet
from wallet.models.wt_wallet_page_view import WTWalletPageView
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
    api_instance = wallet.AnalyticsApi(api_client)
    voucher_id = None # object | 

    try:
        # Fetch a static voucher's wallet page views
        api_response = api_instance.fetch_analytics_static_voucher_wallet_page_views(voucher_id)
        print("The response of AnalyticsApi->fetch_analytics_static_voucher_wallet_page_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_static_voucher_wallet_page_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | [**object**](.md)|  | 

### Return type

[**List[WTWalletPageView]**](WTWalletPageView.md)

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

# **fetch_analytics_tcpa_filters_create_count_partitioned_by_date**
> object fetch_analytics_tcpa_filters_create_count_partitioned_by_date(start_date, end_date)

Count created TCPA Filter entries by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count created TCPA Filter entries by date
        api_response = api_instance.fetch_analytics_tcpa_filters_create_count_partitioned_by_date(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_tcpa_filters_create_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_tcpa_filters_create_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_tcpa_filters_delete_count_partitioned_by_date**
> object fetch_analytics_tcpa_filters_delete_count_partitioned_by_date(start_date, end_date)

Count deleted TCPA Filter entries by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count deleted TCPA Filter entries by date
        api_response = api_instance.fetch_analytics_tcpa_filters_delete_count_partitioned_by_date(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_tcpa_filters_delete_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_tcpa_filters_delete_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_tcpa_stop_count_partitioned_by_date**
> object fetch_analytics_tcpa_stop_count_partitioned_by_date(start_date, end_date, locale, timezone)

Count TCPA (STOP) entries by date

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count TCPA (STOP) entries by date
        api_response = api_instance.fetch_analytics_tcpa_stop_count_partitioned_by_date(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_tcpa_stop_count_partitioned_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_tcpa_stop_count_partitioned_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_tcpa_stop_count_partitioned_by_phone_number**
> List[object] fetch_analytics_tcpa_stop_count_partitioned_by_phone_number(start_date, end_date)

Count TCPA (STOP) entries by phone number

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count TCPA (STOP) entries by phone number
        api_response = api_instance.fetch_analytics_tcpa_stop_count_partitioned_by_phone_number(start_date, end_date)
        print("The response of AnalyticsApi->fetch_analytics_tcpa_stop_count_partitioned_by_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_tcpa_stop_count_partitioned_by_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

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

# **fetch_analytics_total_amount_redeemed_per_merchant_credit**
> object fetch_analytics_total_amount_redeemed_per_merchant_credit(start_date, end_date, locale, timezone)

Fetch redeemed amount of merchant credits

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch redeemed amount of merchant credits
        api_response = api_instance.fetch_analytics_total_amount_redeemed_per_merchant_credit(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_total_amount_redeemed_per_merchant_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_total_amount_redeemed_per_merchant_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_total_amount_redeemed_per_tier**
> List[MSAnalyticsMembershipTierAmountRedeemedPartitionedByDate] fetch_analytics_total_amount_redeemed_per_tier(start_date, end_date, locale, timezone)

Fetch redeemed amoun̥t of tiers

### Example


```python
import wallet
from wallet.models.ms_analytics_membership_tier_amount_redeemed_partitioned_by_date import MSAnalyticsMembershipTierAmountRedeemedPartitionedByDate
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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch redeemed amoun̥t of tiers
        api_response = api_instance.fetch_analytics_total_amount_redeemed_per_tier(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_total_amount_redeemed_per_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_total_amount_redeemed_per_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

### Return type

[**List[MSAnalyticsMembershipTierAmountRedeemedPartitionedByDate]**](MSAnalyticsMembershipTierAmountRedeemedPartitionedByDate.md)

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

# **fetch_analytics_total_amount_refunded_per_merchant_credit**
> object fetch_analytics_total_amount_refunded_per_merchant_credit(start_date, end_date, locale, timezone)

Fetch refunded amount of merchant credits

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch refunded amount of merchant credits
        api_response = api_instance.fetch_analytics_total_amount_refunded_per_merchant_credit(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_total_amount_refunded_per_merchant_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_total_amount_refunded_per_merchant_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

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

# **fetch_analytics_total_amount_refunded_per_tier**
> List[MSAnalyticsMembershipTierAmountRefundedPartitionedByDate] fetch_analytics_total_amount_refunded_per_tier(start_date, end_date, locale, timezone)

Fetch refunded amount of tiers

### Example


```python
import wallet
from wallet.models.ms_analytics_membership_tier_amount_refunded_partitioned_by_date import MSAnalyticsMembershipTierAmountRefundedPartitionedByDate
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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Fetch refunded amount of tiers
        api_response = api_instance.fetch_analytics_total_amount_refunded_per_tier(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_total_amount_refunded_per_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_total_amount_refunded_per_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

### Return type

[**List[MSAnalyticsMembershipTierAmountRefundedPartitionedByDate]**](MSAnalyticsMembershipTierAmountRefundedPartitionedByDate.md)

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

# **fetch_analytics_total_points_redeemed**
> List[MSAnalyticsMemberPointsRedeemedPartitionedByDate] fetch_analytics_total_points_redeemed(start_date, end_date, locale, timezone)

Count redeemed points

### Example


```python
import wallet
from wallet.models.ms_analytics_member_points_redeemed_partitioned_by_date import MSAnalyticsMemberPointsRedeemedPartitionedByDate
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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count redeemed points
        api_response = api_instance.fetch_analytics_total_points_redeemed(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_total_points_redeemed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_total_points_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

### Return type

[**List[MSAnalyticsMemberPointsRedeemedPartitionedByDate]**](MSAnalyticsMemberPointsRedeemedPartitionedByDate.md)

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

# **fetch_analytics_total_points_refunded**
> List[MSAnalyticsMemberPointsRefundedPartitionedByDate] fetch_analytics_total_points_refunded(start_date, end_date, locale, timezone)

Count refunded points

### Example


```python
import wallet
from wallet.models.ms_analytics_member_points_refunded_partitioned_by_date import MSAnalyticsMemberPointsRefundedPartitionedByDate
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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    locale = 'locale_example' # str | 
    timezone = 'timezone_example' # str | 

    try:
        # Count refunded points
        api_response = api_instance.fetch_analytics_total_points_refunded(start_date, end_date, locale, timezone)
        print("The response of AnalyticsApi->fetch_analytics_total_points_refunded:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_total_points_refunded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **locale** | **str**|  | 
 **timezone** | **str**|  | 

### Return type

[**List[MSAnalyticsMemberPointsRefundedPartitionedByDate]**](MSAnalyticsMemberPointsRefundedPartitionedByDate.md)

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

# **fetch_analytics_wallet_session_activity**
> List[WTWalletPageView] fetch_analytics_wallet_session_activity(session_id)

Fetch session activity

### Example


```python
import wallet
from wallet.models.wt_wallet_page_view import WTWalletPageView
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
    api_instance = wallet.AnalyticsApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Fetch session activity
        api_response = api_instance.fetch_analytics_wallet_session_activity(session_id)
        print("The response of AnalyticsApi->fetch_analytics_wallet_session_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_analytics_wallet_session_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**List[WTWalletPageView]**](WTWalletPageView.md)

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

# **fetch_wallet_page_view_by_id**
> WalletPageView fetch_wallet_page_view_by_id(id)

Fetch session activity by wallet page view ID

### Example


```python
import wallet
from wallet.models.wallet_page_view import WalletPageView
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
    api_instance = wallet.AnalyticsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Fetch session activity by wallet page view ID
        api_response = api_instance.fetch_wallet_page_view_by_id(id)
        print("The response of AnalyticsApi->fetch_wallet_page_view_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->fetch_wallet_page_view_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WalletPageView**](WalletPageView.md)

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

# **referring_sites_summary**
> object referring_sites_summary(start_date=start_date, end_date=end_date)

Count referring sites

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count referring sites
        api_response = api_instance.referring_sites_summary(start_date=start_date, end_date=end_date)
        print("The response of AnalyticsApi->referring_sites_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->referring_sites_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **sum_revenue**
> object sum_revenue(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)

Fetch refund amount of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    transaction_type = 'transaction_type_example' # str |  (optional)
    segment_type = 'segment_type_example' # str |  (optional)

    try:
        # Fetch refund amount of campaigns by Campaign
        api_response = api_instance.sum_revenue(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)
        print("The response of AnalyticsApi->sum_revenue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->sum_revenue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **transaction_type** | **str**|  | [optional] 
 **segment_type** | **str**|  | [optional] 

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

# **sum_transactions**
> object sum_transactions(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)

Fetch refund amount of campaigns by Campaign

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
    api_instance = wallet.AnalyticsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date = '2013-10-20T19:20:30+01:00' # datetime | 
    transaction_type = 'transaction_type_example' # str |  (optional)
    segment_type = 'segment_type_example' # str |  (optional)

    try:
        # Fetch refund amount of campaigns by Campaign
        api_response = api_instance.sum_transactions(start_date, end_date, transaction_type=transaction_type, segment_type=segment_type)
        print("The response of AnalyticsApi->sum_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->sum_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **transaction_type** | **str**|  | [optional] 
 **segment_type** | **str**|  | [optional] 

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

