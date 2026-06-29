# WTPerformanceUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**body** | **object** |  | 
**start_date_time** | **object** |  | 
**price** | **object** |  | 
**url** | **object** |  | 
**order_number** | **object** | Stores the order number | 
**is_sold_out** | **object** | Denotes if the event has been sold out | 
**media_url** | **object** |  | [optional] 
**payment_design_id** | **str** |  | [optional] 
**max_comp_tickets** | **object** |  | [optional] 
**ticket_expiration_date_time** | **object** |  | [optional] 
**redemption_instructions** | **object** |  | [optional] 

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


