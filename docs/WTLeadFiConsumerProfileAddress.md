# WTLeadFiConsumerProfileAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **object** |  | [optional] 
**state** | **object** |  | [optional] 
**city** | **object** |  | [optional] 
**zip** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_lead_fi_consumer_profile_address import WTLeadFiConsumerProfileAddress

# TODO update the JSON string below
json = "{}"
# create an instance of WTLeadFiConsumerProfileAddress from a JSON string
wt_lead_fi_consumer_profile_address_instance = WTLeadFiConsumerProfileAddress.from_json(json)
# print the JSON string representation of the object
print WTLeadFiConsumerProfileAddress.to_json()

# convert the object into a dict
wt_lead_fi_consumer_profile_address_dict = wt_lead_fi_consumer_profile_address_instance.to_dict()
# create an instance of WTLeadFiConsumerProfileAddress from a dict
wt_lead_fi_consumer_profile_address_form_dict = wt_lead_fi_consumer_profile_address.from_dict(wt_lead_fi_consumer_profile_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


