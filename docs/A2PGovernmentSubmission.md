# A2PGovernmentSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **object** |  | 
**last_name** | **object** |  | 
**email** | **object** |  | 
**business_classification** | [**BusinessClassificationGovernment**](BusinessClassificationGovernment.md) |  | 
**business_industry** | [**BusinessIndustryGOVERNMENT**](BusinessIndustryGOVERNMENT.md) |  | 
**tax_id_type** | [**BusinessRegistrationIdentifier**](BusinessRegistrationIdentifier.md) |  | 
**tax_id** | **object** |  | 
**website_url** | **object** |  | 
**social_media_url** | **object** |  | 
**regions_of_operation** | **object** |  | 
**messaging_volume_high** | **object** |  | 
**job_title** | **object** |  | 
**job_position** | [**JobPosition**](JobPosition.md) |  | 
**business_name** | **object** |  | 
**business_type** | [**BusinessTypeNonProfit**](BusinessTypeNonProfit.md) |  | 
**address1** | **object** |  | 
**address2** | **object** |  | [optional] 
**city** | **object** |  | 
**state** | **object** |  | 
**postal_code** | **object** |  | 
**country** | **object** |  | 
**phone_number** | **object** |  | 
**is_twilio_terms_read** | **object** |  | 
**is_privacy_policy_on_website** | **object** |  | 
**is_tos_on_website** | **object** |  | 
**is_stop_understood** | **object** |  | 
**is_manual_read** | **object** |  | 
**is_ctia_short_code_read** | **object** |  | 
**is_standards_understood** | **object** |  | 
**is_short_code_understood** | **object** |  | 
**is_opt_in_out_understood** | **object** |  | 
**is_short_code_transfer_understood** | **object** |  | 
**is_pricing_understood** | **object** |  | 
**is_short_code_timeline_understood** | **object** |  | 

## Example

```python
from wallet.models.a2_p_government_submission import A2PGovernmentSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of A2PGovernmentSubmission from a JSON string
a2_p_government_submission_instance = A2PGovernmentSubmission.from_json(json)
# print the JSON string representation of the object
print A2PGovernmentSubmission.to_json()

# convert the object into a dict
a2_p_government_submission_dict = a2_p_government_submission_instance.to_dict()
# create an instance of A2PGovernmentSubmission from a dict
a2_p_government_submission_form_dict = a2_p_government_submission.from_dict(a2_p_government_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


