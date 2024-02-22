# FetchImportedListRecipientsByPage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**length** | **float** |  | 
**results** | [**List[ImportedListRecipient]**](ImportedListRecipient.md) |  | 

## Example

```python
from wallet.models.fetch_imported_list_recipients_by_page200_response import FetchImportedListRecipientsByPage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchImportedListRecipientsByPage200Response from a JSON string
fetch_imported_list_recipients_by_page200_response_instance = FetchImportedListRecipientsByPage200Response.from_json(json)
# print the JSON string representation of the object
print FetchImportedListRecipientsByPage200Response.to_json()

# convert the object into a dict
fetch_imported_list_recipients_by_page200_response_dict = fetch_imported_list_recipients_by_page200_response_instance.to_dict()
# create an instance of FetchImportedListRecipientsByPage200Response from a dict
fetch_imported_list_recipients_by_page200_response_form_dict = fetch_imported_list_recipients_by_page200_response.from_dict(fetch_imported_list_recipients_by_page200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


