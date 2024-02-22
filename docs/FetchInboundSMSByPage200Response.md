# FetchInboundSMSByPage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**length** | **float** |  | 
**results** | [**List[InboundSMS]**](InboundSMS.md) |  | 

## Example

```python
from wallet.models.fetch_inbound_smsby_page200_response import FetchInboundSMSByPage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchInboundSMSByPage200Response from a JSON string
fetch_inbound_smsby_page200_response_instance = FetchInboundSMSByPage200Response.from_json(json)
# print the JSON string representation of the object
print FetchInboundSMSByPage200Response.to_json()

# convert the object into a dict
fetch_inbound_smsby_page200_response_dict = fetch_inbound_smsby_page200_response_instance.to_dict()
# create an instance of FetchInboundSMSByPage200Response from a dict
fetch_inbound_smsby_page200_response_form_dict = fetch_inbound_smsby_page200_response.from_dict(fetch_inbound_smsby_page200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


