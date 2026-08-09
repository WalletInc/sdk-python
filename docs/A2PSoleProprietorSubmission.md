# A2PSoleProprietorSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **object** |  | 
**last_name** | **object** |  | 
**email** | **object** |  | 
**billing_consent** | [**A2PBillingConsent**](A2PBillingConsent.md) |  | [optional] 
**business_name** | **object** |  | 
**business_type** | [**BusinessTypeSoleProprietorship**](BusinessTypeSoleProprietorship.md) |  | 
**address1** | **object** |  | 
**address2** | **object** |  | [optional] 
**city** | **object** |  | 
**state** | **object** |  | 
**postal_code** | **object** |  | 
**country** | **object** |  | 
**phone_number** | **object** |  | 
**is_twilio_terms_read** | **object** |  | 
**is_wallet_sms_terms_read** | **object** |  | 
**is_pricing_understood** | **object** |  | 
**is_privacy_and_tos_present** | **object** |  | 
**privacy_policy_url** | **object** |  | [optional] 
**will_obtain_consent** | **object** |  | 
**will_honor_opt_out** | **object** |  | 
**will_follow_content_rules** | **object** |  | 
**will_comply_law_and_hours** | **object** |  | 
**info_is_accurate** | **object** |  | 
**verification_mobile** | **str** |  | 

## Example

```python
from wallet.models.a2_p_sole_proprietor_submission import A2PSoleProprietorSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of A2PSoleProprietorSubmission from a JSON string
a2_p_sole_proprietor_submission_instance = A2PSoleProprietorSubmission.from_json(json)
# print the JSON string representation of the object
print A2PSoleProprietorSubmission.to_json()

# convert the object into a dict
a2_p_sole_proprietor_submission_dict = a2_p_sole_proprietor_submission_instance.to_dict()
# create an instance of A2PSoleProprietorSubmission from a dict
a2_p_sole_proprietor_submission_form_dict = a2_p_sole_proprietor_submission.from_dict(a2_p_sole_proprietor_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


