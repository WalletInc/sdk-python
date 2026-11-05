# WTMenuItemCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_restriction** | [**WTAgeRestriction**](WTAgeRestriction.md) |  | [optional] 
**id_check_on_handoff** | **object** |  | [optional] 
**is_sold_out** | **object** |  | [optional] 
**sold_out_until** | **object** |  | [optional] 
**fulfillment_modes** | **object** |  | [optional] 
**title** | **object** |  | 
**description** | **object** |  | [optional] 
**media_url** | **object** |  | [optional] 
**price_amount** | **object** |  | 
**currency** | **object** |  | [optional] 
**tax_category** | [**WTMenuTaxCategory**](WTMenuTaxCategory.md) |  | [optional] 
**dietary_tags** | **object** |  | [optional] 
**allergens** | **object** |  | [optional] 
**prep_minutes** | **object** |  | [optional] 
**option_group_ids** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_menu_item_create_params import WTMenuItemCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuItemCreateParams from a JSON string
wt_menu_item_create_params_instance = WTMenuItemCreateParams.from_json(json)
# print the JSON string representation of the object
print WTMenuItemCreateParams.to_json()

# convert the object into a dict
wt_menu_item_create_params_dict = wt_menu_item_create_params_instance.to_dict()
# create an instance of WTMenuItemCreateParams from a dict
wt_menu_item_create_params_form_dict = wt_menu_item_create_params.from_dict(wt_menu_item_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


