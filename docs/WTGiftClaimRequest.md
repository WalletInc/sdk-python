# WTGiftClaimRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimed_by_phone_number** | **object** |  | 
**claimed_by_member_id** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_gift_claim_request import WTGiftClaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTGiftClaimRequest from a JSON string
wt_gift_claim_request_instance = WTGiftClaimRequest.from_json(json)
# print the JSON string representation of the object
print WTGiftClaimRequest.to_json()

# convert the object into a dict
wt_gift_claim_request_dict = wt_gift_claim_request_instance.to_dict()
# create an instance of WTGiftClaimRequest from a dict
wt_gift_claim_request_form_dict = wt_gift_claim_request.from_dict(wt_gift_claim_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


