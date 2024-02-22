# WTBillingChangePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_name** | **str** |  | 

## Example

```python
from wallet.models.wt_billing_change_plan import WTBillingChangePlan

# TODO update the JSON string below
json = "{}"
# create an instance of WTBillingChangePlan from a JSON string
wt_billing_change_plan_instance = WTBillingChangePlan.from_json(json)
# print the JSON string representation of the object
print WTBillingChangePlan.to_json()

# convert the object into a dict
wt_billing_change_plan_dict = wt_billing_change_plan_instance.to_dict()
# create an instance of WTBillingChangePlan from a dict
wt_billing_change_plan_form_dict = wt_billing_change_plan.from_dict(wt_billing_change_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


