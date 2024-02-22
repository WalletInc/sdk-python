# WTEmployeeS3FilePresign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**file_type** | **str** |  | 
**context** | [**WTEmployeeS3FilePresignContext**](WTEmployeeS3FilePresignContext.md) |  | 

## Example

```python
from wallet.models.wt_employee_s3_file_presign import WTEmployeeS3FilePresign

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeS3FilePresign from a JSON string
wt_employee_s3_file_presign_instance = WTEmployeeS3FilePresign.from_json(json)
# print the JSON string representation of the object
print WTEmployeeS3FilePresign.to_json()

# convert the object into a dict
wt_employee_s3_file_presign_dict = wt_employee_s3_file_presign_instance.to_dict()
# create an instance of WTEmployeeS3FilePresign from a dict
wt_employee_s3_file_presign_form_dict = wt_employee_s3_file_presign.from_dict(wt_employee_s3_file_presign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


