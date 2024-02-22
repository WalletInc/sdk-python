# FetchAllLedgerTransactions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[LedgerEntry]**](LedgerEntry.md) |  | 
**page_count** | **float** |  | 
**total_records** | **float** |  | 

## Example

```python
from wallet.models.fetch_all_ledger_transactions200_response import FetchAllLedgerTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchAllLedgerTransactions200Response from a JSON string
fetch_all_ledger_transactions200_response_instance = FetchAllLedgerTransactions200Response.from_json(json)
# print the JSON string representation of the object
print FetchAllLedgerTransactions200Response.to_json()

# convert the object into a dict
fetch_all_ledger_transactions200_response_dict = fetch_all_ledger_transactions200_response_instance.to_dict()
# create an instance of FetchAllLedgerTransactions200Response from a dict
fetch_all_ledger_transactions200_response_form_dict = fetch_all_ledger_transactions200_response.from_dict(fetch_all_ledger_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


