# WalletPageView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | 
**wallet_object_id** | **str** |  | 
**wallet_object_prefix** | **str** |  | 
**parent_object_id** | **str** |  | 
**parent_object_prefix** | **str** |  | 
**session_id** | **str** |  | 
**navigator_agent** | **str** |  | 
**browser_name** | **str** |  | 
**browser_version** | **str** |  | 
**engine_name** | **str** |  | 
**engine_version** | **str** |  | 
**o_s_name** | **str** |  | 
**o_s_version** | **str** |  | 
**is_mobile** | **bool** |  | 
**device_vendor** | **str** |  | 
**device_model** | **str** |  | 
**device_type** | **str** |  | 
**phone_verification_token** | **str** |  | 
**referring_domain** | **str** |  | [optional] 
**referrer** | **str** |  | [optional] 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**status** | **str** |  | 
**country** | **str** |  | 
**country_code** | **str** |  | 
**region** | **str** |  | 
**region_name** | **str** |  | 
**city** | **str** |  | 
**zip** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**timezone** | **str** |  | 
**isp** | **str** |  | 
**org** | **str** |  | 
**asn** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**merchant_id** | **str** |  | 
**is_active** | **bool** | Denotes if this resource is active | 
**geo_point** | [**WTWalletPageViewGeoPoint**](WTWalletPageViewGeoPoint.md) |  | 

## Example

```python
from wallet.models.wallet_page_view import WalletPageView

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPageView from a JSON string
wallet_page_view_instance = WalletPageView.from_json(json)
# print the JSON string representation of the object
print WalletPageView.to_json()

# convert the object into a dict
wallet_page_view_dict = wallet_page_view_instance.to_dict()
# create an instance of WalletPageView from a dict
wallet_page_view_form_dict = wallet_page_view.from_dict(wallet_page_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


