# SubscriptionProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**title_full** | **str** |  | 
**category** | **str** |  | 
**volume** | **float** |  | [optional] 
**features** | [**List[SubscriptionFeature]**](SubscriptionFeature.md) |  | 
**pages** | [**List[PortalPage]**](PortalPage.md) |  | 
**icon_name** | **str** |  | 
**description** | **str** |  | 
**is_hourly** | **bool** |  | [optional] 
**release_status** | **str** |  | [optional] 

## Example

```python
from wallet.models.subscription_product import SubscriptionProduct

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionProduct from a JSON string
subscription_product_instance = SubscriptionProduct.from_json(json)
# print the JSON string representation of the object
print SubscriptionProduct.to_json()

# convert the object into a dict
subscription_product_dict = subscription_product_instance.to_dict()
# create an instance of SubscriptionProduct from a dict
subscription_product_form_dict = subscription_product.from_dict(subscription_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


