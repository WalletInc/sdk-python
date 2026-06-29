# OAIAssistantUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**description** | **str** |  | [optional] 
**instructions** | **object** |  | 
**tools** | **object** |  | [optional] 
**tool_resources** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**temperature** | **str** |  | 
**top_p** | **str** |  | 
**response_format** | **str** |  | [optional] 

## Example

```python
from wallet.models.oai_assistant_update_params import OAIAssistantUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of OAIAssistantUpdateParams from a JSON string
oai_assistant_update_params_instance = OAIAssistantUpdateParams.from_json(json)
# print the JSON string representation of the object
print OAIAssistantUpdateParams.to_json()

# convert the object into a dict
oai_assistant_update_params_dict = oai_assistant_update_params_instance.to_dict()
# create an instance of OAIAssistantUpdateParams from a dict
oai_assistant_update_params_form_dict = oai_assistant_update_params.from_dict(oai_assistant_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


