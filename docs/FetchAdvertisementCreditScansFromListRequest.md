# FetchAdvertisementCreditScansFromListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_of_ad_credit_scan_ids** | **List[str]** |  | 

## Example

```python
from wallet.models.fetch_advertisement_credit_scans_from_list_request import FetchAdvertisementCreditScansFromListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchAdvertisementCreditScansFromListRequest from a JSON string
fetch_advertisement_credit_scans_from_list_request_instance = FetchAdvertisementCreditScansFromListRequest.from_json(json)
# print the JSON string representation of the object
print FetchAdvertisementCreditScansFromListRequest.to_json()

# convert the object into a dict
fetch_advertisement_credit_scans_from_list_request_dict = fetch_advertisement_credit_scans_from_list_request_instance.to_dict()
# create an instance of FetchAdvertisementCreditScansFromListRequest from a dict
fetch_advertisement_credit_scans_from_list_request_form_dict = fetch_advertisement_credit_scans_from_list_request.from_dict(fetch_advertisement_credit_scans_from_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


