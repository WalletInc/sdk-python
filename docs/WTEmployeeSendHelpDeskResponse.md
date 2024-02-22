# WTEmployeeSendHelpDeskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**help_desk_request_id** | **str** |  | 
**message** | **str** |  | 
**media_urls** | **List[str]** |  | [optional] 

## Example

```python
from wallet.models.wt_employee_send_help_desk_response import WTEmployeeSendHelpDeskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeSendHelpDeskResponse from a JSON string
wt_employee_send_help_desk_response_instance = WTEmployeeSendHelpDeskResponse.from_json(json)
# print the JSON string representation of the object
print WTEmployeeSendHelpDeskResponse.to_json()

# convert the object into a dict
wt_employee_send_help_desk_response_dict = wt_employee_send_help_desk_response_instance.to_dict()
# create an instance of WTEmployeeSendHelpDeskResponse from a dict
wt_employee_send_help_desk_response_form_dict = wt_employee_send_help_desk_response.from_dict(wt_employee_send_help_desk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


