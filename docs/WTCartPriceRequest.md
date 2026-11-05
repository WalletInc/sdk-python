# WTCartPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | **object** |  | 

## Example

```python
from wallet.models.wt_cart_price_request import WTCartPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTCartPriceRequest from a JSON string
wt_cart_price_request_instance = WTCartPriceRequest.from_json(json)
# print the JSON string representation of the object
print WTCartPriceRequest.to_json()

# convert the object into a dict
wt_cart_price_request_dict = wt_cart_price_request_instance.to_dict()
# create an instance of WTCartPriceRequest from a dict
wt_cart_price_request_form_dict = wt_cart_price_request.from_dict(wt_cart_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


