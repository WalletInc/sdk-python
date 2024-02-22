# ClickFunnelContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**page_id** | **float** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**name** | **str** |  | 
**address** | **str** |  | 
**city** | **str** |  | 
**country** | **str** |  | 
**state** | **str** |  | [optional] 
**zip** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**webinar_at** | **object** |  | [optional] 
**webinar_last_time** | **object** |  | [optional] 
**webinar_ext** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**ip** | **str** |  | 
**funnel_id** | **float** |  | 
**funnel_step_id** | **float** |  | 
**unsubscribed_at** | **object** |  | [optional] 
**cf_uvid** | **str** |  | 
**cart_affiliate_id** | **str** |  | 
**shipping_address** | **str** |  | 
**shipping_city** | **str** |  | 
**shipping_country** | **str** |  | 
**shipping_state** | **str** |  | 
**shipping_zip** | **str** |  | 
**vat_number** | **str** |  | 
**affiliate_id** | **object** |  | [optional] 
**aff_sub** | **str** |  | 
**aff_sub2** | **str** |  | 
**cf_affiliate_id** | **object** |  | [optional] 
**contact_profile** | [**ClickFunnelContactProfile**](ClickFunnelContactProfile.md) |  | [optional] 
**time_zone** | **str** |  | [optional] 
**company_name** | **str** |  | 
**company_industry** | **str** |  | 
**additional_info** | **object** |  | [optional] 
**ga_client_id** | **str** |  | [optional] 
**ga_measurement_id** | **str** |  | [optional] 

## Example

```python
from wallet.models.click_funnel_contact import ClickFunnelContact

# TODO update the JSON string below
json = "{}"
# create an instance of ClickFunnelContact from a JSON string
click_funnel_contact_instance = ClickFunnelContact.from_json(json)
# print the JSON string representation of the object
print ClickFunnelContact.to_json()

# convert the object into a dict
click_funnel_contact_dict = click_funnel_contact_instance.to_dict()
# create an instance of ClickFunnelContact from a dict
click_funnel_contact_form_dict = click_funnel_contact.from_dict(click_funnel_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


