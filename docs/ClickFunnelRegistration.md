# ClickFunnelRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**ClickFunnelContact**](ClickFunnelContact.md) |  | 
**event** | **str** |  | 

## Example

```python
from wallet.models.click_funnel_registration import ClickFunnelRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of ClickFunnelRegistration from a JSON string
click_funnel_registration_instance = ClickFunnelRegistration.from_json(json)
# print the JSON string representation of the object
print ClickFunnelRegistration.to_json()

# convert the object into a dict
click_funnel_registration_dict = click_funnel_registration_instance.to_dict()
# create an instance of ClickFunnelRegistration from a dict
click_funnel_registration_form_dict = click_funnel_registration.from_dict(click_funnel_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


