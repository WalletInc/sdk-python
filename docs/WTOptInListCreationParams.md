# WTOptInListCreationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**is_over21_required** | **bool** |  | 
**opt_in_confirmed_media_urls** | **List[str]** |  | [optional] 
**opt_out_confirmed_media_urls** | **List[str]** |  | [optional] 

## Example

```python
from wallet.models.wt_opt_in_list_creation_params import WTOptInListCreationParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTOptInListCreationParams from a JSON string
wt_opt_in_list_creation_params_instance = WTOptInListCreationParams.from_json(json)
# print the JSON string representation of the object
print WTOptInListCreationParams.to_json()

# convert the object into a dict
wt_opt_in_list_creation_params_dict = wt_opt_in_list_creation_params_instance.to_dict()
# create an instance of WTOptInListCreationParams from a dict
wt_opt_in_list_creation_params_form_dict = wt_opt_in_list_creation_params.from_dict(wt_opt_in_list_creation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


