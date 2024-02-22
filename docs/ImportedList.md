# ImportedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | 
**is_active** | **bool** |  | 
**list_name** | **str** |  | 
**phone_number_id** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wallet.models.imported_list import ImportedList

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedList from a JSON string
imported_list_instance = ImportedList.from_json(json)
# print the JSON string representation of the object
print ImportedList.to_json()

# convert the object into a dict
imported_list_dict = imported_list_instance.to_dict()
# create an instance of ImportedList from a dict
imported_list_form_dict = imported_list.from_dict(imported_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


