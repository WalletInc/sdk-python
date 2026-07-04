# WTVideoPlaybackSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WTVideoPlaybackSourceType**](WTVideoPlaybackSourceType.md) |  | 
**url** | **object** |  | 

## Example

```python
from wallet.models.wt_video_playback_source import WTVideoPlaybackSource

# TODO update the JSON string below
json = "{}"
# create an instance of WTVideoPlaybackSource from a JSON string
wt_video_playback_source_instance = WTVideoPlaybackSource.from_json(json)
# print the JSON string representation of the object
print WTVideoPlaybackSource.to_json()

# convert the object into a dict
wt_video_playback_source_dict = wt_video_playback_source_instance.to_dict()
# create an instance of WTVideoPlaybackSource from a dict
wt_video_playback_source_form_dict = wt_video_playback_source.from_dict(wt_video_playback_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


