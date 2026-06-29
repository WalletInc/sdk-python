# Assistant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**description** | **object** |  | [optional] 
**instructions** | **object** |  | 
**tools** | **object** |  | [optional] 
**tool_resources** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 
**temperature** | **object** |  | 
**top_p** | **object** |  | 
**response_format** | **object** |  | [optional] 
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**assistant_id** | **object** |  | 
**is_active** | **object** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.assistant import Assistant

# TODO update the JSON string below
json = "{}"
# create an instance of Assistant from a JSON string
assistant_instance = Assistant.from_json(json)
# print the JSON string representation of the object
print Assistant.to_json()

# convert the object into a dict
assistant_dict = assistant_instance.to_dict()
# create an instance of Assistant from a dict
assistant_form_dict = assistant.from_dict(assistant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


