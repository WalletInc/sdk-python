# ImportTicketsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickets** | [**List[WTTicketUpdateParams]**](WTTicketUpdateParams.md) |  | 

## Example

```python
from wallet.models.import_tickets_request import ImportTicketsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTicketsRequest from a JSON string
import_tickets_request_instance = ImportTicketsRequest.from_json(json)
# print the JSON string representation of the object
print ImportTicketsRequest.to_json()

# convert the object into a dict
import_tickets_request_dict = import_tickets_request_instance.to_dict()
# create an instance of ImportTicketsRequest from a dict
import_tickets_request_form_dict = import_tickets_request.from_dict(import_tickets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


