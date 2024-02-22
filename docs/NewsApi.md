# wallet.NewsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_news_article**](NewsApi.md#archive_news_article) | **DELETE** /v2/news/{id} | Archive news article
[**create_news_article**](NewsApi.md#create_news_article) | **POST** /v2/news | Create news article
[**fetch_all_news_articles**](NewsApi.md#fetch_all_news_articles) | **GET** /v2/news/all | Fetch all news articles
[**restore_news_article**](NewsApi.md#restore_news_article) | **PATCH** /v2/news/{id} | Restore news article
[**update_news_article**](NewsApi.md#update_news_article) | **PUT** /v2/news/{id} | Update news article


# **archive_news_article**
> NewsArticle archive_news_article(id)

Archive news article

### Example


```python
import wallet
from wallet.models.news_article import NewsArticle
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.NewsApi(api_client)
    id = None # object | 

    try:
        # Archive news article
        api_response = api_instance.archive_news_article(id)
        print("The response of NewsApi->archive_news_article:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->archive_news_article: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**NewsArticle**](NewsArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_news_article**
> NewsArticle create_news_article(wt_news_article_create_params)

Create news article

### Example


```python
import wallet
from wallet.models.news_article import NewsArticle
from wallet.models.wt_news_article_create_params import WTNewsArticleCreateParams
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.NewsApi(api_client)
    wt_news_article_create_params = wallet.WTNewsArticleCreateParams() # WTNewsArticleCreateParams | 

    try:
        # Create news article
        api_response = api_instance.create_news_article(wt_news_article_create_params)
        print("The response of NewsApi->create_news_article:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->create_news_article: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_news_article_create_params** | [**WTNewsArticleCreateParams**](WTNewsArticleCreateParams.md)|  | 

### Return type

[**NewsArticle**](NewsArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_news_articles**
> object fetch_all_news_articles(is_archive_included=is_archive_included)

Fetch all news articles

### Example


```python
import wallet
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.NewsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all news articles
        api_response = api_instance.fetch_all_news_articles(is_archive_included=is_archive_included)
        print("The response of NewsApi->fetch_all_news_articles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->fetch_all_news_articles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_news_article**
> NewsArticle restore_news_article(id)

Restore news article

### Example


```python
import wallet
from wallet.models.news_article import NewsArticle
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.NewsApi(api_client)
    id = None # object | 

    try:
        # Restore news article
        api_response = api_instance.restore_news_article(id)
        print("The response of NewsApi->restore_news_article:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->restore_news_article: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**NewsArticle**](NewsArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_news_article**
> NewsArticle update_news_article(id, wt_news_article_update_params)

Update news article

### Example


```python
import wallet
from wallet.models.news_article import NewsArticle
from wallet.models.wt_news_article_update_params import WTNewsArticleUpdateParams
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.NewsApi(api_client)
    id = None # object | 
    wt_news_article_update_params = wallet.WTNewsArticleUpdateParams() # WTNewsArticleUpdateParams | 

    try:
        # Update news article
        api_response = api_instance.update_news_article(id, wt_news_article_update_params)
        print("The response of NewsApi->update_news_article:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->update_news_article: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_news_article_update_params** | [**WTNewsArticleUpdateParams**](WTNewsArticleUpdateParams.md)|  | 

### Return type

[**NewsArticle**](NewsArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

