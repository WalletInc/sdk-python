# WTPassStyleResponseProviders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple** | [**WTPassStyleResponseProvidersApple**](WTPassStyleResponseProvidersApple.md) |  | 
**google** | [**WTPassStyleResponseProvidersApple**](WTPassStyleResponseProvidersApple.md) |  | 

## Example

```python
from wallet.models.wt_pass_style_response_providers import WTPassStyleResponseProviders

# TODO update the JSON string below
json = "{}"
# create an instance of WTPassStyleResponseProviders from a JSON string
wt_pass_style_response_providers_instance = WTPassStyleResponseProviders.from_json(json)
# print the JSON string representation of the object
print WTPassStyleResponseProviders.to_json()

# convert the object into a dict
wt_pass_style_response_providers_dict = wt_pass_style_response_providers_instance.to_dict()
# create an instance of WTPassStyleResponseProviders from a dict
wt_pass_style_response_providers_form_dict = wt_pass_style_response_providers.from_dict(wt_pass_style_response_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


