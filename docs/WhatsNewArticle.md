# WhatsNewArticle

The shape the widget renders. Matches the fields it already reads from ProductUpdate entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**story** | **str** |  | [optional] 
**items** | **object** |  | 
**stages** | **object** |  | 
**published_at** | **str** |  | 
**announced_at** | **str** |  | 

## Example

```python
from wallet.models.whats_new_article import WhatsNewArticle

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsNewArticle from a JSON string
whats_new_article_instance = WhatsNewArticle.from_json(json)
# print the JSON string representation of the object
print WhatsNewArticle.to_json()

# convert the object into a dict
whats_new_article_dict = whats_new_article_instance.to_dict()
# create an instance of WhatsNewArticle from a dict
whats_new_article_form_dict = whats_new_article.from_dict(whats_new_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


