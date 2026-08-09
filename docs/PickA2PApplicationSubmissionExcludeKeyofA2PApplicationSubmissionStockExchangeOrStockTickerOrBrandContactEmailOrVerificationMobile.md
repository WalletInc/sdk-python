# PickA2PApplicationSubmissionExcludeKeyofA2PApplicationSubmissionStockExchangeOrStockTickerOrBrandContactEmailOrVerificationMobile

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**business_classification** | [**BusinessClassification**](BusinessClassification.md) |  | 
**business_industry** | [**BusinessIndustry**](BusinessIndustry.md) |  | 
**tax_id_type** | [**BusinessRegistrationIdentifier**](BusinessRegistrationIdentifier.md) |  | 
**tax_id** | **str** |  | 
**website_url** | **str** |  | 
**social_media_url** | **str** |  | 
**regions_of_operation** | [**List[BusinessRegionsOfOperation]**](BusinessRegionsOfOperation.md) |  | 
**messaging_volume_high** | **bool** |  | 
**job_title** | **str** |  | 
**job_position** | [**JobPosition**](JobPosition.md) |  | 
**billing_consent** | [**A2PBillingConsent**](A2PBillingConsent.md) |  | [optional] 
**business_name** | **str** |  | 
**business_type** | [**BusinessType**](BusinessType.md) |  | 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**city** | **str** |  | 
**state** | **str** |  | 
**postal_code** | **str** |  | 
**country** | **str** |  | 
**phone_number** | **str** |  | 
**is_twilio_terms_read** | **bool** |  | 
**is_wallet_sms_terms_read** | **bool** |  | 
**is_pricing_understood** | **bool** |  | 
**is_privacy_and_tos_present** | **bool** |  | 
**privacy_policy_url** | **str** |  | [optional] 
**will_obtain_consent** | **bool** |  | 
**will_honor_opt_out** | **bool** |  | 
**will_follow_content_rules** | **bool** |  | 
**will_comply_law_and_hours** | **bool** |  | 
**info_is_accurate** | **bool** |  | 

## Example

```python
from wallet.models.pick_a2_p_application_submission_exclude_keyof_a2_p_application_submission_stock_exchange_or_stock_ticker_or_brand_contact_email_or_verification_mobile import PickA2PApplicationSubmissionExcludeKeyofA2PApplicationSubmissionStockExchangeOrStockTickerOrBrandContactEmailOrVerificationMobile

# TODO update the JSON string below
json = "{}"
# create an instance of PickA2PApplicationSubmissionExcludeKeyofA2PApplicationSubmissionStockExchangeOrStockTickerOrBrandContactEmailOrVerificationMobile from a JSON string
pick_a2_p_application_submission_exclude_keyof_a2_p_application_submission_stock_exchange_or_stock_ticker_or_brand_contact_email_or_verification_mobile_instance = PickA2PApplicationSubmissionExcludeKeyofA2PApplicationSubmissionStockExchangeOrStockTickerOrBrandContactEmailOrVerificationMobile.from_json(json)
# print the JSON string representation of the object
print PickA2PApplicationSubmissionExcludeKeyofA2PApplicationSubmissionStockExchangeOrStockTickerOrBrandContactEmailOrVerificationMobile.to_json()

# convert the object into a dict
pick_a2_p_application_submission_exclude_keyof_a2_p_application_submission_stock_exchange_or_stock_ticker_or_brand_contact_email_or_verification_mobile_dict = pick_a2_p_application_submission_exclude_keyof_a2_p_application_submission_stock_exchange_or_stock_ticker_or_brand_contact_email_or_verification_mobile_instance.to_dict()
# create an instance of PickA2PApplicationSubmissionExcludeKeyofA2PApplicationSubmissionStockExchangeOrStockTickerOrBrandContactEmailOrVerificationMobile from a dict
pick_a2_p_application_submission_exclude_keyof_a2_p_application_submission_stock_exchange_or_stock_ticker_or_brand_contact_email_or_verification_mobile_form_dict = pick_a2_p_application_submission_exclude_keyof_a2_p_application_submission_stock_exchange_or_stock_ticker_or_brand_contact_email_or_verification_mobile.from_dict(pick_a2_p_application_submission_exclude_keyof_a2_p_application_submission_stock_exchange_or_stock_ticker_or_brand_contact_email_or_verification_mobile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


