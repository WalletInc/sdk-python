# A2PApplicationSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_twilio_terms_read** | **bool** |  | 
**is_privacy_policy_on_website** | **bool** |  | 
**is_tos_on_website** | **bool** |  | 
**is_stop_understood** | **bool** |  | 
**is_manual_read** | **bool** |  | 
**is_ctia_short_code_read** | **bool** |  | 
**is_standards_understood** | **bool** |  | 
**is_short_code_understood** | **bool** |  | 
**is_opt_in_out_understood** | **bool** |  | 
**is_short_code_transfer_understood** | **bool** |  | 
**is_pricing_understood** | **bool** |  | 
**is_short_code_timeline_understood** | **bool** |  | 
**business_name** | **str** |  | 
**business_type** | [**BusinessType**](BusinessType.md) |  | 
**business_classification** | [**BusinessClassification**](BusinessClassification.md) |  | 
**business_industry** | [**BusinessIndustry**](BusinessIndustry.md) |  | 
**tax_id_type** | [**BusinessRegistrationIdentifier**](BusinessRegistrationIdentifier.md) |  | 
**tax_id** | **str** |  | 
**website_url** | **str** |  | 
**social_media_url** | **str** |  | 
**regions_of_operation** | [**List[BusinessRegionsOfOperation]**](BusinessRegionsOfOperation.md) |  | 
**stock_exchange** | [**BusinessStockExchanges**](BusinessStockExchanges.md) |  | [optional] 
**stock_ticker** | **str** |  | [optional] 
**messaging_volume_high** | **bool** |  | 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**city** | **str** |  | 
**state** | **str** |  | 
**postal_code** | **str** |  | 
**country** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**job_title** | **str** |  | 
**job_position** | [**JobPosition**](JobPosition.md) |  | 
**phone_number** | **str** |  | 

## Example

```python
from wallet.models.a2_p_application_submission import A2PApplicationSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of A2PApplicationSubmission from a JSON string
a2_p_application_submission_instance = A2PApplicationSubmission.from_json(json)
# print the JSON string representation of the object
print A2PApplicationSubmission.to_json()

# convert the object into a dict
a2_p_application_submission_dict = a2_p_application_submission_instance.to_dict()
# create an instance of A2PApplicationSubmission from a dict
a2_p_application_submission_form_dict = a2_p_application_submission.from_dict(a2_p_application_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


