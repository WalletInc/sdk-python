# WTSMSOptInListSourceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | 
**source_name** | **str** |  | 

## Example

```python
from wallet.models.wtsms_opt_in_list_source_create import WTSMSOptInListSourceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WTSMSOptInListSourceCreate from a JSON string
wtsms_opt_in_list_source_create_instance = WTSMSOptInListSourceCreate.from_json(json)
# print the JSON string representation of the object
print WTSMSOptInListSourceCreate.to_json()

# convert the object into a dict
wtsms_opt_in_list_source_create_dict = wtsms_opt_in_list_source_create_instance.to_dict()
# create an instance of WTSMSOptInListSourceCreate from a dict
wtsms_opt_in_list_source_create_form_dict = wtsms_opt_in_list_source_create.from_dict(wtsms_opt_in_list_source_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


