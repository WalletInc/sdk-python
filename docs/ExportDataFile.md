# ExportDataFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**is_read** | **bool** |  | 
**employee_id** | **str** |  | 
**s3_bucket** | **str** |  | 
**s3_key** | **str** |  | 
**file_size_bytes** | **float** |  | 

## Example

```python
from wallet.models.export_data_file import ExportDataFile

# TODO update the JSON string below
json = "{}"
# create an instance of ExportDataFile from a JSON string
export_data_file_instance = ExportDataFile.from_json(json)
# print the JSON string representation of the object
print ExportDataFile.to_json()

# convert the object into a dict
export_data_file_dict = export_data_file_instance.to_dict()
# create an instance of ExportDataFile from a dict
export_data_file_form_dict = export_data_file.from_dict(export_data_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


