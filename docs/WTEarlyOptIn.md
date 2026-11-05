# WTEarlyOptIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**mobile_number** | **object** |  | 
**joined_at** | **object** |  | 
**tier** | [**WTEarlyOptInTier**](WTEarlyOptInTier.md) |  | 
**opt_in_source** | **object** |  | [optional] 
**disclosure_version** | **object** |  | [optional] 
**disclosure_basis** | [**WTDisclosureBasis**](WTDisclosureBasis.md) |  | [optional] 

## Example

```python
from wallet.models.wt_early_opt_in import WTEarlyOptIn

# TODO update the JSON string below
json = "{}"
# create an instance of WTEarlyOptIn from a JSON string
wt_early_opt_in_instance = WTEarlyOptIn.from_json(json)
# print the JSON string representation of the object
print WTEarlyOptIn.to_json()

# convert the object into a dict
wt_early_opt_in_dict = wt_early_opt_in_instance.to_dict()
# create an instance of WTEarlyOptIn from a dict
wt_early_opt_in_form_dict = wt_early_opt_in.from_dict(wt_early_opt_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


