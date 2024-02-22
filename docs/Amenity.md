# Amenity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 
**displayed_price** | **str** |  | [optional] 
**order_number** | **int** |  | 
**media_url** | **str** |  | [optional] 
**additional_info_url** | **str** |  | [optional] 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.amenity import Amenity

# TODO update the JSON string below
json = "{}"
# create an instance of Amenity from a JSON string
amenity_instance = Amenity.from_json(json)
# print the JSON string representation of the object
print Amenity.to_json()

# convert the object into a dict
amenity_dict = amenity_instance.to_dict()
# create an instance of Amenity from a dict
amenity_form_dict = amenity.from_dict(amenity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


