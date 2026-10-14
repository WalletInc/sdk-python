# WTCustomDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **object** | The custom domain, or empty when none is set up. | 
**state** | [**WTCustomDomainState**](WTCustomDomainState.md) | Where the domain is in its setup. Absent when &#x60;hostname&#x60; is empty. | [optional] 
**managed** | **object** | False when Wallet set the domain up by hand. Such a domain is shown read-only and cannot be changed here. | 
**dns_target** | **object** | The CNAME target the merchant points their domain at. | 
**txt** | [**WTCustomDomainTXT**](WTCustomDomainTXT.md) | Present when the merchant must also add a TXT record. | [optional] 
**error** | [**WTCustomDomainError**](WTCustomDomainError.md) | Present when &#x60;state&#x60; is &#x60;error&#x60;. | [optional] 
**paused** | **object** | True when the domain is live but the merchant&#39;s plan no longer includes custom domains. Guests are redirected to the same page on wall.et until the merchant upgrades; nothing needs to be set up again. | [optional] 
**adoption** | [**WTCustomDomainAdoption**](WTCustomDomainAdoption.md) | Present while a domain Wallet set up by hand is being moved onto self-serve. The domain stays live throughout. | [optional] 
**certificate_txt** | [**WTCustomDomainTXT**](WTCustomDomainTXT.md) | Present while adopting: the TXT record that lets the certificate be issued before the domain is switched. | [optional] 

## Example

```python
from wallet.models.wt_custom_domain import WTCustomDomain

# TODO update the JSON string below
json = "{}"
# create an instance of WTCustomDomain from a JSON string
wt_custom_domain_instance = WTCustomDomain.from_json(json)
# print the JSON string representation of the object
print WTCustomDomain.to_json()

# convert the object into a dict
wt_custom_domain_dict = wt_custom_domain_instance.to_dict()
# create an instance of WTCustomDomain from a dict
wt_custom_domain_form_dict = wt_custom_domain.from_dict(wt_custom_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


