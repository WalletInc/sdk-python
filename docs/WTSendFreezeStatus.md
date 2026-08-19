# WTSendFreezeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frozen** | **object** |  | 
**freezes** | **object** |  | 

## Example

```python
from wallet.models.wt_send_freeze_status import WTSendFreezeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WTSendFreezeStatus from a JSON string
wt_send_freeze_status_instance = WTSendFreezeStatus.from_json(json)
# print the JSON string representation of the object
print WTSendFreezeStatus.to_json()

# convert the object into a dict
wt_send_freeze_status_dict = wt_send_freeze_status_instance.to_dict()
# create an instance of WTSendFreezeStatus from a dict
wt_send_freeze_status_form_dict = wt_send_freeze_status.from_dict(wt_send_freeze_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


