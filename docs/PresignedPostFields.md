# PresignedPostFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | A base64-encoded policy detailing what constitutes an acceptable POST upload. Composed of the conditions and expiration provided to s3.createPresignedPost | 
**x_amz_signature** | **str** | A hex-encoded HMAC of the POST policy, signed with the credentials provided to the S3 client. | 
**any string name** | **str** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


