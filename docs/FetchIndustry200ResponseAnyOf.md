# FetchIndustry200ResponseAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**List[SubscriptionPlan]**](SubscriptionPlan.md) |  | 
**title** | **str** |  | 
**icon** | **str** |  | 
**sort_number** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from wallet.models.fetch_industry200_response_any_of import FetchIndustry200ResponseAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of FetchIndustry200ResponseAnyOf from a JSON string
fetch_industry200_response_any_of_instance = FetchIndustry200ResponseAnyOf.from_json(json)
# print the JSON string representation of the object
print FetchIndustry200ResponseAnyOf.to_json()

# convert the object into a dict
fetch_industry200_response_any_of_dict = fetch_industry200_response_any_of_instance.to_dict()
# create an instance of FetchIndustry200ResponseAnyOf from a dict
fetch_industry200_response_any_of_form_dict = fetch_industry200_response_any_of.from_dict(fetch_industry200_response_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


