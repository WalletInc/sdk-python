# WTNewsArticleUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**body** | **str** |  | 
**url** | **str** |  | 
**order_number** | **int** |  | 
**media_url** | **str** |  | [optional] 
**published_date** | **datetime** |  | [optional] 

## Example

```python
from wallet.models.wt_news_article_update_params import WTNewsArticleUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTNewsArticleUpdateParams from a JSON string
wt_news_article_update_params_instance = WTNewsArticleUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTNewsArticleUpdateParams.to_json()

# convert the object into a dict
wt_news_article_update_params_dict = wt_news_article_update_params_instance.to_dict()
# create an instance of WTNewsArticleUpdateParams from a dict
wt_news_article_update_params_form_dict = wt_news_article_update_params.from_dict(wt_news_article_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


