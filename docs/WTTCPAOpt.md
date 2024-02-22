# WTTCPAOpt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | [**WTTCPAOptListID**](WTTCPAOptListID.md) |  | 
**source_id** | [**WTTCPAOptSourceID**](WTTCPAOptSourceID.md) |  | 
**phone_number** | **str** |  | 

## Example

```python
from wallet.models.wttcpa_opt import WTTCPAOpt

# TODO update the JSON string below
json = "{}"
# create an instance of WTTCPAOpt from a JSON string
wttcpa_opt_instance = WTTCPAOpt.from_json(json)
# print the JSON string representation of the object
print WTTCPAOpt.to_json()

# convert the object into a dict
wttcpa_opt_dict = wttcpa_opt_instance.to_dict()
# create an instance of WTTCPAOpt from a dict
wttcpa_opt_form_dict = wttcpa_opt.from_dict(wttcpa_opt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


