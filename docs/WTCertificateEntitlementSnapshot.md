# WTCertificateEntitlementSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**description** | **object** |  | [optional] 
**media_url** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_certificate_entitlement_snapshot import WTCertificateEntitlementSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of WTCertificateEntitlementSnapshot from a JSON string
wt_certificate_entitlement_snapshot_instance = WTCertificateEntitlementSnapshot.from_json(json)
# print the JSON string representation of the object
print WTCertificateEntitlementSnapshot.to_json()

# convert the object into a dict
wt_certificate_entitlement_snapshot_dict = wt_certificate_entitlement_snapshot_instance.to_dict()
# create an instance of WTCertificateEntitlementSnapshot from a dict
wt_certificate_entitlement_snapshot_form_dict = wt_certificate_entitlement_snapshot.from_dict(wt_certificate_entitlement_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


