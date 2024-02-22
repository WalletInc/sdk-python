# ClickFunnelProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**stripe_plan** | **str** |  | 
**amount** | [**ClickFunnelAmount**](ClickFunnelAmount.md) |  | 
**amount_currency** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**subject** | **str** |  | 
**html_body** | **str** |  | 
**thank_you_page_id** | **float** |  | 
**stripe_cancel_after_payments** | **object** |  | [optional] 
**bump** | **bool** |  | 
**cart_product_id** | **object** |  | [optional] 
**billing_integration** | **str** |  | 
**infusionsoft_product_id** | **object** |  | [optional] 
**infusionsoft_subscription_id** | **object** |  | [optional] 
**ontraport_product_id** | **object** |  | [optional] 
**ontraport_payment_count** | **object** |  | [optional] 
**ontraport_payment_type** | **object** |  | [optional] 
**ontraport_unit** | **object** |  | [optional] 
**ontraport_gateway_id** | **object** |  | [optional] 
**ontraport_invoice_id** | **object** |  | [optional] 
**commissionable** | **bool** |  | 
**statement_descriptor** | **str** |  | 
**netsuite_id** | **object** |  | [optional] 
**netsuite_tag** | **object** |  | [optional] 
**netsuite_class** | **object** |  | [optional] 
**description** | **str** |  | 

## Example

```python
from wallet.models.click_funnel_product import ClickFunnelProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ClickFunnelProduct from a JSON string
click_funnel_product_instance = ClickFunnelProduct.from_json(json)
# print the JSON string representation of the object
print ClickFunnelProduct.to_json()

# convert the object into a dict
click_funnel_product_dict = click_funnel_product_instance.to_dict()
# create an instance of ClickFunnelProduct from a dict
click_funnel_product_form_dict = click_funnel_product.from_dict(click_funnel_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


