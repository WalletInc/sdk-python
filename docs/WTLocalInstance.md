# WTLocalInstance

tsoaModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**PhoneNumberCapabilities**](PhoneNumberCapabilities.md) |  | 
**beta** | **bool** |  | 
**address_requirements** | **str** |  | 
**iso_country** | **str** |  | 
**postal_code** | **str** |  | 
**region** | **str** |  | 
**longitude** | **float** |  | 
**latitude** | **float** |  | 
**rate_center** | **str** |  | 
**locality** | **str** |  | 
**lata** | **str** |  | 
**phone_number** | **str** |  | 
**friendly_name** | **str** |  | 

## Example

```python
from wallet.models.wt_local_instance import WTLocalInstance

# TODO update the JSON string below
json = "{}"
# create an instance of WTLocalInstance from a JSON string
wt_local_instance_instance = WTLocalInstance.from_json(json)
# print the JSON string representation of the object
print WTLocalInstance.to_json()

# convert the object into a dict
wt_local_instance_dict = wt_local_instance_instance.to_dict()
# create an instance of WTLocalInstance from a dict
wt_local_instance_form_dict = wt_local_instance.from_dict(wt_local_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


