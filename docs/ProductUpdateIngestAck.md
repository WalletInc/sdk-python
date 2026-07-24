# ProductUpdateIngestAck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**received** | **bool** |  | 
**product** | [**ProductKey**](ProductKey.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from wallet.models.product_update_ingest_ack import ProductUpdateIngestAck

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUpdateIngestAck from a JSON string
product_update_ingest_ack_instance = ProductUpdateIngestAck.from_json(json)
# print the JSON string representation of the object
print ProductUpdateIngestAck.to_json()

# convert the object into a dict
product_update_ingest_ack_dict = product_update_ingest_ack_instance.to_dict()
# create an instance of ProductUpdateIngestAck from a dict
product_update_ingest_ack_form_dict = product_update_ingest_ack.from_dict(product_update_ingest_ack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


