# FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_design** | [**PaymentDesign**](PaymentDesign.md) |  | 
**value_type** | [**FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInnerValueType**](FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInnerValueType.md) |  | 
**voucher_type** | **float** |  | 
**expiration_date** | **datetime** |  | 
**start_date** | **datetime** |  | 
**title** | **str** |  | 
**is_redeemed** | **bool** |  | 
**display_value** | **str** |  | 
**offer_amount_cents_decimal** | **str** |  | 
**offer_amount_cents** | **float** |  | 
**member_id** | **str** |  | 
**cell_phone_number** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from wallet.models.fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner import FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner from a JSON string
fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner_instance = FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner.from_json(json)
# print the JSON string representation of the object
print FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner.to_json()

# convert the object into a dict
fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner_dict = fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner_instance.to_dict()
# create an instance of FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner from a dict
fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner_form_dict = fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner.from_dict(fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


