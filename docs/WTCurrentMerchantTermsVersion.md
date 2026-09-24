# WTCurrentMerchantTermsVersion

One in-force merchant agreement, as a signup page needs it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | [**MerchantTermsDocumentType**](MerchantTermsDocumentType.md) | Which agreement: \&quot;tos\&quot; or \&quot;privacy\&quot;. | 
**version_id** | **object** | The exact id to send back as &#x60;acceptedTermsVersion&#x60; / &#x60;acceptedPrivacyVersion&#x60; on registration. | 
**effective_date** | **object** | When this version came into force. | 
**url** | **object** | The document the merchant should be shown and link to. | 

## Example

```python
from wallet.models.wt_current_merchant_terms_version import WTCurrentMerchantTermsVersion

# TODO update the JSON string below
json = "{}"
# create an instance of WTCurrentMerchantTermsVersion from a JSON string
wt_current_merchant_terms_version_instance = WTCurrentMerchantTermsVersion.from_json(json)
# print the JSON string representation of the object
print WTCurrentMerchantTermsVersion.to_json()

# convert the object into a dict
wt_current_merchant_terms_version_dict = wt_current_merchant_terms_version_instance.to_dict()
# create an instance of WTCurrentMerchantTermsVersion from a dict
wt_current_merchant_terms_version_form_dict = wt_current_merchant_terms_version.from_dict(wt_current_merchant_terms_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


