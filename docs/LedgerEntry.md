# LedgerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_id** | **object** |  | 
**register_type** | [**ApplicableTerminals**](ApplicableTerminals.md) |  | 
**transaction_id** | **object** |  | 
**transaction_type** | [**LedgerEntryTransactionType**](LedgerEntryTransactionType.md) |  | 
**check_amount** | **object** |  | 
**transaction_amount** | **object** |  | 
**check_balance** | **object** |  | 
**discount_received** | **object** |  | 
**payment_object_prefix** | **object** |  | 
**payment_object_id** | **str** |  | 
**parent_object_prefix** | **object** |  | 
**parent_object_id** | [**LedgerEntryParentObjectID**](LedgerEntryParentObjectID.md) |  | 
**meta_value** | **object** |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**refunded_ledger_entry_id** | **str** |  | [optional] 
**transaction_amount_decimal** | **object** |  | 
**transaction_amount_string** | **object** |  | 
**check_amount_decimal** | **object** |  | 
**check_amount_string** | **object** |  | 
**check_balance_decimal** | **object** |  | 
**check_balance_string** | **object** |  | 

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


