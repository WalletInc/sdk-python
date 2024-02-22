# Performance


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
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
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


