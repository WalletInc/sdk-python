# ClickFunnelEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase** | [**ClickFunnelPurchase**](ClickFunnelPurchase.md) |  | 
**event** | **str** |  | 

## Example

```python
from wallet.models.click_funnel_event import ClickFunnelEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClickFunnelEvent from a JSON string
click_funnel_event_instance = ClickFunnelEvent.from_json(json)
# print the JSON string representation of the object
print ClickFunnelEvent.to_json()

# convert the object into a dict
click_funnel_event_dict = click_funnel_event_instance.to_dict()
# create an instance of ClickFunnelEvent from a dict
click_funnel_event_form_dict = click_funnel_event.from_dict(click_funnel_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


