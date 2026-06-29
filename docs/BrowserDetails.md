# BrowserDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** |  | 
**phone_verification_token** | **object** |  | [optional] 
**session_id** | **object** |  | [optional] 
**navigator_agent** | **object** |  | [optional] 
**referrer** | **object** |  | [optional] 

## Example

```python
from wallet.models.browser_details import BrowserDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserDetails from a JSON string
browser_details_instance = BrowserDetails.from_json(json)
# print the JSON string representation of the object
print BrowserDetails.to_json()

# convert the object into a dict
browser_details_dict = browser_details_instance.to_dict()
# create an instance of BrowserDetails from a dict
browser_details_form_dict = browser_details.from_dict(browser_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


