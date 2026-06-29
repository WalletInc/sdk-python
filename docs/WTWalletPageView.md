# WTWalletPageView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** |  | 
**wallet_object_id** | **object** |  | 
**wallet_object_prefix** | **object** |  | 
**parent_object_id** | **object** |  | 
**parent_object_prefix** | **object** |  | 
**session_id** | **object** |  | 
**navigator_agent** | **object** |  | 
**browser_name** | **object** |  | 
**browser_version** | **object** |  | 
**engine_name** | **object** |  | 
**engine_version** | **object** |  | 
**o_s_name** | **object** |  | 
**o_s_version** | **object** |  | 
**is_mobile** | **object** |  | 
**device_vendor** | **object** |  | 
**device_model** | **object** |  | 
**device_type** | **object** |  | 
**phone_verification_token** | **object** |  | 
**referring_domain** | **object** |  | [optional] 
**referrer** | **object** |  | [optional] 
**id** | **str** |  | 
**status** | **object** |  | 
**country** | **object** |  | 
**country_code** | **object** |  | 
**region** | **object** |  | 
**region_name** | **object** |  | 
**city** | **object** |  | 
**zip** | **object** |  | 
**latitude** | **object** |  | 
**longitude** | **object** |  | 
**timezone** | **object** |  | 
**isp** | **object** |  | 
**org** | **object** |  | 
**asn** | **object** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**merchant_id** | **str** |  | 
**is_active** | **object** | Denotes if this resource is active | 
**geo_point** | [**WTWalletPageViewGeoPoint**](WTWalletPageViewGeoPoint.md) |  | 

## Example

```python
from wallet.models.wt_wallet_page_view import WTWalletPageView

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletPageView from a JSON string
wt_wallet_page_view_instance = WTWalletPageView.from_json(json)
# print the JSON string representation of the object
print WTWalletPageView.to_json()

# convert the object into a dict
wt_wallet_page_view_dict = wt_wallet_page_view_instance.to_dict()
# create an instance of WTWalletPageView from a dict
wt_wallet_page_view_form_dict = wt_wallet_page_view.from_dict(wt_wallet_page_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


