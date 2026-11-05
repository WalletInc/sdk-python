# WTEarlyOptInCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **object** |  | 
**last_joined_at** | **object** |  | [optional] 
**ready_count** | **object** |  | 
**needs_confirmation_count** | **object** |  | 

## Example

```python
from wallet.models.wt_early_opt_in_count import WTEarlyOptInCount

# TODO update the JSON string below
json = "{}"
# create an instance of WTEarlyOptInCount from a JSON string
wt_early_opt_in_count_instance = WTEarlyOptInCount.from_json(json)
# print the JSON string representation of the object
print WTEarlyOptInCount.to_json()

# convert the object into a dict
wt_early_opt_in_count_dict = wt_early_opt_in_count_instance.to_dict()
# create an instance of WTEarlyOptInCount from a dict
wt_early_opt_in_count_form_dict = wt_early_opt_in_count.from_dict(wt_early_opt_in_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


