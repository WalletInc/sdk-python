# WTWebsiteWidgetEmbedders

The anonymous read the wallet's own server uses to build its `frame-ancestors` header.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origins** | **object** |  | 
**mark_removable** | **bool** |  | 

## Example

```python
from wallet.models.wt_website_widget_embedders import WTWebsiteWidgetEmbedders

# TODO update the JSON string below
json = "{}"
# create an instance of WTWebsiteWidgetEmbedders from a JSON string
wt_website_widget_embedders_instance = WTWebsiteWidgetEmbedders.from_json(json)
# print the JSON string representation of the object
print WTWebsiteWidgetEmbedders.to_json()

# convert the object into a dict
wt_website_widget_embedders_dict = wt_website_widget_embedders_instance.to_dict()
# create an instance of WTWebsiteWidgetEmbedders from a dict
wt_website_widget_embedders_form_dict = wt_website_widget_embedders.from_dict(wt_website_widget_embedders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


