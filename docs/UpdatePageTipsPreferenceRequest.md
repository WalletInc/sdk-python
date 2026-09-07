# UpdatePageTipsPreferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_page_tips_disabled** | **bool** |  | [optional] 

## Example

```python
from wallet.models.update_page_tips_preference_request import UpdatePageTipsPreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePageTipsPreferenceRequest from a JSON string
update_page_tips_preference_request_instance = UpdatePageTipsPreferenceRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePageTipsPreferenceRequest.to_json()

# convert the object into a dict
update_page_tips_preference_request_dict = update_page_tips_preference_request_instance.to_dict()
# create an instance of UpdatePageTipsPreferenceRequest from a dict
update_page_tips_preference_request_form_dict = update_page_tips_preference_request.from_dict(update_page_tips_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


