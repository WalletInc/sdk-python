# ImportedListRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported_list_id** | **str** |  | 
**mobile_phone_number** | **object** |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**opted_status** | **object** |  | [optional] 

## Example

```python
from wallet.models.imported_list_recipient import ImportedListRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedListRecipient from a JSON string
imported_list_recipient_instance = ImportedListRecipient.from_json(json)
# print the JSON string representation of the object
print ImportedListRecipient.to_json()

# convert the object into a dict
imported_list_recipient_dict = imported_list_recipient_instance.to_dict()
# create an instance of ImportedListRecipient from a dict
imported_list_recipient_form_dict = imported_list_recipient.from_dict(imported_list_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


