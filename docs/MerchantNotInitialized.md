# MerchantNotInitialized


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**message** | **str** |  | 
**stack** | **str** |  | [optional] 
**http_error_code** | **float** |  | 
**tracking_code** | **str** |  | 

## Example

```python
from wallet.models.merchant_not_initialized import MerchantNotInitialized

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantNotInitialized from a JSON string
merchant_not_initialized_instance = MerchantNotInitialized.from_json(json)
# print the JSON string representation of the object
print MerchantNotInitialized.to_json()

# convert the object into a dict
merchant_not_initialized_dict = merchant_not_initialized_instance.to_dict()
# create an instance of MerchantNotInitialized from a dict
merchant_not_initialized_form_dict = merchant_not_initialized.from_dict(merchant_not_initialized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


