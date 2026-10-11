# WTMediaUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **object** |  | 
**file_type** | **object** |  | 
**file_size** | **object** |  | 
**folder** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_media_upload_request import WTMediaUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTMediaUploadRequest from a JSON string
wt_media_upload_request_instance = WTMediaUploadRequest.from_json(json)
# print the JSON string representation of the object
print WTMediaUploadRequest.to_json()

# convert the object into a dict
wt_media_upload_request_dict = wt_media_upload_request_instance.to_dict()
# create an instance of WTMediaUploadRequest from a dict
wt_media_upload_request_form_dict = wt_media_upload_request.from_dict(wt_media_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


