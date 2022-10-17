# MSMerchantCreditRedemption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID at the POS | 
**transaction_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The type of the transaction - either redemption or refund | 
**amount** | **int** | The number of amount involved in this transaction | 
**terminal_type** | **str** | The type of the terminal | 
**id** | **str** | The UUID of this record | 
**merchant_credit_id** | [**NanoID**](NanoID.md) |  | 
**merchant_id** | [**MerchantID**](MerchantID.md) |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**is_active** | **bool** | Denotes if this resource is active | 
**register_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The ID of the register where the transaction occurred | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


