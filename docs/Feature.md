# Feature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_num** | **float** |  | 
**name** | **str** |  | 
**max_volume** | **str** |  | [optional] 
**measurement** | **str** |  | 
**description** | **str** |  | 
**current_volume** | **str** |  | [optional] 
**is_exceeded** | **bool** |  | [optional] 
**is_in_use** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 

## Example

```python
from wallet.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print Feature.to_json()

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_form_dict = feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


