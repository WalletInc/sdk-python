# WTA2PApplicationUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | 
**business_type** | [**BusinessType**](BusinessType.md) |  | 
**business_classification** | [**BusinessClassification**](BusinessClassification.md) |  | 
**business_industry** | [**BusinessIndustry**](BusinessIndustry.md) |  | 
**tax_id_type** | [**BusinessRegistrationIdentifier**](BusinessRegistrationIdentifier.md) |  | 
**tax_id** | **str** |  | 
**website_url** | **str** |  | 
**social_media_url** | **str** |  | 
**regions_of_operation** | [**List[BusinessRegionsOfOperation]**](BusinessRegionsOfOperation.md) |  | 
**stock_exchange** | [**BusinessStockExchanges**](BusinessStockExchanges.md) |  | [optional] 
**stock_ticker** | **str** |  | [optional] 
**messaging_volume_high** | **bool** |  | 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**city** | **str** |  | 
**state** | **str** |  | 
**postal_code** | **str** |  | 
**country** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**job_title** | **str** |  | 
**job_position** | [**JobPosition**](JobPosition.md) |  | 
**phone_number** | **str** |  | 

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


