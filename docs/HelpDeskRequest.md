# HelpDeskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_phone_number_id** | **str** |  | 
**cell_phone** | **object** |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**employee_id** | **str** |  | 
**is_resolved** | **object** |  | 
**resolved_at** | **object** |  | [optional] 

## Example

```python
from wallet.models.help_desk_request import HelpDeskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HelpDeskRequest from a JSON string
help_desk_request_instance = HelpDeskRequest.from_json(json)
# print the JSON string representation of the object
print HelpDeskRequest.to_json()

# convert the object into a dict
help_desk_request_dict = help_desk_request_instance.to_dict()
# create an instance of HelpDeskRequest from a dict
help_desk_request_form_dict = help_desk_request.from_dict(help_desk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


