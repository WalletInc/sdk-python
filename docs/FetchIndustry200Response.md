# FetchIndustry200Response


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
from wallet.models.fetch_industry200_response import FetchIndustry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchIndustry200Response from a JSON string
fetch_industry200_response_instance = FetchIndustry200Response.from_json(json)
# print the JSON string representation of the object
print FetchIndustry200Response.to_json()

# convert the object into a dict
fetch_industry200_response_dict = fetch_industry200_response_instance.to_dict()
# create an instance of FetchIndustry200Response from a dict
fetch_industry200_response_form_dict = fetch_industry200_response.from_dict(fetch_industry200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


