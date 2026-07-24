# ProductKey

Product update (\"What's New\") entries for the in-product News widget (KAN-557).  DESIGN - fan-out at write time, never read ReadMe here:    The release process writes each release to TWO sinks: ReadMe (the external wallet.dev surface)    and a structured store WE own (what this class reads). The in-product widget reads THIS store,    never ReadMe, which answers the two concerns directly:      - ReadMe outages cannot affect the merchant widget. ReadMe is a WRITE-TIME sink only, and that        write is already best-effort/non-fatal. Read time has zero external dependency.      - Nothing parses changelog markdown at read time. Entries are already structured (title +        items[]). The only split-into-items happens once, at WRITE time, on our OWN generated        release notes (semantic-release's \"* item\" list) - deterministic input we control, not a        regex over arbitrary third-party content.  PROTOTYPE NOTE: `readFromStore` below returns a seeded fixture so the endpoint returns real-looking data today. In production it reads the durable store the release plugin writes to. That store is the ONE open decision (Parse class for durability vs a capped Redis list); everything else here - the read path, filtering, read-through caching, and the unread-count - is the shape being shown, and does not change with the store choice because it all sits behind `readFromStore`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from wallet.models.product_key import ProductKey

# TODO update the JSON string below
json = "{}"
# create an instance of ProductKey from a JSON string
product_key_instance = ProductKey.from_json(json)
# print the JSON string representation of the object
print ProductKey.to_json()

# convert the object into a dict
product_key_dict = product_key_instance.to_dict()
# create an instance of ProductKey from a dict
product_key_form_dict = product_key.from_dict(product_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


