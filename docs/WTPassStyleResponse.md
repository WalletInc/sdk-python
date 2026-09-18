# WTPassStyleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | [**WTPassBrandKit**](WTPassBrandKit.md) |  | 
**effective** | [**WTPassBrandKit**](WTPassBrandKit.md) |  | 
**providers** | [**WTPassStyleResponseProviders**](WTPassStyleResponseProviders.md) |  | 
**google** | [**WTPassStyleResponseGoogle**](WTPassStyleResponseGoogle.md) |  | [optional] 
**apple** | [**WTPassStyleResponseApple**](WTPassStyleResponseApple.md) |  | [optional] 

## Example

```python
from wallet.models.wt_pass_style_response import WTPassStyleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTPassStyleResponse from a JSON string
wt_pass_style_response_instance = WTPassStyleResponse.from_json(json)
# print the JSON string representation of the object
print WTPassStyleResponse.to_json()

# convert the object into a dict
wt_pass_style_response_dict = wt_pass_style_response_instance.to_dict()
# create an instance of WTPassStyleResponse from a dict
wt_pass_style_response_form_dict = wt_pass_style_response.from_dict(wt_pass_style_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


