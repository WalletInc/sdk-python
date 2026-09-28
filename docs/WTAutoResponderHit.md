# WTAutoResponderHit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**auto_responder_id** | **str** |  | 
**keyword** | **object** |  | 
**consumer_phone** | **object** |  | 
**inbound_message_id** | **object** |  | 
**outbound_message_id** | **object** |  | 
**outcome** | [**WTAutoResponderHitOutcome**](WTAutoResponderHitOutcome.md) |  | 
**outcome_detail** | **object** |  | 
**message_status** | **object** |  | [optional] 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.wt_auto_responder_hit import WTAutoResponderHit

# TODO update the JSON string below
json = "{}"
# create an instance of WTAutoResponderHit from a JSON string
wt_auto_responder_hit_instance = WTAutoResponderHit.from_json(json)
# print the JSON string representation of the object
print WTAutoResponderHit.to_json()

# convert the object into a dict
wt_auto_responder_hit_dict = wt_auto_responder_hit_instance.to_dict()
# create an instance of WTAutoResponderHit from a dict
wt_auto_responder_hit_form_dict = wt_auto_responder_hit.from_dict(wt_auto_responder_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


