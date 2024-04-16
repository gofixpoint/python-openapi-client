# FixpointPostDatasetLogsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_names** | **List[str]** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.fixpoint_post_dataset_logs_request import FixpointPostDatasetLogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FixpointPostDatasetLogsRequest from a JSON string
fixpoint_post_dataset_logs_request_instance = FixpointPostDatasetLogsRequest.from_json(json)
# print the JSON string representation of the object
print(FixpointPostDatasetLogsRequest.to_json())

# convert the object into a dict
fixpoint_post_dataset_logs_request_dict = fixpoint_post_dataset_logs_request_instance.to_dict()
# create an instance of FixpointPostDatasetLogsRequest from a dict
fixpoint_post_dataset_logs_request_form_dict = fixpoint_post_dataset_logs_request.from_dict(fixpoint_post_dataset_logs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


