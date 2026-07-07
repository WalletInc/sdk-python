# WTFinancingSoftPullResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_record_id** | **object** |  | 
**qualification_tier** | **object** |  | [optional] 
**bureaus** | **object** |  | 
**result** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_financing_soft_pull_response import WTFinancingSoftPullResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTFinancingSoftPullResponse from a JSON string
wt_financing_soft_pull_response_instance = WTFinancingSoftPullResponse.from_json(json)
# print the JSON string representation of the object
print WTFinancingSoftPullResponse.to_json()

# convert the object into a dict
wt_financing_soft_pull_response_dict = wt_financing_soft_pull_response_instance.to_dict()
# create an instance of WTFinancingSoftPullResponse from a dict
wt_financing_soft_pull_response_form_dict = wt_financing_soft_pull_response.from_dict(wt_financing_soft_pull_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


