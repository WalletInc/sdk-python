# WTMediaUploadTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_file** | [**WTMediaFile**](WTMediaFile.md) |  | 
**url** | **object** |  | 
**fields** | **Dict[str, object]** |  | 
**expires_at** | **object** |  | 

## Example

```python
from wallet.models.wt_media_upload_ticket import WTMediaUploadTicket

# TODO update the JSON string below
json = "{}"
# create an instance of WTMediaUploadTicket from a JSON string
wt_media_upload_ticket_instance = WTMediaUploadTicket.from_json(json)
# print the JSON string representation of the object
print WTMediaUploadTicket.to_json()

# convert the object into a dict
wt_media_upload_ticket_dict = wt_media_upload_ticket_instance.to_dict()
# create an instance of WTMediaUploadTicket from a dict
wt_media_upload_ticket_form_dict = wt_media_upload_ticket.from_dict(wt_media_upload_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


