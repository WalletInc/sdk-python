# WTLeadFiConsumerProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **object** |  | [optional] 
**phones** | **object** |  | 
**address** | [**WTLeadFiConsumerProfileAddress**](WTLeadFiConsumerProfileAddress.md) |  | [optional] 
**income** | [**WTLeadFiConsumerProfileIncome**](WTLeadFiConsumerProfileIncome.md) |  | [optional] 
**assets** | [**WTLeadFiConsumerProfileAssets**](WTLeadFiConsumerProfileAssets.md) |  | [optional] 

## Example

```python
from wallet.models.wt_lead_fi_consumer_profile import WTLeadFiConsumerProfile

# TODO update the JSON string below
json = "{}"
# create an instance of WTLeadFiConsumerProfile from a JSON string
wt_lead_fi_consumer_profile_instance = WTLeadFiConsumerProfile.from_json(json)
# print the JSON string representation of the object
print WTLeadFiConsumerProfile.to_json()

# convert the object into a dict
wt_lead_fi_consumer_profile_dict = wt_lead_fi_consumer_profile_instance.to_dict()
# create an instance of WTLeadFiConsumerProfile from a dict
wt_lead_fi_consumer_profile_form_dict = wt_lead_fi_consumer_profile.from_dict(wt_lead_fi_consumer_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


