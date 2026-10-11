# WTCustomDomainError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** |  | 
**message** | **object** |  | 
**help_url** | **object** | A help-centre guide for this problem. | 

## Example

```python
from wallet.models.wt_custom_domain_error import WTCustomDomainError

# TODO update the JSON string below
json = "{}"
# create an instance of WTCustomDomainError from a JSON string
wt_custom_domain_error_instance = WTCustomDomainError.from_json(json)
# print the JSON string representation of the object
print WTCustomDomainError.to_json()

# convert the object into a dict
wt_custom_domain_error_dict = wt_custom_domain_error_instance.to_dict()
# create an instance of WTCustomDomainError from a dict
wt_custom_domain_error_form_dict = wt_custom_domain_error.from_dict(wt_custom_domain_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


