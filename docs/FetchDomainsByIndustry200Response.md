# FetchDomainsByIndustry200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entertainment** | **List[object]** |  | 
**grocery** | **List[object]** |  | 
**service** | **List[object]** |  | 
**casino** | **List[object]** |  | 
**hospitality** | **List[object]** |  | 
**food** | **List[object]** |  | 
**retail** | **List[object]** |  | 

## Example

```python
from wallet.models.fetch_domains_by_industry200_response import FetchDomainsByIndustry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDomainsByIndustry200Response from a JSON string
fetch_domains_by_industry200_response_instance = FetchDomainsByIndustry200Response.from_json(json)
# print the JSON string representation of the object
print FetchDomainsByIndustry200Response.to_json()

# convert the object into a dict
fetch_domains_by_industry200_response_dict = fetch_domains_by_industry200_response_instance.to_dict()
# create an instance of FetchDomainsByIndustry200Response from a dict
fetch_domains_by_industry200_response_form_dict = fetch_domains_by_industry200_response.from_dict(fetch_domains_by_industry200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


