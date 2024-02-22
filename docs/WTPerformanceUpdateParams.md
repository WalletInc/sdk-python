# WTPerformanceUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**body** | **str** |  | 
**start_date_time** | **datetime** |  | 
**price** | **str** |  | 
**url** | **str** |  | 
**order_number** | **int** | Stores the order number | 
**is_sold_out** | **bool** | Denotes if the event has been sold out | 
**media_url** | **str** |  | [optional] 
**payment_design_id** | **str** |  | [optional] 
**max_comp_tickets** | **float** |  | [optional] 
**ticket_expiration_date_time** | **datetime** |  | [optional] 
**redemption_instructions** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_performance_update_params import WTPerformanceUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPerformanceUpdateParams from a JSON string
wt_performance_update_params_instance = WTPerformanceUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTPerformanceUpdateParams.to_json()

# convert the object into a dict
wt_performance_update_params_dict = wt_performance_update_params_instance.to_dict()
# create an instance of WTPerformanceUpdateParams from a dict
wt_performance_update_params_form_dict = wt_performance_update_params.from_dict(wt_performance_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


