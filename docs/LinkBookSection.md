# LinkBookSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**order_number** | **int** |  | 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.link_book_section import LinkBookSection

# TODO update the JSON string below
json = "{}"
# create an instance of LinkBookSection from a JSON string
link_book_section_instance = LinkBookSection.from_json(json)
# print the JSON string representation of the object
print LinkBookSection.to_json()

# convert the object into a dict
link_book_section_dict = link_book_section_instance.to_dict()
# create an instance of LinkBookSection from a dict
link_book_section_form_dict = link_book_section.from_dict(link_book_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


