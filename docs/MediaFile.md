# MediaFile


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
from wallet.models.media_file import MediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFile from a JSON string
media_file_instance = MediaFile.from_json(json)
# print the JSON string representation of the object
print MediaFile.to_json()

# convert the object into a dict
media_file_dict = media_file_instance.to_dict()
# create an instance of MediaFile from a dict
media_file_form_dict = media_file.from_dict(media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


