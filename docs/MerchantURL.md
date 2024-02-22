# MerchantURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** |  | 
**destination_url** | **str** |  | 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**merchant_id** | **str** |  | 
**is_active** | **bool** |  | 

## Example

```python
from wallet.models.merchant_url import MerchantURL

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantURL from a JSON string
merchant_url_instance = MerchantURL.from_json(json)
# print the JSON string representation of the object
print MerchantURL.to_json()

# convert the object into a dict
merchant_url_dict = merchant_url_instance.to_dict()
# create an instance of MerchantURL from a dict
merchant_url_form_dict = merchant_url.from_dict(merchant_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


