# ClickFunnelContactProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**address** | **str** |  | 
**city** | **str** |  | 
**country** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**unsubscribed_at** | **object** |  | [optional] 
**cf_uvid** | **str** |  | 
**shipping_address** | **str** |  | [optional] 
**shipping_country** | **object** |  | [optional] 
**shipping_city** | **object** |  | [optional] 
**shipping_state** | **object** |  | [optional] 
**shipping_zip** | **object** |  | [optional] 
**vat_number** | **object** |  | [optional] 
**middle_name** | **object** |  | [optional] 
**websites** | **object** |  | [optional] 
**location_general** | **object** |  | [optional] 
**normalized_location** | **object** |  | [optional] 
**deduced_location** | **object** |  | [optional] 
**age** | **object** |  | [optional] 
**gender** | **object** |  | [optional] 
**age_range_lower** | **object** |  | [optional] 
**age_range_upper** | **object** |  | [optional] 
**action_score** | **object** |  | [optional] 
**known_ltv** | **str** |  | 
**tags** | **List[object]** |  | 
**time_zone** | **str** |  | [optional] 
**lists_names** | **str** |  | [optional] 
**globally_unsubscribed** | **bool** |  | 

## Example

```python
from wallet.models.click_funnel_contact_profile import ClickFunnelContactProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ClickFunnelContactProfile from a JSON string
click_funnel_contact_profile_instance = ClickFunnelContactProfile.from_json(json)
# print the JSON string representation of the object
print ClickFunnelContactProfile.to_json()

# convert the object into a dict
click_funnel_contact_profile_dict = click_funnel_contact_profile_instance.to_dict()
# create an instance of ClickFunnelContactProfile from a dict
click_funnel_contact_profile_form_dict = click_funnel_contact_profile.from_dict(click_funnel_contact_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


