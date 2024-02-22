# WTWalletPageViewGeoPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**longitude** | **float** |  | 
**latitude** | **float** |  | 

## Example

```python
from wallet.models.wt_wallet_page_view_geo_point import WTWalletPageViewGeoPoint

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletPageViewGeoPoint from a JSON string
wt_wallet_page_view_geo_point_instance = WTWalletPageViewGeoPoint.from_json(json)
# print the JSON string representation of the object
print WTWalletPageViewGeoPoint.to_json()

# convert the object into a dict
wt_wallet_page_view_geo_point_dict = wt_wallet_page_view_geo_point_instance.to_dict()
# create an instance of WTWalletPageViewGeoPoint from a dict
wt_wallet_page_view_geo_point_form_dict = wt_wallet_page_view_geo_point.from_dict(wt_wallet_page_view_geo_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


