# WTShareActivityRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **object** |  | 
**shares** | **object** |  | 
**clicks** | **object** |  | 
**new_visitors** | **object** |  | 
**new_visitors_per_share** | **object** |  | 

## Example

```python
from wallet.models.wt_share_activity_row import WTShareActivityRow

# TODO update the JSON string below
json = "{}"
# create an instance of WTShareActivityRow from a JSON string
wt_share_activity_row_instance = WTShareActivityRow.from_json(json)
# print the JSON string representation of the object
print WTShareActivityRow.to_json()

# convert the object into a dict
wt_share_activity_row_dict = wt_share_activity_row_instance.to_dict()
# create an instance of WTShareActivityRow from a dict
wt_share_activity_row_form_dict = wt_share_activity_row.from_dict(wt_share_activity_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


