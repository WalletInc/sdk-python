# SubscriptionProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**title** | **object** |  | 
**title_full** | **object** |  | 
**category** | **object** |  | 
**volume** | **object** |  | [optional] 
**value** | **object** |  | [optional] 
**features** | **object** |  | 
**pages** | **object** |  | 
**icon_name** | **object** |  | 
**description** | **object** |  | 
**is_hourly** | **object** |  | [optional] 
**release_status** | **object** |  | [optional] 

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


