# StaticVoucher


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
from wallet.models.static_voucher import StaticVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of StaticVoucher from a JSON string
static_voucher_instance = StaticVoucher.from_json(json)
# print the JSON string representation of the object
print StaticVoucher.to_json()

# convert the object into a dict
static_voucher_dict = static_voucher_instance.to_dict()
# create an instance of StaticVoucher from a dict
static_voucher_form_dict = static_voucher.from_dict(static_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


