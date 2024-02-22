# PresignedPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL that should be used as the action of the form. | 
**fields** | [**PresignedPostFields**](PresignedPostFields.md) |  | 

## Example

```python
from wallet.models.presigned_post import PresignedPost

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedPost from a JSON string
presigned_post_instance = PresignedPost.from_json(json)
# print the JSON string representation of the object
print PresignedPost.to_json()

# convert the object into a dict
presigned_post_dict = presigned_post_instance.to_dict()
# create an instance of PresignedPost from a dict
presigned_post_form_dict = presigned_post.from_dict(presigned_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


