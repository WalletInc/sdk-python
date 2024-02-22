# SubscriptionPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**price** | **float** |  | 
**nickname** | **str** |  | 
**examples** | **str** |  | 
**products** | [**List[SubscriptionProduct]**](SubscriptionProduct.md) |  | 
**all_pages** | [**List[PortalPage]**](PortalPage.md) |  | 

## Example

```python
from wallet.models.subscription_plan import SubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlan from a JSON string
subscription_plan_instance = SubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print SubscriptionPlan.to_json()

# convert the object into a dict
subscription_plan_dict = subscription_plan_instance.to_dict()
# create an instance of SubscriptionPlan from a dict
subscription_plan_form_dict = subscription_plan.from_dict(subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


