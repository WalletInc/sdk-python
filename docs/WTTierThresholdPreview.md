# WTTierThresholdPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**WTTierThresholdDirection**](WTTierThresholdDirection.md) |  | 
**would_upgrade** | **object** | Members who would move up to this tier if the threshold were saved now. | 
**total_members** | **object** | All of the merchant&#39;s active members, so the client can show &#x60;wouldUpgrade&#x60; as a share. | 

## Example

```python
from wallet.models.wt_tier_threshold_preview import WTTierThresholdPreview

# TODO update the JSON string below
json = "{}"
# create an instance of WTTierThresholdPreview from a JSON string
wt_tier_threshold_preview_instance = WTTierThresholdPreview.from_json(json)
# print the JSON string representation of the object
print WTTierThresholdPreview.to_json()

# convert the object into a dict
wt_tier_threshold_preview_dict = wt_tier_threshold_preview_instance.to_dict()
# create an instance of WTTierThresholdPreview from a dict
wt_tier_threshold_preview_form_dict = wt_tier_threshold_preview.from_dict(wt_tier_threshold_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


