# WTVideoUploadProvisionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **object** |  | 
**file_type** | **object** |  | 
**max_duration_seconds** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_video_upload_provision_params import WTVideoUploadProvisionParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTVideoUploadProvisionParams from a JSON string
wt_video_upload_provision_params_instance = WTVideoUploadProvisionParams.from_json(json)
# print the JSON string representation of the object
print WTVideoUploadProvisionParams.to_json()

# convert the object into a dict
wt_video_upload_provision_params_dict = wt_video_upload_provision_params_instance.to_dict()
# create an instance of WTVideoUploadProvisionParams from a dict
wt_video_upload_provision_params_form_dict = wt_video_upload_provision_params.from_dict(wt_video_upload_provision_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


