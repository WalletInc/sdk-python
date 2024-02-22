# LinkBook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**url** | **str** |  | 
**icon** | **str** |  | 
**order_number** | **int** |  | 
**link_book_section_id** | [**WTLinkBookLinkBookSectionID**](WTLinkBookLinkBookSectionID.md) |  | [optional] 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.link_book import LinkBook

# TODO update the JSON string below
json = "{}"
# create an instance of LinkBook from a JSON string
link_book_instance = LinkBook.from_json(json)
# print the JSON string representation of the object
print LinkBook.to_json()

# convert the object into a dict
link_book_dict = link_book_instance.to_dict()
# create an instance of LinkBook from a dict
link_book_form_dict = link_book.from_dict(link_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


