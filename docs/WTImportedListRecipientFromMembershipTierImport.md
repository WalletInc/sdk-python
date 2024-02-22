# WTImportedListRecipientFromMembershipTierImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_name** | **str** |  | 
**phone_number_id** | **str** |  | 
**tier_id** | [**WTImportedListRecipientFromMembershipTierImportTierID**](WTImportedListRecipientFromMembershipTierImportTierID.md) |  | 

## Example

```python
from wallet.models.wt_imported_list_recipient_from_membership_tier_import import WTImportedListRecipientFromMembershipTierImport

# TODO update the JSON string below
json = "{}"
# create an instance of WTImportedListRecipientFromMembershipTierImport from a JSON string
wt_imported_list_recipient_from_membership_tier_import_instance = WTImportedListRecipientFromMembershipTierImport.from_json(json)
# print the JSON string representation of the object
print WTImportedListRecipientFromMembershipTierImport.to_json()

# convert the object into a dict
wt_imported_list_recipient_from_membership_tier_import_dict = wt_imported_list_recipient_from_membership_tier_import_instance.to_dict()
# create an instance of WTImportedListRecipientFromMembershipTierImport from a dict
wt_imported_list_recipient_from_membership_tier_import_form_dict = wt_imported_list_recipient_from_membership_tier_import.from_dict(wt_imported_list_recipient_from_membership_tier_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


