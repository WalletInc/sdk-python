# WTImportedList


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
from wallet.models.wt_imported_list import WTImportedList

# TODO update the JSON string below
json = "{}"
# create an instance of WTImportedList from a JSON string
wt_imported_list_instance = WTImportedList.from_json(json)
# print the JSON string representation of the object
print WTImportedList.to_json()

# convert the object into a dict
wt_imported_list_dict = wt_imported_list_instance.to_dict()
# create an instance of WTImportedList from a dict
wt_imported_list_form_dict = wt_imported_list.from_dict(wt_imported_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


