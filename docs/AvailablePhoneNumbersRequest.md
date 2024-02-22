# AvailablePhoneNumbersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_code** | **int** | The area code within which an available number needs to be queried | 
**limit** | **float** | The number of available phone numbers to be returned in a single request | [optional] 

## Example

```python
from wallet.models.available_phone_numbers_request import AvailablePhoneNumbersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePhoneNumbersRequest from a JSON string
available_phone_numbers_request_instance = AvailablePhoneNumbersRequest.from_json(json)
# print the JSON string representation of the object
print AvailablePhoneNumbersRequest.to_json()

# convert the object into a dict
available_phone_numbers_request_dict = available_phone_numbers_request_instance.to_dict()
# create an instance of AvailablePhoneNumbersRequest from a dict
available_phone_numbers_request_form_dict = available_phone_numbers_request.from_dict(available_phone_numbers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


