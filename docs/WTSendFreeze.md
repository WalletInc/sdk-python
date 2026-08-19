# WTSendFreeze


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **object** |  | 
**reason** | **object** |  | [optional] 
**frozen_by** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_send_freeze import WTSendFreeze

# TODO update the JSON string below
json = "{}"
# create an instance of WTSendFreeze from a JSON string
wt_send_freeze_instance = WTSendFreeze.from_json(json)
# print the JSON string representation of the object
print WTSendFreeze.to_json()

# convert the object into a dict
wt_send_freeze_dict = wt_send_freeze_instance.to_dict()
# create an instance of WTSendFreeze from a dict
wt_send_freeze_form_dict = wt_send_freeze.from_dict(wt_send_freeze_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


