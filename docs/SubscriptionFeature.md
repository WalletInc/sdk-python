# SubscriptionFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_num** | **float** |  | 
**name** | **str** |  | 
**max_volume** | **str** |  | [optional] 
**measurement** | **str** |  | 
**description** | **str** |  | 
**current_volume** | **str** |  | [optional] 
**is_exceeded** | **bool** |  | [optional] 
**is_in_use** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 

## Example

```python
from wallet.models.subscription_feature import SubscriptionFeature

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionFeature from a JSON string
subscription_feature_instance = SubscriptionFeature.from_json(json)
# print the JSON string representation of the object
print SubscriptionFeature.to_json()

# convert the object into a dict
subscription_feature_dict = subscription_feature_instance.to_dict()
# create an instance of SubscriptionFeature from a dict
subscription_feature_form_dict = subscription_feature.from_dict(subscription_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


