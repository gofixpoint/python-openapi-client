# FixpointBatchDeleteDatasetLogsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_ids** | **List[str]** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.fixpoint_batch_delete_dataset_logs_request import FixpointBatchDeleteDatasetLogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FixpointBatchDeleteDatasetLogsRequest from a JSON string
fixpoint_batch_delete_dataset_logs_request_instance = FixpointBatchDeleteDatasetLogsRequest.from_json(json)
# print the JSON string representation of the object
print(FixpointBatchDeleteDatasetLogsRequest.to_json())

# convert the object into a dict
fixpoint_batch_delete_dataset_logs_request_dict = fixpoint_batch_delete_dataset_logs_request_instance.to_dict()
# create an instance of FixpointBatchDeleteDatasetLogsRequest from a dict
fixpoint_batch_delete_dataset_logs_request_form_dict = fixpoint_batch_delete_dataset_logs_request.from_dict(fixpoint_batch_delete_dataset_logs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


