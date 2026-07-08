# WTFinancingSoftPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **object** |  | 
**last_name** | **object** |  | 
**phone_number** | **object** |  | 
**email** | **object** |  | 
**disclosure_text** | **object** |  | 

## Example

```python
from wallet.models.wt_financing_soft_pull_request import WTFinancingSoftPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTFinancingSoftPullRequest from a JSON string
wt_financing_soft_pull_request_instance = WTFinancingSoftPullRequest.from_json(json)
# print the JSON string representation of the object
print WTFinancingSoftPullRequest.to_json()

# convert the object into a dict
wt_financing_soft_pull_request_dict = wt_financing_soft_pull_request_instance.to_dict()
# create an instance of WTFinancingSoftPullRequest from a dict
wt_financing_soft_pull_request_form_dict = wt_financing_soft_pull_request.from_dict(wt_financing_soft_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


