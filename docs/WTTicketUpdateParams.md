# WTTicketUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_phone_number** | **str** |  | [optional] 
**recipient_email_address** | **str** |  | [optional] 
**recipient_member_id** | **str** |  | [optional] 
**is_comp** | **bool** |  | [optional] 
**quantity** | **float** | The number of tickets allocated to the recipient. | [optional] 

## Example

```python
from wallet.models.wt_ticket_update_params import WTTicketUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTTicketUpdateParams from a JSON string
wt_ticket_update_params_instance = WTTicketUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTTicketUpdateParams.to_json()

# convert the object into a dict
wt_ticket_update_params_dict = wt_ticket_update_params_instance.to_dict()
# create an instance of WTTicketUpdateParams from a dict
wt_ticket_update_params_form_dict = wt_ticket_update_params.from_dict(wt_ticket_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


