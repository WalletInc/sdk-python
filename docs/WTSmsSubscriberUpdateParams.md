# WTSmsSubscriberUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_number** | **str** |  | 

## Example

```python
from wallet.models.wt_sms_subscriber_update_params import WTSmsSubscriberUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTSmsSubscriberUpdateParams from a JSON string
wt_sms_subscriber_update_params_instance = WTSmsSubscriberUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTSmsSubscriberUpdateParams.to_json()

# convert the object into a dict
wt_sms_subscriber_update_params_dict = wt_sms_subscriber_update_params_instance.to_dict()
# create an instance of WTSmsSubscriberUpdateParams from a dict
wt_sms_subscriber_update_params_form_dict = wt_sms_subscriber_update_params.from_dict(wt_sms_subscriber_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


