# WTVideoUploadPresign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** |  | 
**fields** | **Dict[str, object]** |  | 
**key** | **object** |  | 
**public_url** | **object** |  | 

## Example

```python
from wallet.models.wt_video_upload_presign import WTVideoUploadPresign

# TODO update the JSON string below
json = "{}"
# create an instance of WTVideoUploadPresign from a JSON string
wt_video_upload_presign_instance = WTVideoUploadPresign.from_json(json)
# print the JSON string representation of the object
print WTVideoUploadPresign.to_json()

# convert the object into a dict
wt_video_upload_presign_dict = wt_video_upload_presign_instance.to_dict()
# create an instance of WTVideoUploadPresign from a dict
wt_video_upload_presign_form_dict = wt_video_upload_presign.from_dict(wt_video_upload_presign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


