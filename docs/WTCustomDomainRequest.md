# WTCustomDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **object** | A subdomain the merchant controls, such as &#x60;wallet.acme.com&#x60;. | 

## Example

```python
from wallet.models.wt_custom_domain_request import WTCustomDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTCustomDomainRequest from a JSON string
wt_custom_domain_request_instance = WTCustomDomainRequest.from_json(json)
# print the JSON string representation of the object
print WTCustomDomainRequest.to_json()

# convert the object into a dict
wt_custom_domain_request_dict = wt_custom_domain_request_instance.to_dict()
# create an instance of WTCustomDomainRequest from a dict
wt_custom_domain_request_form_dict = wt_custom_domain_request.from_dict(wt_custom_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


