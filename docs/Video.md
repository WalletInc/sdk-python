# Video


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**order_number** | **float** |  | 
**additional_info_url** | **str** |  | [optional] 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 
**provider** | [**VideoProvider**](VideoProvider.md) |  | 
**asset_id** | **object** |  | 
**source** | [**WTVideoPlaybackSource**](WTVideoPlaybackSource.md) |  | 
**width** | **object** |  | [optional] 
**height** | **object** |  | [optional] 
**orientation** | [**WTVideoOrientation**](WTVideoOrientation.md) |  | [optional] 
**duration_seconds** | **object** |  | [optional] 
**poster_url** | **object** |  | [optional] 
**status** | [**WTVideoStatus**](WTVideoStatus.md) |  | [optional] 

## Example

```python
from wallet.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print Video.to_json()

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_form_dict = video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


