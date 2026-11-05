# WTEarlyOptInImportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dry_run** | **object** |  | 
**is_registration_approved** | **object** |  | 
**opt_in_list_id** | **object** |  | [optional] 
**phone_number_id** | **object** |  | [optional] 
**total_count** | **object** |  | 
**bring_over_count** | **object** |  | 
**welcome_count** | **object** |  | 
**confirmation_count** | **object** |  | 
**skipped_count** | **object** |  | 
**skipped** | **object** |  | 
**not_eligible_count** | **object** |  | 
**is_opt_out_checked** | **object** |  | 
**texts_scheduled_at** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_early_opt_in_import_result import WTEarlyOptInImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTEarlyOptInImportResult from a JSON string
wt_early_opt_in_import_result_instance = WTEarlyOptInImportResult.from_json(json)
# print the JSON string representation of the object
print WTEarlyOptInImportResult.to_json()

# convert the object into a dict
wt_early_opt_in_import_result_dict = wt_early_opt_in_import_result_instance.to_dict()
# create an instance of WTEarlyOptInImportResult from a dict
wt_early_opt_in_import_result_form_dict = wt_early_opt_in_import_result.from_dict(wt_early_opt_in_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


