# WTVideoUploadPresignParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **object** |  | 
**file_type** | **object** |  | 

## Example

```python
from wallet.models.wt_video_upload_presign_params import WTVideoUploadPresignParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTVideoUploadPresignParams from a JSON string
wt_video_upload_presign_params_instance = WTVideoUploadPresignParams.from_json(json)
# print the JSON string representation of the object
print WTVideoUploadPresignParams.to_json()

# convert the object into a dict
wt_video_upload_presign_params_dict = wt_video_upload_presign_params_instance.to_dict()
# create an instance of WTVideoUploadPresignParams from a dict
wt_video_upload_presign_params_form_dict = wt_video_upload_presign_params.from_dict(wt_video_upload_presign_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


