# WTWebsiteWidget

What the portal's install page needs: who may embed, where the snippet loads from, and what it loads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origins** | **object** | The website origins allowed to embed this merchant&#39;s wallet, normalised (&#x60;https://&#x60; plus host, lowercase). | 
**wallet_host** | **object** | Where the snippet loads the wallet from: the merchant&#39;s live custom domain, otherwise this environment&#39;s default wallet site. | 
**wallet_id** | **object** | The id of the merchant&#39;s wallet configuration, the object the widget opens. | 
**mark_removable** | **object** | True when the merchant&#39;s plan includes White-Labeled Custom Domain, which removes the \&quot;Powered by Wallet\&quot; mark. | 

## Example

```python
from wallet.models.wt_website_widget import WTWebsiteWidget

# TODO update the JSON string below
json = "{}"
# create an instance of WTWebsiteWidget from a JSON string
wt_website_widget_instance = WTWebsiteWidget.from_json(json)
# print the JSON string representation of the object
print WTWebsiteWidget.to_json()

# convert the object into a dict
wt_website_widget_dict = wt_website_widget_instance.to_dict()
# create an instance of WTWebsiteWidget from a dict
wt_website_widget_form_dict = wt_website_widget.from_dict(wt_website_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


