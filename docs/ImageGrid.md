# ImageGrid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**url** | **str** |  | 
**media_url** | **str** |  | 
**sequence_number** | **int** |  | 
**is_pinned** | **bool** |  | [optional] 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.image_grid import ImageGrid

# TODO update the JSON string below
json = "{}"
# create an instance of ImageGrid from a JSON string
image_grid_instance = ImageGrid.from_json(json)
# print the JSON string representation of the object
print ImageGrid.to_json()

# convert the object into a dict
image_grid_dict = image_grid_instance.to_dict()
# create an instance of ImageGrid from a dict
image_grid_form_dict = image_grid.from_dict(image_grid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


