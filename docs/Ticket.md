# Ticket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_phone_number** | **str** |  | [optional] 
**recipient_email_address** | **str** |  | [optional] 
**recipient_member_id** | **str** |  | [optional] 
**is_comp** | **bool** |  | [optional] 
**quantity** | **float** | The number of tickets allocated to the recipient. | [optional] 
**performance_id** | **str** |  | 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 
**is_claimed** | **bool** |  | [optional] 
**date_time_claimed** | **datetime** |  | [optional] 
**claimed_by_phone_number** | **str** |  | [optional] 
**redeemed_source** | **str** |  | [optional] 
**redeemed_transaction_id** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**register_id** | **str** |  | [optional] 
**is_redeemed** | **bool** |  | [optional] 
**date_time_redeemed** | **datetime** |  | [optional] 

## Example

```python
from wallet.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print Ticket.to_json()

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_form_dict = ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


