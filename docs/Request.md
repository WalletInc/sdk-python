# Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**auth_amount** | **object** |  | 
**server_emp_id** | **object** |  | 
**module_invoked** | **object** |  | 
**cashier_emp_id** | **object** |  | 
**routing_id** | **object** |  | 
**auth_account_num** | **object** |  | 
**more_records_count** | **object** |  | 
**payment_method_id** | **object** |  | 
**tag_data** | **object** |  | 
**total_auth_amount** | **object** |  | 
**refund_flag** | **object** |  | 
**close_time** | **object** |  | 
**client_id** | **object** |  | 
**change_amount** | **object** |  | 
**employee_id** | **str** |  | 
**training_mode_flag** | **object** |  | 
**source_property_id** | **object** |  | 
**associated_check_number** | **object** |  | 
**post_to_property_id** | **object** |  | 
**unique_posting_id** | **object** |  | 
**expire_date** | **object** |  | 
**by_name_flag** | **object** |  | 
**payment_slip_id** | **object** |  | 
**financial_bin_detail** | **object** |  | 
**cvv2** | **object** |  | 
**employee_grat_tip** | **object** |  | 
**card_swipe_track1** | **object** |  | 
**card_swipe_track2** | **object** |  | 
**check_number** | **object** |  | 
**more_records_key** | **object** |  | 
**tip_amount** | **object** |  | 
**input_data** | **object** |  | 
**profit_center_id** | **object** |  | 
**invoice_number** | **object** |  | 
**receipt_text_image** | **object** |  | 
**brokerage_amount** | **object** |  | 
**amount** | **object** |  | 
**cover_count** | **object** |  | 
**more_records_flag** | **object** |  | 
**account_num** | **object** |  | 
**max_record_count** | **object** |  | 
**incremental_auth_amount** | **object** |  | 
**extra_data** | **object** |  | 
**check_type_id** | **object** |  | 
**posting_id** | **object** |  | 
**destination_property_id** | **object** |  | 
**account_detail** | **object** |  | 
**payment_amount** | **object** |  | 
**register_id** | **object** |  | 
**tndr_account_object** | **object** |  | 
**meal_period_id** | **object** |  | 

## Example

```python
from wallet.models.request import Request

# TODO update the JSON string below
json = "{}"
# create an instance of Request from a JSON string
request_instance = Request.from_json(json)
# print the JSON string representation of the object
print Request.to_json()

# convert the object into a dict
request_dict = request_instance.to_dict()
# create an instance of Request from a dict
request_form_dict = request.from_dict(request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


