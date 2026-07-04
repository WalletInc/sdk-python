# WTVideoUploadProvision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WTVideoUploadProvisionProvider**](WTVideoUploadProvisionProvider.md) |  | 
**url** | **object** |  | 
**fields** | **Dict[str, object]** |  | [optional] 
**asset_id** | **object** |  | 
**hd_included** | **object** |  | 

## Example

```python
from wallet.models.wt_video_upload_provision import WTVideoUploadProvision

# TODO update the JSON string below
json = "{}"
# create an instance of WTVideoUploadProvision from a JSON string
wt_video_upload_provision_instance = WTVideoUploadProvision.from_json(json)
# print the JSON string representation of the object
print WTVideoUploadProvision.to_json()

# convert the object into a dict
wt_video_upload_provision_dict = wt_video_upload_provision_instance.to_dict()
# create an instance of WTVideoUploadProvision from a dict
wt_video_upload_provision_form_dict = wt_video_upload_provision.from_dict(wt_video_upload_provision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


