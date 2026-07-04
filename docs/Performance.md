# Performance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**body** | **object** |  | 
**start_date_time** | **object** |  | 
**price** | **object** |  | 
**url** | **object** |  | 
**order_number** | **object** |  | 
**is_sold_out** | **object** | Denotes if the event has been sold out | 
**media_url** | **object** |  | [optional] 
**payment_design_id** | **str** |  | [optional] 
**max_comp_tickets** | **object** |  | [optional] 
**ticket_expiration_date_time** | **object** |  | [optional] 
**redemption_instructions** | **object** |  | [optional] 
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.performance import Performance

# TODO update the JSON string below
json = "{}"
# create an instance of Performance from a JSON string
performance_instance = Performance.from_json(json)
# print the JSON string representation of the object
print Performance.to_json()

# convert the object into a dict
performance_dict = performance_instance.to_dict()
# create an instance of Performance from a dict
performance_form_dict = performance.from_dict(performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


