# ClaimTicketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimed_by_phone_number** | **str** |  | 

## Example

```python
from wallet.models.claim_ticket_request import ClaimTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimTicketRequest from a JSON string
claim_ticket_request_instance = ClaimTicketRequest.from_json(json)
# print the JSON string representation of the object
print ClaimTicketRequest.to_json()

# convert the object into a dict
claim_ticket_request_dict = claim_ticket_request_instance.to_dict()
# create an instance of ClaimTicketRequest from a dict
claim_ticket_request_form_dict = claim_ticket_request.from_dict(claim_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


