# WTConnectRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currently_due** | **object** |  | 
**past_due** | **object** |  | 
**eventually_due** | **object** |  | 
**pending_verification** | **object** |  | 
**disabled_reason** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_connect_requirements import WTConnectRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of WTConnectRequirements from a JSON string
wt_connect_requirements_instance = WTConnectRequirements.from_json(json)
# print the JSON string representation of the object
print WTConnectRequirements.to_json()

# convert the object into a dict
wt_connect_requirements_dict = wt_connect_requirements_instance.to_dict()
# create an instance of WTConnectRequirements from a dict
wt_connect_requirements_form_dict = wt_connect_requirements.from_dict(wt_connect_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


