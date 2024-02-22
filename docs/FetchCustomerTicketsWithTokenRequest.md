# FetchCustomerTicketsWithTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_verification_token** | **str** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.fetch_customer_tickets_with_token_request import FetchCustomerTicketsWithTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchCustomerTicketsWithTokenRequest from a JSON string
fetch_customer_tickets_with_token_request_instance = FetchCustomerTicketsWithTokenRequest.from_json(json)
# print the JSON string representation of the object
print FetchCustomerTicketsWithTokenRequest.to_json()

# convert the object into a dict
fetch_customer_tickets_with_token_request_dict = fetch_customer_tickets_with_token_request_instance.to_dict()
# create an instance of FetchCustomerTicketsWithTokenRequest from a dict
fetch_customer_tickets_with_token_request_form_dict = fetch_customer_tickets_with_token_request.from_dict(fetch_customer_tickets_with_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


