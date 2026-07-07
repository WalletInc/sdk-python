# WTLeadFiInquiryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** |  | 
**pre_qualification** | **object** |  | [optional] 
**tier** | **object** |  | [optional] 
**credit_score** | **object** |  | [optional] 
**credit_limit** | [**WTLeadFiCreditOffer**](WTLeadFiCreditOffer.md) |  | 
**credit_pre_approval** | [**WTLeadFiCreditOffer**](WTLeadFiCreditOffer.md) |  | 
**consumer_profile** | [**WTLeadFiConsumerProfile**](WTLeadFiConsumerProfile.md) |  | 

## Example

```python
from wallet.models.wt_lead_fi_inquiry_result import WTLeadFiInquiryResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTLeadFiInquiryResult from a JSON string
wt_lead_fi_inquiry_result_instance = WTLeadFiInquiryResult.from_json(json)
# print the JSON string representation of the object
print WTLeadFiInquiryResult.to_json()

# convert the object into a dict
wt_lead_fi_inquiry_result_dict = wt_lead_fi_inquiry_result_instance.to_dict()
# create an instance of WTLeadFiInquiryResult from a dict
wt_lead_fi_inquiry_result_form_dict = wt_lead_fi_inquiry_result.from_dict(wt_lead_fi_inquiry_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


