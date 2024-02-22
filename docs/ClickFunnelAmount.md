# ClickFunnelAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cents** | **float** |  | 
**currency_iso** | **str** |  | 

## Example

```python
from wallet.models.click_funnel_amount import ClickFunnelAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ClickFunnelAmount from a JSON string
click_funnel_amount_instance = ClickFunnelAmount.from_json(json)
# print the JSON string representation of the object
print ClickFunnelAmount.to_json()

# convert the object into a dict
click_funnel_amount_dict = click_funnel_amount_instance.to_dict()
# create an instance of ClickFunnelAmount from a dict
click_funnel_amount_form_dict = click_funnel_amount.from_dict(click_funnel_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


