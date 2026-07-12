# WTCertificateDealCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**description** | **object** |  | [optional] 
**entitlement_type** | [**WTCertificateDealCreateRequestEntitlementType**](WTCertificateDealCreateRequestEntitlementType.md) |  | 
**entitlement_id** | **object** |  | 
**entitlement_quantity** | **object** |  | [optional] 
**entitlement_snapshot** | [**WTCertificateEntitlementSnapshot**](WTCertificateEntitlementSnapshot.md) |  | 
**retail_value_cents** | **object** |  | 
**sale_price_cents** | **object** |  | 
**quantity_available** | **object** |  | [optional] 
**requires_gift_redemption** | **object** |  | [optional] 
**valid_from** | **object** |  | [optional] 
**valid_through** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_certificate_deal_create_request import WTCertificateDealCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTCertificateDealCreateRequest from a JSON string
wt_certificate_deal_create_request_instance = WTCertificateDealCreateRequest.from_json(json)
# print the JSON string representation of the object
print WTCertificateDealCreateRequest.to_json()

# convert the object into a dict
wt_certificate_deal_create_request_dict = wt_certificate_deal_create_request_instance.to_dict()
# create an instance of WTCertificateDealCreateRequest from a dict
wt_certificate_deal_create_request_form_dict = wt_certificate_deal_create_request.from_dict(wt_certificate_deal_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


