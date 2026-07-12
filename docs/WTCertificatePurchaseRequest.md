# WTCertificatePurchaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_member_id** | **object** |  | [optional] 
**buyer_phone_number** | **object** |  | [optional] 
**sender_name** | **object** |  | [optional] 
**recipient_phone_number** | **object** |  | [optional] 
**recipient_email_address** | **object** |  | [optional] 
**recipient_member_id** | **object** |  | [optional] 
**gift_message** | **object** |  | [optional] 
**occasion** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_certificate_purchase_request import WTCertificatePurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTCertificatePurchaseRequest from a JSON string
wt_certificate_purchase_request_instance = WTCertificatePurchaseRequest.from_json(json)
# print the JSON string representation of the object
print WTCertificatePurchaseRequest.to_json()

# convert the object into a dict
wt_certificate_purchase_request_dict = wt_certificate_purchase_request_instance.to_dict()
# create an instance of WTCertificatePurchaseRequest from a dict
wt_certificate_purchase_request_form_dict = wt_certificate_purchase_request.from_dict(wt_certificate_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


