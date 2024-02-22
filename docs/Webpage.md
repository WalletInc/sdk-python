# Webpage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**category** | **str** |  | 
**admin_page** | **str** |  | 
**display_name** | **str** |  | 
**system_name** | **str** |  | 
**is_public** | **bool** |  | 
**order_number** | **float** |  | 
**icons** | **List[str]** |  | 

## Example

```python
from wallet.models.webpage import Webpage

# TODO update the JSON string below
json = "{}"
# create an instance of Webpage from a JSON string
webpage_instance = Webpage.from_json(json)
# print the JSON string representation of the object
print Webpage.to_json()

# convert the object into a dict
webpage_dict = webpage_instance.to_dict()
# create an instance of Webpage from a dict
webpage_form_dict = webpage.from_dict(webpage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


