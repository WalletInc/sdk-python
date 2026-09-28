# WTAutoResponder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**phone_number_id** | **str** |  | 
**keyword** | **object** |  | 
**keyword_canonical** | **object** |  | 
**response_body** | **object** |  | 
**media_urls** | **object** |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.wt_auto_responder import WTAutoResponder

# TODO update the JSON string below
json = "{}"
# create an instance of WTAutoResponder from a JSON string
wt_auto_responder_instance = WTAutoResponder.from_json(json)
# print the JSON string representation of the object
print WTAutoResponder.to_json()

# convert the object into a dict
wt_auto_responder_dict = wt_auto_responder_instance.to_dict()
# create an instance of WTAutoResponder from a dict
wt_auto_responder_form_dict = wt_auto_responder.from_dict(wt_auto_responder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


