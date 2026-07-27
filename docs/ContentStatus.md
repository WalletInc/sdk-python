# ContentStatus

Curation gate for the merchant-facing feed.   - \"hold\": ingested but NOT shown to merchants. The default for everything the release fan-out writes,     so raw commit language / a not-yet-live feature can never reach the widget on its own. Marketing     (and Legal where needed) rewrite the entry into merchant copy, then flip it to \"ready\".   - \"ready\": curated and cleared; shown in the widget. A row with NO ContentStatus (legacy rows written before this gate) is grandfathered as visible: only an explicit \"hold\" hides. So the gate is fail-safe for NEW writes (default hold) without emptying the feed of the already-curated backfill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from wallet.models.content_status import ContentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ContentStatus from a JSON string
content_status_instance = ContentStatus.from_json(json)
# print the JSON string representation of the object
print ContentStatus.to_json()

# convert the object into a dict
content_status_dict = content_status_instance.to_dict()
# create an instance of ContentStatus from a dict
content_status_form_dict = content_status.from_dict(content_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


