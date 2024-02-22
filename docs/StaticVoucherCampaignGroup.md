# StaticVoucherCampaignGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**voucher_type** | **int** |  | 
**created_by_source_id** | **int** |  | 
**employee_id** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**is_loaded** | **bool** |  | 

## Example

```python
from wallet.models.static_voucher_campaign_group import StaticVoucherCampaignGroup

# TODO update the JSON string below
json = "{}"
# create an instance of StaticVoucherCampaignGroup from a JSON string
static_voucher_campaign_group_instance = StaticVoucherCampaignGroup.from_json(json)
# print the JSON string representation of the object
print StaticVoucherCampaignGroup.to_json()

# convert the object into a dict
static_voucher_campaign_group_dict = static_voucher_campaign_group_instance.to_dict()
# create an instance of StaticVoucherCampaignGroup from a dict
static_voucher_campaign_group_form_dict = static_voucher_campaign_group.from_dict(static_voucher_campaign_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


