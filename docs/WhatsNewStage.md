# WhatsNewStage

Which lifecycle stage(s) an article improves, rendered as pills in the widget. The four nouns are the fixed lifecycle spine (context/design-system.md); \"platform\" is the neutral pill for portal-wide and billing changes that belong to no single stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from wallet.models.whats_new_stage import WhatsNewStage

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsNewStage from a JSON string
whats_new_stage_instance = WhatsNewStage.from_json(json)
# print the JSON string representation of the object
print WhatsNewStage.to_json()

# convert the object into a dict
whats_new_stage_dict = whats_new_stage_instance.to_dict()
# create an instance of WhatsNewStage from a dict
whats_new_stage_form_dict = whats_new_stage.from_dict(whats_new_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


