# WTAutoResponderUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**keyword** | **object** |  | [optional] 
**response_body** | **object** |  | [optional] 
**media_urls** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_auto_responder_update_params import WTAutoResponderUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTAutoResponderUpdateParams from a JSON string
wt_auto_responder_update_params_instance = WTAutoResponderUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTAutoResponderUpdateParams.to_json()

# convert the object into a dict
wt_auto_responder_update_params_dict = wt_auto_responder_update_params_instance.to_dict()
# create an instance of WTAutoResponderUpdateParams from a dict
wt_auto_responder_update_params_form_dict = wt_auto_responder_update_params.from_dict(wt_auto_responder_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


