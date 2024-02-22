# WTLinkBook


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
from wallet.models.wt_link_book import WTLinkBook

# TODO update the JSON string below
json = "{}"
# create an instance of WTLinkBook from a JSON string
wt_link_book_instance = WTLinkBook.from_json(json)
# print the JSON string representation of the object
print WTLinkBook.to_json()

# convert the object into a dict
wt_link_book_dict = wt_link_book_instance.to_dict()
# create an instance of WTLinkBook from a dict
wt_link_book_form_dict = wt_link_book.from_dict(wt_link_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


