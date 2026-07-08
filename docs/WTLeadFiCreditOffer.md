# WTLeadFiCreditOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**details** | **object** |  | [optional] 
**status** | **object** |  | [optional] 
**amount** | **object** |  | [optional] 
**contingencies** | **object** |  | [optional] 
**debt_to_income** | **object** |  | [optional] 
**monthly_payments** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_lead_fi_credit_offer import WTLeadFiCreditOffer

# TODO update the JSON string below
json = "{}"
# create an instance of WTLeadFiCreditOffer from a JSON string
wt_lead_fi_credit_offer_instance = WTLeadFiCreditOffer.from_json(json)
# print the JSON string representation of the object
print WTLeadFiCreditOffer.to_json()

# convert the object into a dict
wt_lead_fi_credit_offer_dict = wt_lead_fi_credit_offer_instance.to_dict()
# create an instance of WTLeadFiCreditOffer from a dict
wt_lead_fi_credit_offer_form_dict = wt_lead_fi_credit_offer.from_dict(wt_lead_fi_credit_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


