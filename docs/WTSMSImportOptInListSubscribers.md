# WTSMSImportOptInListSubscribers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**bucket** | **str** |  | 
**opt_in_source_id** | **str** |  | 

## Example

```python
from wallet.models.wtsms_import_opt_in_list_subscribers import WTSMSImportOptInListSubscribers

# TODO update the JSON string below
json = "{}"
# create an instance of WTSMSImportOptInListSubscribers from a JSON string
wtsms_import_opt_in_list_subscribers_instance = WTSMSImportOptInListSubscribers.from_json(json)
# print the JSON string representation of the object
print WTSMSImportOptInListSubscribers.to_json()

# convert the object into a dict
wtsms_import_opt_in_list_subscribers_dict = wtsms_import_opt_in_list_subscribers_instance.to_dict()
# create an instance of WTSMSImportOptInListSubscribers from a dict
wtsms_import_opt_in_list_subscribers_form_dict = wtsms_import_opt_in_list_subscribers.from_dict(wtsms_import_opt_in_list_subscribers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


