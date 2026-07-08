# WTLeadFiConsumerProfileIncome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**household** | **object** |  | [optional] 
**personal** | **object** |  | [optional] 
**estimate** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_lead_fi_consumer_profile_income import WTLeadFiConsumerProfileIncome

# TODO update the JSON string below
json = "{}"
# create an instance of WTLeadFiConsumerProfileIncome from a JSON string
wt_lead_fi_consumer_profile_income_instance = WTLeadFiConsumerProfileIncome.from_json(json)
# print the JSON string representation of the object
print WTLeadFiConsumerProfileIncome.to_json()

# convert the object into a dict
wt_lead_fi_consumer_profile_income_dict = wt_lead_fi_consumer_profile_income_instance.to_dict()
# create an instance of WTLeadFiConsumerProfileIncome from a dict
wt_lead_fi_consumer_profile_income_form_dict = wt_lead_fi_consumer_profile_income.from_dict(wt_lead_fi_consumer_profile_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


