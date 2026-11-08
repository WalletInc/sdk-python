# WTWebsiteWidgetOriginsUpdate

Replaces the whole list. Send an empty list to stop all embedding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origins** | **object** | Up to 10 exact &#x60;https://&#x60; origins, e.g. &#x60;https://www.acmecafe.com&#x60;. No paths, no wildcards. | 

## Example

```python
from wallet.models.wt_website_widget_origins_update import WTWebsiteWidgetOriginsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WTWebsiteWidgetOriginsUpdate from a JSON string
wt_website_widget_origins_update_instance = WTWebsiteWidgetOriginsUpdate.from_json(json)
# print the JSON string representation of the object
print WTWebsiteWidgetOriginsUpdate.to_json()

# convert the object into a dict
wt_website_widget_origins_update_dict = wt_website_widget_origins_update_instance.to_dict()
# create an instance of WTWebsiteWidgetOriginsUpdate from a dict
wt_website_widget_origins_update_form_dict = wt_website_widget_origins_update.from_dict(wt_website_widget_origins_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


