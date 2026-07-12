# WTGiftCardPurchaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_cents** | **object** |  | 
**recipient_phone_number** | **object** |  | [optional] 
**recipient_email_address** | **object** |  | [optional] 
**recipient_member_id** | **object** |  | [optional] 
**pin_number** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_gift_card_purchase_request import WTGiftCardPurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTGiftCardPurchaseRequest from a JSON string
wt_gift_card_purchase_request_instance = WTGiftCardPurchaseRequest.from_json(json)
# print the JSON string representation of the object
print WTGiftCardPurchaseRequest.to_json()

# convert the object into a dict
wt_gift_card_purchase_request_dict = wt_gift_card_purchase_request_instance.to_dict()
# create an instance of WTGiftCardPurchaseRequest from a dict
wt_gift_card_purchase_request_form_dict = wt_gift_card_purchase_request.from_dict(wt_gift_card_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


