# WTAndroidKeystoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keystore_base64** | **object** |  | 
**fingerprint** | **object** |  | 

## Example

```python
from wallet.models.wt_android_keystore_response import WTAndroidKeystoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTAndroidKeystoreResponse from a JSON string
wt_android_keystore_response_instance = WTAndroidKeystoreResponse.from_json(json)
# print the JSON string representation of the object
print WTAndroidKeystoreResponse.to_json()

# convert the object into a dict
wt_android_keystore_response_dict = wt_android_keystore_response_instance.to_dict()
# create an instance of WTAndroidKeystoreResponse from a dict
wt_android_keystore_response_form_dict = wt_android_keystore_response.from_dict(wt_android_keystore_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


