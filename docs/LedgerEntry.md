# LedgerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_id** | **str** |  | 
**register_type** | [**ApplicableTerminals**](ApplicableTerminals.md) |  | 
**transaction_id** | **str** |  | 
**transaction_type** | [**LedgerEntryTransactionType**](LedgerEntryTransactionType.md) |  | 
**check_amount** | **float** |  | 
**transaction_amount** | **float** |  | 
**check_balance** | **float** |  | 
**discount_received** | **str** |  | 
**payment_object_prefix** | **str** |  | 
**payment_object_id** | **str** |  | 
**parent_object_prefix** | **str** |  | 
**parent_object_id** | [**LedgerEntryParentObjectID**](LedgerEntryParentObjectID.md) |  | 
**meta_value** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**refunded_ledger_entry_id** | **str** |  | [optional] 
**transaction_amount_decimal** | **str** |  | 
**transaction_amount_string** | **str** |  | 
**check_amount_decimal** | **str** |  | 
**check_amount_string** | **str** |  | 
**check_balance_decimal** | **str** |  | 
**check_balance_string** | **str** |  | 

## Example

```python
from wallet.models.ledger_entry import LedgerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerEntry from a JSON string
ledger_entry_instance = LedgerEntry.from_json(json)
# print the JSON string representation of the object
print LedgerEntry.to_json()

# convert the object into a dict
ledger_entry_dict = ledger_entry_instance.to_dict()
# create an instance of LedgerEntry from a dict
ledger_entry_form_dict = ledger_entry.from_dict(ledger_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


