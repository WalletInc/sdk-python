# WTMediaFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**merchant_id** | **str** |  | 
**file_url** | **object** | The URL of the file | 
**file_type** | **object** | The type of the file | 
**file_name** | **object** | The name of the file | 
**file_size** | **object** | The size of the file | 
**folder** | **object** | The folder in which the file is stored | 
**employee_id** | **str** |  | 
**status** | [**WTMediaFileStatus**](WTMediaFileStatus.md) | Processing state of a large upload (KAN-367). Absent on files uploaded the original way, which are always ready. | [optional] 

## Example

```python
from wallet.models.wt_media_file import WTMediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of WTMediaFile from a JSON string
wt_media_file_instance = WTMediaFile.from_json(json)
# print the JSON string representation of the object
print WTMediaFile.to_json()

# convert the object into a dict
wt_media_file_dict = wt_media_file_instance.to_dict()
# create an instance of WTMediaFile from a dict
wt_media_file_form_dict = wt_media_file.from_dict(wt_media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


