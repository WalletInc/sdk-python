# WTBillingKeepPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_downgrade_cancelled** | **object** |  | 
**plan_name** | **object** |  | 
**scheduled_downgrade_at** | **object** |  | 

## Example

```python
from wallet.models.wt_billing_keep_plan_response import WTBillingKeepPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTBillingKeepPlanResponse from a JSON string
wt_billing_keep_plan_response_instance = WTBillingKeepPlanResponse.from_json(json)
# print the JSON string representation of the object
print WTBillingKeepPlanResponse.to_json()

# convert the object into a dict
wt_billing_keep_plan_response_dict = wt_billing_keep_plan_response_instance.to_dict()
# create an instance of WTBillingKeepPlanResponse from a dict
wt_billing_keep_plan_response_form_dict = wt_billing_keep_plan_response.from_dict(wt_billing_keep_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


