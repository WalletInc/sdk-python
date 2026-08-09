# A2PBillingConsent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **object** |  | 
**accepted_at** | **object** |  | 
**text** | **object** |  | 

## Example

```python
from wallet.models.a2_p_billing_consent import A2PBillingConsent

# TODO update the JSON string below
json = "{}"
# create an instance of A2PBillingConsent from a JSON string
a2_p_billing_consent_instance = A2PBillingConsent.from_json(json)
# print the JSON string representation of the object
print A2PBillingConsent.to_json()

# convert the object into a dict
a2_p_billing_consent_dict = a2_p_billing_consent_instance.to_dict()
# create an instance of A2PBillingConsent from a dict
a2_p_billing_consent_form_dict = a2_p_billing_consent.from_dict(a2_p_billing_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


