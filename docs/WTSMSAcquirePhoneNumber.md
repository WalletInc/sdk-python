# WTSMSAcquirePhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | 

## Example

```python
from wallet.models.wtsms_acquire_phone_number import WTSMSAcquirePhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of WTSMSAcquirePhoneNumber from a JSON string
wtsms_acquire_phone_number_instance = WTSMSAcquirePhoneNumber.from_json(json)
# print the JSON string representation of the object
print WTSMSAcquirePhoneNumber.to_json()

# convert the object into a dict
wtsms_acquire_phone_number_dict = wtsms_acquire_phone_number_instance.to_dict()
# create an instance of WTSMSAcquirePhoneNumber from a dict
wtsms_acquire_phone_number_form_dict = wtsms_acquire_phone_number.from_dict(wtsms_acquire_phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


