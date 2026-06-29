# WTDynamicVoucherRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_key** | **object** |  | 
**redeemed_amount** | **object** |  | 
**dynamic_voucher_id** | **str** |  | 
**redeemed_source** | **object** |  | 
**redeemed_transaction_id** | **object** |  | 
**transaction_type** | [**WTDynamicVoucherRedemptionTransactionType**](WTDynamicVoucherRedemptionTransactionType.md) |  | 
**register_id** | [**MSMemberRedemptionRegisterID**](MSMemberRedemptionRegisterID.md) |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**redeemed_at** | **object** |  | [optional] 
**refunded_at** | **object** |  | [optional] 
**refunded_transaction_id** | **object** |  | 
**refunded_amount** | **object** |  | 
**status** | [**VSDynamicVoucherStatus**](VSDynamicVoucherStatus.md) |  | 
**redeemed_amount_decimal** | **object** |  | 
**redeemed_amount_string** | **object** |  | 
**discount_received** | **object** |  | 
**meta_value** | **object** |  | 
**parent_object_id** | **str** |  | 

## Example

```python
from wallet.models.wt_dynamic_voucher_redemption import WTDynamicVoucherRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of WTDynamicVoucherRedemption from a JSON string
wt_dynamic_voucher_redemption_instance = WTDynamicVoucherRedemption.from_json(json)
# print the JSON string representation of the object
print WTDynamicVoucherRedemption.to_json()

# convert the object into a dict
wt_dynamic_voucher_redemption_dict = wt_dynamic_voucher_redemption_instance.to_dict()
# create an instance of WTDynamicVoucherRedemption from a dict
wt_dynamic_voucher_redemption_form_dict = wt_dynamic_voucher_redemption.from_dict(wt_dynamic_voucher_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


