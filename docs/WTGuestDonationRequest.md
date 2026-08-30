# WTGuestDonationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_verification_token** | **object** |  | 
**merchant_id** | **object** |  | 
**amount_cents** | **object** |  | 
**message** | **object** |  | [optional] 
**type** | [**WTGuestDonationRequestType**](WTGuestDonationRequestType.md) |  | [optional] 

## Example

```python
from wallet.models.wt_guest_donation_request import WTGuestDonationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTGuestDonationRequest from a JSON string
wt_guest_donation_request_instance = WTGuestDonationRequest.from_json(json)
# print the JSON string representation of the object
print WTGuestDonationRequest.to_json()

# convert the object into a dict
wt_guest_donation_request_dict = wt_guest_donation_request_instance.to_dict()
# create an instance of WTGuestDonationRequest from a dict
wt_guest_donation_request_form_dict = wt_guest_donation_request.from_dict(wt_guest_donation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


