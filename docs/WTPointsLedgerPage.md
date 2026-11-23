# WTPointsLedgerPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **object** |  | 
**length** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from wallet.models.wt_points_ledger_page import WTPointsLedgerPage

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsLedgerPage from a JSON string
wt_points_ledger_page_instance = WTPointsLedgerPage.from_json(json)
# print the JSON string representation of the object
print WTPointsLedgerPage.to_json()

# convert the object into a dict
wt_points_ledger_page_dict = wt_points_ledger_page_instance.to_dict()
# create an instance of WTPointsLedgerPage from a dict
wt_points_ledger_page_form_dict = wt_points_ledger_page.from_dict(wt_points_ledger_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


