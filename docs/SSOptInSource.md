# SSOptInSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**list_id** | **str** |  | 
**source_name** | **str** |  | 
**employee_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 

## Example

```python
from wallet.models.ss_opt_in_source import SSOptInSource

# TODO update the JSON string below
json = "{}"
# create an instance of SSOptInSource from a JSON string
ss_opt_in_source_instance = SSOptInSource.from_json(json)
# print the JSON string representation of the object
print SSOptInSource.to_json()

# convert the object into a dict
ss_opt_in_source_dict = ss_opt_in_source_instance.to_dict()
# create an instance of SSOptInSource from a dict
ss_opt_in_source_form_dict = ss_opt_in_source.from_dict(ss_opt_in_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


