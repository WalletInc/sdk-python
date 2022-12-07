# WTMerchantCredit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PrefixedNanoID**](PrefixedNanoID.md) |  | 
**merchant_id** | [**MerchantID**](MerchantID.md) |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**updated_at** | **datetime** | The timestamp of when this resource was updated | 
**is_active** | **bool** | Denotes if this resource is active | 
**mobile_number** | **str** |  | 
**credit_amount** | **int** | The amount that needs to be credited to the member | 
**credit_amount_decimal** | **str** | The amount that needs to be credited to the member (fixed to 2 decimals) | 
**credit_amount_string** | **str** | The amount that needs to be credited to the member (in string) | 
**member_id** | **str** | MerchantCredit ID as represented by the merchant | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


