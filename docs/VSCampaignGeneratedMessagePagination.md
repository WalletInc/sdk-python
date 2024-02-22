# VSCampaignGeneratedMessagePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[VSCampaignGeneratedMessage]**](VSCampaignGeneratedMessage.md) | Stores the results as an array | 
**length** | **float** | Denotes the length of the results array | 
**total** | **float** | Denotes the total number of records present in the database | 

## Example

```python
from wallet.models.vs_campaign_generated_message_pagination import VSCampaignGeneratedMessagePagination

# TODO update the JSON string below
json = "{}"
# create an instance of VSCampaignGeneratedMessagePagination from a JSON string
vs_campaign_generated_message_pagination_instance = VSCampaignGeneratedMessagePagination.from_json(json)
# print the JSON string representation of the object
print VSCampaignGeneratedMessagePagination.to_json()

# convert the object into a dict
vs_campaign_generated_message_pagination_dict = vs_campaign_generated_message_pagination_instance.to_dict()
# create an instance of VSCampaignGeneratedMessagePagination from a dict
vs_campaign_generated_message_pagination_form_dict = vs_campaign_generated_message_pagination.from_dict(vs_campaign_generated_message_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


