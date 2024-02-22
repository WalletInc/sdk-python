# DashboardWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**div_id** | **str** |  | 
**title** | **str** |  | 
**subtitle** | **str** |  | 
**css_class** | **str** |  | 
**icon** | **str** |  | 
**route** | **str** |  | 
**type** | **str** |  | 
**order_number** | **float** |  | 
**is_default** | **bool** |  | 
**category** | **str** |  | 
**category_icon** | **str** |  | 
**category_order_number** | **float** |  | 
**page_name** | **str** |  | 

## Example

```python
from wallet.models.dashboard_widget import DashboardWidget

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardWidget from a JSON string
dashboard_widget_instance = DashboardWidget.from_json(json)
# print the JSON string representation of the object
print DashboardWidget.to_json()

# convert the object into a dict
dashboard_widget_dict = dashboard_widget_instance.to_dict()
# create an instance of DashboardWidget from a dict
dashboard_widget_form_dict = dashboard_widget.from_dict(dashboard_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


