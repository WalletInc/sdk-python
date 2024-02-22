# SSImportedListRecipientCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported_list_id** | **str** |  | 
**mobile_phone_number** | **str** |  | 

## Example

```python
from wallet.models.ss_imported_list_recipient_create_params import SSImportedListRecipientCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SSImportedListRecipientCreateParams from a JSON string
ss_imported_list_recipient_create_params_instance = SSImportedListRecipientCreateParams.from_json(json)
# print the JSON string representation of the object
print SSImportedListRecipientCreateParams.to_json()

# convert the object into a dict
ss_imported_list_recipient_create_params_dict = ss_imported_list_recipient_create_params_instance.to_dict()
# create an instance of SSImportedListRecipientCreateParams from a dict
ss_imported_list_recipient_create_params_form_dict = ss_imported_list_recipient_create_params.from_dict(ss_imported_list_recipient_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


