# MerchantTermsDocumentType

The two agreements a merchant accepts at signup. One acceptance record is written per document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from wallet.models.merchant_terms_document_type import MerchantTermsDocumentType

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantTermsDocumentType from a JSON string
merchant_terms_document_type_instance = MerchantTermsDocumentType.from_json(json)
# print the JSON string representation of the object
print MerchantTermsDocumentType.to_json()

# convert the object into a dict
merchant_terms_document_type_dict = merchant_terms_document_type_instance.to_dict()
# create an instance of MerchantTermsDocumentType from a dict
merchant_terms_document_type_form_dict = merchant_terms_document_type.from_dict(merchant_terms_document_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


