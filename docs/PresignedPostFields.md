# PresignedPostFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | A base64-encoded policy detailing what constitutes an acceptable POST upload. Composed of the conditions and expiration provided to s3.createPresignedPost | 
**x_amz_signature** | **str** | A hex-encoded HMAC of the POST policy, signed with the credentials provided to the S3 client. | 

## Example

```python
from wallet.models.presigned_post_fields import PresignedPostFields

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedPostFields from a JSON string
presigned_post_fields_instance = PresignedPostFields.from_json(json)
# print the JSON string representation of the object
print PresignedPostFields.to_json()

# convert the object into a dict
presigned_post_fields_dict = presigned_post_fields_instance.to_dict()
# create an instance of PresignedPostFields from a dict
presigned_post_fields_form_dict = presigned_post_fields.from_dict(presigned_post_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


