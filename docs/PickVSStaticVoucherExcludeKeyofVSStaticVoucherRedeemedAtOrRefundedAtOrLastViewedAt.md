# PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAt

From T, pick a set of properties whose keys are in the union K

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_active** | **bool** |  | 
**campaign_id** | [**NanoID**](NanoID.md) |  | 
**offer_amount_cents** | **int** |  | 
**order_number** | **int** |  | 
**transaction_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The type of the transaction - only redemption at the moment | 
**register_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The ID of the register where the transaction occurred | 
**redeemed_source** | **str** |  | 
**redeemed_transaction_id** | **str** |  | 
**redeemed_amount** | **int** |  | 
**is_redeemed** | **bool** |  | 
**refunded_transaction_id** | **str** |  | 
**refunded_amount** | **int** |  | 
**status** | [**Status**](Status.md) |  | 
**authorized_against_check_number** | **str** |  | 
**authorized_amount** | **int** |  | 
**merchant_id** | [**MerchantID**](MerchantID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**member_id** | **str** |  | [optional] 
**cell_phone_number** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


