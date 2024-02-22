# WTVirtualBusinessCardCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email_address** | **str** |  | 
**designation** | **str** |  | 
**phone_number** | **str** |  | 
**introduction** | **str** |  | [optional] 
**instagram** | **str** |  | [optional] 
**facebook** | **str** |  | [optional] 
**you_tube** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**linked_in** | **str** |  | [optional] 
**whats_app** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_virtual_business_card_create_params import WTVirtualBusinessCardCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTVirtualBusinessCardCreateParams from a JSON string
wt_virtual_business_card_create_params_instance = WTVirtualBusinessCardCreateParams.from_json(json)
# print the JSON string representation of the object
print WTVirtualBusinessCardCreateParams.to_json()

# convert the object into a dict
wt_virtual_business_card_create_params_dict = wt_virtual_business_card_create_params_instance.to_dict()
# create an instance of WTVirtualBusinessCardCreateParams from a dict
wt_virtual_business_card_create_params_form_dict = wt_virtual_business_card_create_params.from_dict(wt_virtual_business_card_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


