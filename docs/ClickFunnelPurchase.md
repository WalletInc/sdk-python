# ClickFunnelPurchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**products** | [**List[ClickFunnelProduct]**](ClickFunnelProduct.md) |  | 
**member_id** | **object** |  | [optional] 
**contact** | [**ClickFunnelContact**](ClickFunnelContact.md) |  | 
**funnel_id** | **float** |  | 
**stripe_customer_token** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**subscription_id** | **object** |  | [optional] 
**charge_id** | **object** |  | [optional] 
**ctransreceipt** | **object** |  | [optional] 
**status** | **str** |  | 
**fulfillment_status** | **object** |  | [optional] 
**fulfillment_id** | **object** |  | [optional] 
**fulfillments** | **object** |  | 
**payments_count** | **object** |  | [optional] 
**infusionsoft_ccid** | **object** |  | [optional] 
**oap_customer_id** | **object** |  | [optional] 
**payment_instrument_type** | **object** |  | [optional] 
**original_amount_cents** | **float** |  | 
**original_amount** | [**ClickFunnelOriginalAmount**](ClickFunnelOriginalAmount.md) |  | 
**original_amount_currency** | **str** |  | 
**manual** | **bool** |  | 
**error_message** | **object** |  | [optional] 
**nmi_customer_vault_id** | **object** |  | [optional] 

## Example

```python
from wallet.models.click_funnel_purchase import ClickFunnelPurchase

# TODO update the JSON string below
json = "{}"
# create an instance of ClickFunnelPurchase from a JSON string
click_funnel_purchase_instance = ClickFunnelPurchase.from_json(json)
# print the JSON string representation of the object
print ClickFunnelPurchase.to_json()

# convert the object into a dict
click_funnel_purchase_dict = click_funnel_purchase_instance.to_dict()
# create an instance of ClickFunnelPurchase from a dict
click_funnel_purchase_form_dict = click_funnel_purchase.from_dict(click_funnel_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


