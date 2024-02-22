# WTEmailSubscriberUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email_address** | **str** |  | 

## Example

```python
from wallet.models.wt_email_subscriber_update_params import WTEmailSubscriberUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmailSubscriberUpdateParams from a JSON string
wt_email_subscriber_update_params_instance = WTEmailSubscriberUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTEmailSubscriberUpdateParams.to_json()

# convert the object into a dict
wt_email_subscriber_update_params_dict = wt_email_subscriber_update_params_instance.to_dict()
# create an instance of WTEmailSubscriberUpdateParams from a dict
wt_email_subscriber_update_params_form_dict = wt_email_subscriber_update_params.from_dict(wt_email_subscriber_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


