# LoginStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**code** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from wallet.models.login_status200_response import LoginStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LoginStatus200Response from a JSON string
login_status200_response_instance = LoginStatus200Response.from_json(json)
# print the JSON string representation of the object
print LoginStatus200Response.to_json()

# convert the object into a dict
login_status200_response_dict = login_status200_response_instance.to_dict()
# create an instance of LoginStatus200Response from a dict
login_status200_response_form_dict = login_status200_response.from_dict(login_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


