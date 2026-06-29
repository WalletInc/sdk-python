# WTMessageInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from wallet.models.wt_message_instance import WTMessageInstance

# TODO update the JSON string below
json = "{}"
# create an instance of WTMessageInstance from a JSON string
wt_message_instance_instance = WTMessageInstance.from_json(json)
# print the JSON string representation of the object
print WTMessageInstance.to_json()

# convert the object into a dict
wt_message_instance_dict = wt_message_instance_instance.to_dict()
# create an instance of WTMessageInstance from a dict
wt_message_instance_form_dict = wt_message_instance.from_dict(wt_message_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


