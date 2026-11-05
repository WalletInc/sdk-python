# WTRelatedItemAdminRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WTRelatedItemType**](WTRelatedItemType.md) |  | 
**id** | **object** |  | 
**status** | [**WTRelatedItemStatus**](WTRelatedItemStatus.md) |  | 
**title** | **object** |  | [optional] 
**thumbnail_url** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_related_item_admin_ref import WTRelatedItemAdminRef

# TODO update the JSON string below
json = "{}"
# create an instance of WTRelatedItemAdminRef from a JSON string
wt_related_item_admin_ref_instance = WTRelatedItemAdminRef.from_json(json)
# print the JSON string representation of the object
print WTRelatedItemAdminRef.to_json()

# convert the object into a dict
wt_related_item_admin_ref_dict = wt_related_item_admin_ref_instance.to_dict()
# create an instance of WTRelatedItemAdminRef from a dict
wt_related_item_admin_ref_form_dict = wt_related_item_admin_ref.from_dict(wt_related_item_admin_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


