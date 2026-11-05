# WTEarlyOptInPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **object** |  | 
**total** | **object** |  | 
**page** | **object** |  | 
**page_size** | **object** |  | 
**has_more** | **object** |  | 

## Example

```python
from wallet.models.wt_early_opt_in_page import WTEarlyOptInPage

# TODO update the JSON string below
json = "{}"
# create an instance of WTEarlyOptInPage from a JSON string
wt_early_opt_in_page_instance = WTEarlyOptInPage.from_json(json)
# print the JSON string representation of the object
print WTEarlyOptInPage.to_json()

# convert the object into a dict
wt_early_opt_in_page_dict = wt_early_opt_in_page_instance.to_dict()
# create an instance of WTEarlyOptInPage from a dict
wt_early_opt_in_page_form_dict = wt_early_opt_in_page.from_dict(wt_early_opt_in_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


