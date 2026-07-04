# SubscriptionPlanAnnual

PLACEHOLDER annual pricing for the monthly/annual toggle UX. Optional: only populated for plans surfaced through Industries.list(). `id` is a placeholder string, not a real Stripe price, and MUST NOT be used at checkout. See PlanCatalog.withAnnualPlaceholder().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **object** |  | 
**id** | **object** |  | 

## Example

```python
from wallet.models.subscription_plan_annual import SubscriptionPlanAnnual

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlanAnnual from a JSON string
subscription_plan_annual_instance = SubscriptionPlanAnnual.from_json(json)
# print the JSON string representation of the object
print SubscriptionPlanAnnual.to_json()

# convert the object into a dict
subscription_plan_annual_dict = subscription_plan_annual_instance.to_dict()
# create an instance of SubscriptionPlanAnnual from a dict
subscription_plan_annual_form_dict = subscription_plan_annual.from_dict(subscription_plan_annual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


