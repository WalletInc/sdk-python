# SaveTicketSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redemption_instructions** | **str** |  | [optional] 
**ticket_expiration_date_time** | **datetime** |  | 
**max_comp_tickets** | **float** |  | 
**payment_design_id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 

## Example

```python
from wallet.models.save_ticket_settings_request import SaveTicketSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveTicketSettingsRequest from a JSON string
save_ticket_settings_request_instance = SaveTicketSettingsRequest.from_json(json)
# print the JSON string representation of the object
print SaveTicketSettingsRequest.to_json()

# convert the object into a dict
save_ticket_settings_request_dict = save_ticket_settings_request_instance.to_dict()
# create an instance of SaveTicketSettingsRequest from a dict
save_ticket_settings_request_form_dict = save_ticket_settings_request.from_dict(save_ticket_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


