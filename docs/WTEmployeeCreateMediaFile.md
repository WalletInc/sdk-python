# WTEmployeeCreateMediaFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**file_data** | **object** |  | 
**folder** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_employee_create_media_file import WTEmployeeCreateMediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeCreateMediaFile from a JSON string
wt_employee_create_media_file_instance = WTEmployeeCreateMediaFile.from_json(json)
# print the JSON string representation of the object
print WTEmployeeCreateMediaFile.to_json()

# convert the object into a dict
wt_employee_create_media_file_dict = wt_employee_create_media_file_instance.to_dict()
# create an instance of WTEmployeeCreateMediaFile from a dict
wt_employee_create_media_file_form_dict = wt_employee_create_media_file.from_dict(wt_employee_create_media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


