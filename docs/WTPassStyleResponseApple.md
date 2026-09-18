# WTPassStyleResponseApple


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective** | [**WTApplePassStyle**](WTApplePassStyle.md) |  | 
**style** | [**WTApplePassStyle**](WTApplePassStyle.md) |  | 

## Example

```python
from wallet.models.wt_pass_style_response_apple import WTPassStyleResponseApple

# TODO update the JSON string below
json = "{}"
# create an instance of WTPassStyleResponseApple from a JSON string
wt_pass_style_response_apple_instance = WTPassStyleResponseApple.from_json(json)
# print the JSON string representation of the object
print WTPassStyleResponseApple.to_json()

# convert the object into a dict
wt_pass_style_response_apple_dict = wt_pass_style_response_apple_instance.to_dict()
# create an instance of WTPassStyleResponseApple from a dict
wt_pass_style_response_apple_form_dict = wt_pass_style_response_apple.from_dict(wt_pass_style_response_apple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


