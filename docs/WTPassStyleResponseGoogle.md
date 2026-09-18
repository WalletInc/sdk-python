# WTPassStyleResponseGoogle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective** | [**WTGooglePassStyle**](WTGooglePassStyle.md) |  | 
**style** | [**WTGooglePassStyle**](WTGooglePassStyle.md) |  | 

## Example

```python
from wallet.models.wt_pass_style_response_google import WTPassStyleResponseGoogle

# TODO update the JSON string below
json = "{}"
# create an instance of WTPassStyleResponseGoogle from a JSON string
wt_pass_style_response_google_instance = WTPassStyleResponseGoogle.from_json(json)
# print the JSON string representation of the object
print WTPassStyleResponseGoogle.to_json()

# convert the object into a dict
wt_pass_style_response_google_dict = wt_pass_style_response_google_instance.to_dict()
# create an instance of WTPassStyleResponseGoogle from a dict
wt_pass_style_response_google_form_dict = wt_pass_style_response_google.from_dict(wt_pass_style_response_google_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


