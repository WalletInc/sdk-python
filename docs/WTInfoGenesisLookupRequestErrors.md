# WTInfoGenesisLookupRequestErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_time** | **datetime** |  | 
**end_date_time** | **datetime** |  | 
**selected_registers** | **List[str]** |  | [optional] 
**routing_ids** | **List[str]** |  | [optional] 

## Example

```python
from wallet.models.wt_info_genesis_lookup_request_errors import WTInfoGenesisLookupRequestErrors

# TODO update the JSON string below
json = "{}"
# create an instance of WTInfoGenesisLookupRequestErrors from a JSON string
wt_info_genesis_lookup_request_errors_instance = WTInfoGenesisLookupRequestErrors.from_json(json)
# print the JSON string representation of the object
print WTInfoGenesisLookupRequestErrors.to_json()

# convert the object into a dict
wt_info_genesis_lookup_request_errors_dict = wt_info_genesis_lookup_request_errors_instance.to_dict()
# create an instance of WTInfoGenesisLookupRequestErrors from a dict
wt_info_genesis_lookup_request_errors_form_dict = wt_info_genesis_lookup_request_errors.from_dict(wt_info_genesis_lookup_request_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


