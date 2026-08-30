# CSPViolationSummaryRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**violated_directive** | **str** |  | 
**blocked_host** | **object** | The scheme+host of the blocked URI, or the raw value for schemeless blocks (inline / eval / data:). | 
**disposition** | **object** | \&quot;enforce\&quot; (actually blocked) vs \&quot;report\&quot; (report-only twin). | 
**count** | **object** |  | 
**sample_document_uri** | **str** |  | 
**first_seen** | **datetime** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 

## Example

```python
from wallet.models.csp_violation_summary_row import CSPViolationSummaryRow

# TODO update the JSON string below
json = "{}"
# create an instance of CSPViolationSummaryRow from a JSON string
csp_violation_summary_row_instance = CSPViolationSummaryRow.from_json(json)
# print the JSON string representation of the object
print CSPViolationSummaryRow.to_json()

# convert the object into a dict
csp_violation_summary_row_dict = csp_violation_summary_row_instance.to_dict()
# create an instance of CSPViolationSummaryRow from a dict
csp_violation_summary_row_form_dict = csp_violation_summary_row.from_dict(csp_violation_summary_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


