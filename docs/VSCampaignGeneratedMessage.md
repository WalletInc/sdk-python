# VSCampaignGeneratedMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_voucher_id** | **str** |  | 
**message** | **str** |  | 
**cell_phone_number** | **str** |  | 

## Example

```python
from wallet.models.vs_campaign_generated_message import VSCampaignGeneratedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VSCampaignGeneratedMessage from a JSON string
vs_campaign_generated_message_instance = VSCampaignGeneratedMessage.from_json(json)
# print the JSON string representation of the object
print VSCampaignGeneratedMessage.to_json()

# convert the object into a dict
vs_campaign_generated_message_dict = vs_campaign_generated_message_instance.to_dict()
# create an instance of VSCampaignGeneratedMessage from a dict
vs_campaign_generated_message_form_dict = vs_campaign_generated_message.from_dict(vs_campaign_generated_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


