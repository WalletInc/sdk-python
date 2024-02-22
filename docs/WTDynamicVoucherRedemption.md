# WTDynamicVoucherRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_key** | **str** |  | 
**redeemed_amount** | **int** |  | 
**dynamic_voucher_id** | **str** |  | 
**redeemed_source** | **str** |  | 
**redeemed_transaction_id** | **str** |  | 
**transaction_type** | [**WTDynamicVoucherRedemptionTransactionType**](WTDynamicVoucherRedemptionTransactionType.md) |  | 
**register_id** | [**PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID**](PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.md) |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**redeemed_at** | **datetime** |  | [optional] 
**refunded_at** | **datetime** |  | [optional] 
**refunded_transaction_id** | **str** |  | 
**refunded_amount** | **int** |  | 
**status** | [**VSDynamicVoucherStatus**](VSDynamicVoucherStatus.md) |  | 
**redeemed_amount_decimal** | **str** |  | 
**redeemed_amount_string** | **str** |  | 
**discount_received** | **str** |  | 
**meta_value** | **str** |  | 
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


