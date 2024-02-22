# WTAdvertisementCreditScan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
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
**redeemed_amount_decimal** | **str** |  | 
**redeemed_amount_string** | **str** |  | 
**authorized_amount_decimal** | **str** |  | 
**authorized_amount_string** | **str** |  | 
**date_time_redeemed** | **datetime** |  | 
**date_time_refunded** | **datetime** |  | 

## Example

```python
from wallet.models.wt_advertisement_credit_scan import WTAdvertisementCreditScan

# TODO update the JSON string below
json = "{}"
# create an instance of WTAdvertisementCreditScan from a JSON string
wt_advertisement_credit_scan_instance = WTAdvertisementCreditScan.from_json(json)
# print the JSON string representation of the object
print WTAdvertisementCreditScan.to_json()

# convert the object into a dict
wt_advertisement_credit_scan_dict = wt_advertisement_credit_scan_instance.to_dict()
# create an instance of WTAdvertisementCreditScan from a dict
wt_advertisement_credit_scan_form_dict = wt_advertisement_credit_scan.from_dict(wt_advertisement_credit_scan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


