# WTAutoResponderCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** |  | 
**keyword** | **object** |  | 
**response_body** | **object** |  | 
**media_urls** | **object** |  | 

## Example

```python
from wallet.models.wt_auto_responder_create_params import WTAutoResponderCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTAutoResponderCreateParams from a JSON string
wt_auto_responder_create_params_instance = WTAutoResponderCreateParams.from_json(json)
# print the JSON string representation of the object
print WTAutoResponderCreateParams.to_json()

# convert the object into a dict
wt_auto_responder_create_params_dict = wt_auto_responder_create_params_instance.to_dict()
# create an instance of WTAutoResponderCreateParams from a dict
wt_auto_responder_create_params_form_dict = wt_auto_responder_create_params.from_dict(wt_auto_responder_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


