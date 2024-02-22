# FetchStaticVouchersPage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WTStaticVoucher]**](WTStaticVoucher.md) |  | 
**total_rows** | **float** |  | 

## Example

```python
from wallet.models.fetch_static_vouchers_page200_response import FetchStaticVouchersPage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchStaticVouchersPage200Response from a JSON string
fetch_static_vouchers_page200_response_instance = FetchStaticVouchersPage200Response.from_json(json)
# print the JSON string representation of the object
print FetchStaticVouchersPage200Response.to_json()

# convert the object into a dict
fetch_static_vouchers_page200_response_dict = fetch_static_vouchers_page200_response_instance.to_dict()
# create an instance of FetchStaticVouchersPage200Response from a dict
fetch_static_vouchers_page200_response_form_dict = fetch_static_vouchers_page200_response.from_dict(fetch_static_vouchers_page200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


