# WTStaticVoucherCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_amount_cents** | **object** |  | 
**member_id** | **object** |  | [optional] 
**cell_phone** | **object** |  | 
**campaign_id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 

## Example

```python
from wallet.models.wt_static_voucher_create_params import WTStaticVoucherCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTStaticVoucherCreateParams from a JSON string
wt_static_voucher_create_params_instance = WTStaticVoucherCreateParams.from_json(json)
# print the JSON string representation of the object
print WTStaticVoucherCreateParams.to_json()

# convert the object into a dict
wt_static_voucher_create_params_dict = wt_static_voucher_create_params_instance.to_dict()
# create an instance of WTStaticVoucherCreateParams from a dict
wt_static_voucher_create_params_form_dict = wt_static_voucher_create_params.from_dict(wt_static_voucher_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


