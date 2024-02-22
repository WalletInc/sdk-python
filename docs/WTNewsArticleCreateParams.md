# WTNewsArticleCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**order_number** | **int** |  | 
**body** | **str** |  | 
**url** | **str** |  | 
**media_url** | **str** |  | [optional] 
**published_date** | **datetime** |  | [optional] 

## Example

```python
from wallet.models.wt_news_article_create_params import WTNewsArticleCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTNewsArticleCreateParams from a JSON string
wt_news_article_create_params_instance = WTNewsArticleCreateParams.from_json(json)
# print the JSON string representation of the object
print WTNewsArticleCreateParams.to_json()

# convert the object into a dict
wt_news_article_create_params_dict = wt_news_article_create_params_instance.to_dict()
# create an instance of WTNewsArticleCreateParams from a dict
wt_news_article_create_params_form_dict = wt_news_article_create_params.from_dict(wt_news_article_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


