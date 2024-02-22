# OptInListSubscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_name** | **str** |  | [optional] 
**caller_type** | **str** |  | [optional] 
**opt_in_list_id** | **str** |  | 
**opt_in_source_id** | [**PickSSOptInListMemberUpdateParamsExcludeKeyofSSOptInListMemberUpdateParamsMerchantCreatedAtOrMaxSMSCountOptInSourceID**](PickSSOptInListMemberUpdateParamsExcludeKeyofSSOptInListMemberUpdateParamsMerchantCreatedAtOrMaxSMSCountOptInSourceID.md) |  | 
**is_subscribed** | **bool** |  | 
**is_pending_age21_verification** | **bool** |  | 
**mobile_phone_number** | **str** |  | 
**referring_url** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**opted_status** | **bool** |  | [optional] 
**source** | [**SSOptInSource**](SSOptInSource.md) |  | [optional] 

## Example

```python
from wallet.models.opt_in_list_subscriber import OptInListSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of OptInListSubscriber from a JSON string
opt_in_list_subscriber_instance = OptInListSubscriber.from_json(json)
# print the JSON string representation of the object
print OptInListSubscriber.to_json()

# convert the object into a dict
opt_in_list_subscriber_dict = opt_in_list_subscriber_instance.to_dict()
# create an instance of OptInListSubscriber from a dict
opt_in_list_subscriber_form_dict = opt_in_list_subscriber.from_dict(opt_in_list_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


