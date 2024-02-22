# FetchAllCountries200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_abbreviation** | **str** |  | 
**phone_code** | **str** |  | 
**iso2** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from wallet.models.fetch_all_countries200_response_inner import FetchAllCountries200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of FetchAllCountries200ResponseInner from a JSON string
fetch_all_countries200_response_inner_instance = FetchAllCountries200ResponseInner.from_json(json)
# print the JSON string representation of the object
print FetchAllCountries200ResponseInner.to_json()

# convert the object into a dict
fetch_all_countries200_response_inner_dict = fetch_all_countries200_response_inner_instance.to_dict()
# create an instance of FetchAllCountries200ResponseInner from a dict
fetch_all_countries200_response_inner_form_dict = fetch_all_countries200_response_inner.from_dict(fetch_all_countries200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


