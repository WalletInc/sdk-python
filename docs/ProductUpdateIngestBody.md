# ProductUpdateIngestBody

The structured release entry CI posts. Mirrors ProductUpdateEntry, with publishedAt optional (defaults to now).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**ProductKey**](ProductKey.md) | Which product shipped: \&quot;admin_portal\&quot; (shown in the merchant widget) or \&quot;api\&quot;. | 
**version** | **object** | The release version, e.g. \&quot;2.4.0\&quot;. Metadata; the widget renders title + items. | 
**type** | [**ProductUpdateType**](ProductUpdateType.md) | \&quot;added\&quot; for a feature release, \&quot;fixed\&quot; for a patch. | 
**title** | **object** | Merchant-facing headline for the release. | 
**items** | **object** | The release-note bullets, already split by the caller. | 
**published_at** | **object** | ISO 8601. Optional; defaults to the ingest time. | [optional] 
**story** | **object** | KAN-874: optional merchant-facing story/narrative for this release (\&quot;what this means for you\&quot;), so What&#39;s New can arrive curated at write time. Optional and content-only: it does NOT affect the hold/ready publish gate (entries still default to hold until Marketing curates them). | [optional] 

## Example

```python
from wallet.models.product_update_ingest_body import ProductUpdateIngestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUpdateIngestBody from a JSON string
product_update_ingest_body_instance = ProductUpdateIngestBody.from_json(json)
# print the JSON string representation of the object
print ProductUpdateIngestBody.to_json()

# convert the object into a dict
product_update_ingest_body_dict = product_update_ingest_body_instance.to_dict()
# create an instance of ProductUpdateIngestBody from a dict
product_update_ingest_body_form_dict = product_update_ingest_body.from_dict(product_update_ingest_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


