# OptInList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | 
**is_active** | **bool** |  | 
**list_name** | **str** |  | 
**phone_number_id** | **str** |  | 
**estimated_messages_per_month** | **int** |  | 
**opt_in_keyword** | **str** |  | 
**opt_out_keyword** | **str** |  | 
**opt_in_confirmed_response** | **str** |  | 
**opt_out_confirmed_response** | **str** |  | 
**opt_in_confirmed_customer_receives** | **str** |  | 
**opt_out_confirmed_customer_receives** | **str** |  | 
**opt_in_confirmed_media_urls** | **List[str]** |  | 
**opt_out_confirmed_media_urls** | **List[str]** |  | 
**is_over21_required** | **bool** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wallet.models.opt_in_list import OptInList

# TODO update the JSON string below
json = "{}"
# create an instance of OptInList from a JSON string
opt_in_list_instance = OptInList.from_json(json)
# print the JSON string representation of the object
print OptInList.to_json()

# convert the object into a dict
opt_in_list_dict = opt_in_list_instance.to_dict()
# create an instance of OptInList from a dict
opt_in_list_form_dict = opt_in_list.from_dict(opt_in_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


