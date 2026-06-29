# PromoCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**description** | **object** |  | 
**promo_code** | **object** |  | 
**display_value** | **object** |  | 
**order_number** | **object** |  | 
**media_url** | **object** |  | [optional] 
**start_date** | **object** |  | 
**expiration_date** | **object** |  | 
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.promo_code import PromoCode

# TODO update the JSON string below
json = "{}"
# create an instance of PromoCode from a JSON string
promo_code_instance = PromoCode.from_json(json)
# print the JSON string representation of the object
print PromoCode.to_json()

# convert the object into a dict
promo_code_dict = promo_code_instance.to_dict()
# create an instance of PromoCode from a dict
promo_code_form_dict = promo_code.from_dict(promo_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


