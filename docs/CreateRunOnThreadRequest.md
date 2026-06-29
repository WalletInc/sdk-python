# CreateRunOnThreadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**assistant_id** | **str** |  | 

## Example

```python
from wallet.models.create_run_on_thread_request import CreateRunOnThreadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRunOnThreadRequest from a JSON string
create_run_on_thread_request_instance = CreateRunOnThreadRequest.from_json(json)
# print the JSON string representation of the object
print CreateRunOnThreadRequest.to_json()

# convert the object into a dict
create_run_on_thread_request_dict = create_run_on_thread_request_instance.to_dict()
# create an instance of CreateRunOnThreadRequest from a dict
create_run_on_thread_request_form_dict = create_run_on_thread_request.from_dict(create_run_on_thread_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


