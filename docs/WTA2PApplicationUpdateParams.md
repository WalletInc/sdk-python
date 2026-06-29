# WTA2PApplicationUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **object** |  | 
**business_type** | [**BusinessType**](BusinessType.md) |  | 
**business_classification** | [**BusinessClassification**](BusinessClassification.md) |  | 
**business_industry** | [**BusinessIndustry**](BusinessIndustry.md) |  | 
**tax_id_type** | [**BusinessRegistrationIdentifier**](BusinessRegistrationIdentifier.md) |  | 
**tax_id** | **object** |  | 
**website_url** | **object** |  | 
**social_media_url** | **object** |  | 
**regions_of_operation** | **object** |  | 
**stock_exchange** | [**BusinessStockExchanges**](BusinessStockExchanges.md) |  | [optional] 
**stock_ticker** | **object** |  | [optional] 
**messaging_volume_high** | **object** |  | 
**address1** | **object** |  | 
**address2** | **object** |  | [optional] 
**city** | **object** |  | 
**state** | **object** |  | 
**postal_code** | **object** |  | 
**country** | **object** |  | 
**first_name** | **object** |  | 
**last_name** | **object** |  | 
**email** | **object** |  | 
**job_title** | **object** |  | 
**job_position** | [**JobPosition**](JobPosition.md) |  | 
**phone_number** | **object** |  | 

## Example

```python
from wallet.models.wta2_p_application_update_params import WTA2PApplicationUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTA2PApplicationUpdateParams from a JSON string
wta2_p_application_update_params_instance = WTA2PApplicationUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTA2PApplicationUpdateParams.to_json()

# convert the object into a dict
wta2_p_application_update_params_dict = wta2_p_application_update_params_instance.to_dict()
# create an instance of WTA2PApplicationUpdateParams from a dict
wta2_p_application_update_params_form_dict = wta2_p_application_update_params.from_dict(wta2_p_application_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


