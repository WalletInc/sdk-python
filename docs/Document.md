# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**merchant_id** | **str** |  | 
**file_url** | **str** | The URL of the file | 
**file_type** | **str** | The type of the file | 
**file_name** | **str** | The name of the file | 
**file_size** | **float** | The size of the file | 
**folder** | **str** | The folder in which the file is stored | 
**employee_id** | **str** |  | 

## Example

```python
from wallet.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print Document.to_json()

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


