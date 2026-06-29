# VirtualBusinessCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **object** |  | 
**last_name** | **object** |  | 
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
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.virtual_business_card import VirtualBusinessCard

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualBusinessCard from a JSON string
virtual_business_card_instance = VirtualBusinessCard.from_json(json)
# print the JSON string representation of the object
print VirtualBusinessCard.to_json()

# convert the object into a dict
virtual_business_card_dict = virtual_business_card_instance.to_dict()
# create an instance of VirtualBusinessCard from a dict
virtual_business_card_form_dict = virtual_business_card.from_dict(virtual_business_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


