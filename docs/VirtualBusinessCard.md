# VirtualBusinessCard


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
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
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


