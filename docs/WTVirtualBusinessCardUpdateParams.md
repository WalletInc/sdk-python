# WTVirtualBusinessCardUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email_address** | **object** |  | 
**designation** | **object** |  | 
**phone_number** | **object** |  | 
**introduction** | **object** |  | [optional] 
**instagram** | **object** |  | [optional] 
**facebook** | **object** |  | [optional] 
**you_tube** | **object** |  | [optional] 
**twitter** | **object** |  | [optional] 
**linked_in** | **object** |  | [optional] 
**whats_app** | **object** |  | [optional] 
**avatar_url** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_virtual_business_card_update_params import WTVirtualBusinessCardUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTVirtualBusinessCardUpdateParams from a JSON string
wt_virtual_business_card_update_params_instance = WTVirtualBusinessCardUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTVirtualBusinessCardUpdateParams.to_json()

# convert the object into a dict
wt_virtual_business_card_update_params_dict = wt_virtual_business_card_update_params_instance.to_dict()
# create an instance of WTVirtualBusinessCardUpdateParams from a dict
wt_virtual_business_card_update_params_form_dict = wt_virtual_business_card_update_params.from_dict(wt_virtual_business_card_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


