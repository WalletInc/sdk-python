# WTInfoGenesisRecordFilterParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_time** | **datetime** |  | 
**end_date_time** | **datetime** |  | 
**selected_registers** | **List[str]** |  | [optional] 

## Example

```python
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters

# TODO update the JSON string below
json = "{}"
# create an instance of WTInfoGenesisRecordFilterParameters from a JSON string
wt_info_genesis_record_filter_parameters_instance = WTInfoGenesisRecordFilterParameters.from_json(json)
# print the JSON string representation of the object
print WTInfoGenesisRecordFilterParameters.to_json()

# convert the object into a dict
wt_info_genesis_record_filter_parameters_dict = wt_info_genesis_record_filter_parameters_instance.to_dict()
# create an instance of WTInfoGenesisRecordFilterParameters from a dict
wt_info_genesis_record_filter_parameters_form_dict = wt_info_genesis_record_filter_parameters.from_dict(wt_info_genesis_record_filter_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


