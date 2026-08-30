# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**merchant_id** | **str** |  | 
**member_id** | **object** |  | [optional] 
**mobile_number** | **object** |  | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**currency** | **object** |  | 
**amount_total** | **object** |  | 
**stripe_checkout_session_id** | **object** |  | [optional] 
**stripe_payment_intent_id** | **object** |  | [optional] 
**stripe_charge_id** | **object** |  | [optional] 
**receipt_url** | **object** |  | [optional] 
**acquisition_source** | **object** |  | [optional] 
**share_id** | **object** |  | [optional] 
**donor_note** | **object** |  | [optional] 
**line_items** | **object** |  | 

## Example

```python
from wallet.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print Order.to_json()

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_form_dict = order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


