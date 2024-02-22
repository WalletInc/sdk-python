# MSMemberRedemptionPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MSMemberRedemption]**](MSMemberRedemption.md) | Stores the results as an array | 
**length** | **int** | Denotes the length of the results array | 
**total** | **int** | Denotes the total number of records present in the database | 

## Example

```python
from wallet.models.ms_member_redemption_pagination import MSMemberRedemptionPagination

# TODO update the JSON string below
json = "{}"
# create an instance of MSMemberRedemptionPagination from a JSON string
ms_member_redemption_pagination_instance = MSMemberRedemptionPagination.from_json(json)
# print the JSON string representation of the object
print MSMemberRedemptionPagination.to_json()

# convert the object into a dict
ms_member_redemption_pagination_dict = ms_member_redemption_pagination_instance.to_dict()
# create an instance of MSMemberRedemptionPagination from a dict
ms_member_redemption_pagination_form_dict = ms_member_redemption_pagination.from_dict(ms_member_redemption_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


