# WTPointsLedgerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**entry_type** | [**WTPointsLedgerEntryType**](WTPointsLedgerEntryType.md) |  | 
**points** | **object** | Signed: positive adds to the balance, negative takes from it. | 
**source** | **str** |  | 
**source_label** | **object** | A plain-words label for &#x60;source&#x60;, ready to show. | 
**created_at** | **datetime** |  | 
**employee_name** | **object** |  | 
**reason** | **object** |  | 
**eligible_amount_cents** | **object** |  | 
**balance_after** | **object** | The balance after this entry. Present only when the membership service supplies it. | [optional] 

## Example

```python
from wallet.models.wt_points_ledger_entry import WTPointsLedgerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsLedgerEntry from a JSON string
wt_points_ledger_entry_instance = WTPointsLedgerEntry.from_json(json)
# print the JSON string representation of the object
print WTPointsLedgerEntry.to_json()

# convert the object into a dict
wt_points_ledger_entry_dict = wt_points_ledger_entry_instance.to_dict()
# create an instance of WTPointsLedgerEntry from a dict
wt_points_ledger_entry_form_dict = wt_points_ledger_entry.from_dict(wt_points_ledger_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


