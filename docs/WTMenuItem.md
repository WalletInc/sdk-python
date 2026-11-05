# WTMenuItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_restriction** | [**WTAgeRestriction**](WTAgeRestriction.md) |  | [optional] 
**id_check_on_handoff** | **object** |  | [optional] 
**is_sold_out** | **object** |  | [optional] 
**sold_out_until** | **object** |  | [optional] 
**fulfillment_modes** | **object** |  | [optional] 
**id** | **object** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**merchant_id** | **str** |  | 
**title** | **object** |  | 
**description** | **object** |  | 
**media_url** | **object** |  | 
**price_amount** | **object** |  | 
**currency** | **object** |  | 
**tax_category** | [**WTMenuTaxCategory**](WTMenuTaxCategory.md) |  | 
**dietary_tags** | **object** |  | 
**allergens** | **object** |  | 
**prep_minutes** | **object** |  | [optional] 
**option_group_ids** | **object** |  | 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.wt_menu_item import WTMenuItem

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuItem from a JSON string
wt_menu_item_instance = WTMenuItem.from_json(json)
# print the JSON string representation of the object
print WTMenuItem.to_json()

# convert the object into a dict
wt_menu_item_dict = wt_menu_item_instance.to_dict()
# create an instance of WTMenuItem from a dict
wt_menu_item_form_dict = wt_menu_item.from_dict(wt_menu_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


