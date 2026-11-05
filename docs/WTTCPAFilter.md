# WTTCPAFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_phone** | **str** |  | 
**phone_number_id** | **str** |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 

## Example

```python
from wallet.models.wttcpa_filter import WTTCPAFilter

# TODO update the JSON string below
json = "{}"
# create an instance of WTTCPAFilter from a JSON string
wttcpa_filter_instance = WTTCPAFilter.from_json(json)
# print the JSON string representation of the object
print WTTCPAFilter.to_json()

# convert the object into a dict
wttcpa_filter_dict = wttcpa_filter_instance.to_dict()
# create an instance of WTTCPAFilter from a dict
wttcpa_filter_form_dict = wttcpa_filter.from_dict(wttcpa_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


