# WTStaticVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**campaign_id** | **str** |  | 
**member_id** | **str** |  | [optional] 
**cell_phone_number** | **str** |  | [optional] 
**offer_amount_cents** | **int** |  | 
**order_number** | **int** |  | 
**transaction_type** | [**PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtTransactionType**](PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtTransactionType.md) |  | 
**register_id** | [**PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID**](PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.md) |  | 
**redeemed_source** | **str** |  | 
**redeemed_transaction_id** | **str** |  | 
**redeemed_amount** | **int** |  | 
**is_redeemed** | **bool** |  | 
**refunded_transaction_id** | **str** |  | 
**refunded_amount** | **int** |  | 
**status** | [**Status**](Status.md) |  | 
**customer_id** | **str** |  | [optional] 
**authorized_against_check_number** | **str** |  | 
**authorized_amount** | **int** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**authorized_amount_decimal** | **object** |  | 
**authorized_amount_string** | **object** |  | 
**offer_amount_cents_decimal** | **object** |  | 
**offer_amount_cents_string** | **object** |  | 
**redeemed_amount_decimal** | **object** |  | 
**redeemed_amount_string** | **object** |  | 
**date_time_redeemed** | **object** |  | [optional] 
**date_time_refunded** | **object** |  | [optional] 
**date_time_last_viewed** | **object** |  | [optional] 
**reason_invalid** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_static_voucher import WTStaticVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of WTStaticVoucher from a JSON string
wt_static_voucher_instance = WTStaticVoucher.from_json(json)
# print the JSON string representation of the object
print WTStaticVoucher.to_json()

# convert the object into a dict
wt_static_voucher_dict = wt_static_voucher_instance.to_dict()
# create an instance of WTStaticVoucher from a dict
wt_static_voucher_form_dict = wt_static_voucher.from_dict(wt_static_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


