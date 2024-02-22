# NewsArticle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**order_number** | **int** |  | 
**body** | **str** |  | 
**url** | **str** |  | 
**media_url** | **str** |  | [optional] 
**published_date** | **datetime** |  | [optional] 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.news_article import NewsArticle

# TODO update the JSON string below
json = "{}"
# create an instance of NewsArticle from a JSON string
news_article_instance = NewsArticle.from_json(json)
# print the JSON string representation of the object
print NewsArticle.to_json()

# convert the object into a dict
news_article_dict = news_article_instance.to_dict()
# create an instance of NewsArticle from a dict
news_article_form_dict = news_article.from_dict(news_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


