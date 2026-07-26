# WTImportedListRecipientImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **object** |  | 
**bucket** | **object** |  | 
**consent_basis** | [**WTImportConsentBasis**](WTImportConsentBasis.md) |  | [optional] 
**consent_attested** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_imported_list_recipient_import import WTImportedListRecipientImport

# TODO update the JSON string below
json = "{}"
# create an instance of WTImportedListRecipientImport from a JSON string
wt_imported_list_recipient_import_instance = WTImportedListRecipientImport.from_json(json)
# print the JSON string representation of the object
print WTImportedListRecipientImport.to_json()

# convert the object into a dict
wt_imported_list_recipient_import_dict = wt_imported_list_recipient_import_instance.to_dict()
# create an instance of WTImportedListRecipientImport from a dict
wt_imported_list_recipient_import_form_dict = wt_imported_list_recipient_import.from_dict(wt_imported_list_recipient_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


