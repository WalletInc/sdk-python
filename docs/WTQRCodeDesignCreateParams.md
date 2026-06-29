# WTQRCodeDesignCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**serialized_json_configuration** | **object** | Construct a type with a set of properties K of type T | 
**serialized_json_border** | **object** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from wallet.models.wtqr_code_design_create_params import WTQRCodeDesignCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTQRCodeDesignCreateParams from a JSON string
wtqr_code_design_create_params_instance = WTQRCodeDesignCreateParams.from_json(json)
# print the JSON string representation of the object
print WTQRCodeDesignCreateParams.to_json()

# convert the object into a dict
wtqr_code_design_create_params_dict = wtqr_code_design_create_params_instance.to_dict()
# create an instance of WTQRCodeDesignCreateParams from a dict
wtqr_code_design_create_params_form_dict = wtqr_code_design_create_params.from_dict(wtqr_code_design_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


