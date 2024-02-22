# PickVSAdvertisementCreditScanExcludeKeyofVSAdvertisementCreditScanRedeemedAtOrRefundedAt

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_type** | [**PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtTransactionType**](PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtTransactionType.md) |  | 
**register_id** | [**PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID**](PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.md) |  | 
**redeemed_source** | **str** |  | 
**redeemed_transaction_id** | **str** |  | 
**redeemed_amount** | **int** |  | 
**is_redeemed** | **bool** |  | 
**refunded_transaction_id** | **str** |  | 
**refunded_amount** | **int** |  | 
**status** | [**Status**](Status.md) |  | 
**authorized_against_check_number** | **str** |  | 
**authorized_amount** | **int** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**advertisement_credit_id** | **str** |  | 

## Example

```python
from wallet.models.pick_vs_advertisement_credit_scan_exclude_keyof_vs_advertisement_credit_scan_redeemed_at_or_refunded_at import PickVSAdvertisementCreditScanExcludeKeyofVSAdvertisementCreditScanRedeemedAtOrRefundedAt

# TODO update the JSON string below
json = "{}"
# create an instance of PickVSAdvertisementCreditScanExcludeKeyofVSAdvertisementCreditScanRedeemedAtOrRefundedAt from a JSON string
pick_vs_advertisement_credit_scan_exclude_keyof_vs_advertisement_credit_scan_redeemed_at_or_refunded_at_instance = PickVSAdvertisementCreditScanExcludeKeyofVSAdvertisementCreditScanRedeemedAtOrRefundedAt.from_json(json)
# print the JSON string representation of the object
print PickVSAdvertisementCreditScanExcludeKeyofVSAdvertisementCreditScanRedeemedAtOrRefundedAt.to_json()

# convert the object into a dict
pick_vs_advertisement_credit_scan_exclude_keyof_vs_advertisement_credit_scan_redeemed_at_or_refunded_at_dict = pick_vs_advertisement_credit_scan_exclude_keyof_vs_advertisement_credit_scan_redeemed_at_or_refunded_at_instance.to_dict()
# create an instance of PickVSAdvertisementCreditScanExcludeKeyofVSAdvertisementCreditScanRedeemedAtOrRefundedAt from a dict
pick_vs_advertisement_credit_scan_exclude_keyof_vs_advertisement_credit_scan_redeemed_at_or_refunded_at_form_dict = pick_vs_advertisement_credit_scan_exclude_keyof_vs_advertisement_credit_scan_redeemed_at_or_refunded_at.from_dict(pick_vs_advertisement_credit_scan_exclude_keyof_vs_advertisement_credit_scan_redeemed_at_or_refunded_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


