# WTConnectMoney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **object** |  | 
**currency** | **object** |  | 

## Example

```python
from wallet.models.wt_connect_money import WTConnectMoney

# TODO update the JSON string below
json = "{}"
# create an instance of WTConnectMoney from a JSON string
wt_connect_money_instance = WTConnectMoney.from_json(json)
# print the JSON string representation of the object
print WTConnectMoney.to_json()

# convert the object into a dict
wt_connect_money_dict = wt_connect_money_instance.to_dict()
# create an instance of WTConnectMoney from a dict
wt_connect_money_form_dict = wt_connect_money.from_dict(wt_connect_money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


