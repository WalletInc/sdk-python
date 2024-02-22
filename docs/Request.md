# Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**auth_amount** | **float** |  | 
**server_emp_id** | **str** |  | 
**module_invoked** | **object** |  | 
**cashier_emp_id** | **str** |  | 
**routing_id** | **str** |  | 
**auth_account_num** | **float** |  | 
**more_records_count** | **float** |  | 
**payment_method_id** | **str** |  | 
**tag_data** | **object** |  | 
**total_auth_amount** | **float** |  | 
**refund_flag** | **object** |  | 
**close_time** | **datetime** |  | 
**client_id** | **str** |  | 
**change_amount** | **float** |  | 
**employee_id** | **str** |  | 
**training_mode_flag** | **object** |  | 
**source_property_id** | **str** |  | 
**associated_check_number** | **str** |  | 
**post_to_property_id** | **str** |  | 
**unique_posting_id** | **str** |  | 
**expire_date** | **datetime** |  | 
**by_name_flag** | **object** |  | 
**payment_slip_id** | **str** |  | 
**financial_bin_detail** | **object** |  | 
**cvv2** | **str** |  | 
**employee_grat_tip** | **float** |  | 
**card_swipe_track1** | **object** |  | 
**card_swipe_track2** | **object** |  | 
**check_number** | **str** |  | 
**more_records_key** | **object** |  | 
**tip_amount** | **float** |  | 
**input_data** | **object** |  | 
**profit_center_id** | **str** |  | 
**invoice_number** | **str** |  | 
**receipt_text_image** | **object** |  | 
**brokerage_amount** | **float** |  | 
**amount** | **float** |  | 
**cover_count** | **float** |  | 
**more_records_flag** | **object** |  | 
**account_num** | **str** |  | 
**max_record_count** | **float** |  | 
**incremental_auth_amount** | **float** |  | 
**extra_data** | **object** |  | 
**check_type_id** | **str** |  | 
**posting_id** | **str** |  | 
**destination_property_id** | **str** |  | 
**account_detail** | **object** |  | 
**payment_amount** | **float** |  | 
**register_id** | **str** |  | 
**tndr_account_object** | **object** |  | 
**meal_period_id** | **str** |  | 

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


