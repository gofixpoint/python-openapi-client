# V1BatchCreateFineTuneJobsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | [optional] 
**tuning_configs** | [**List[V1TuningConfiguration]**](V1TuningConfiguration.md) |  | [optional] 
**mode** | [**V1Mode**](V1Mode.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_batch_create_fine_tune_jobs_request import V1BatchCreateFineTuneJobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1BatchCreateFineTuneJobsRequest from a JSON string
v1_batch_create_fine_tune_jobs_request_instance = V1BatchCreateFineTuneJobsRequest.from_json(json)
# print the JSON string representation of the object
print(V1BatchCreateFineTuneJobsRequest.to_json())

# convert the object into a dict
v1_batch_create_fine_tune_jobs_request_dict = v1_batch_create_fine_tune_jobs_request_instance.to_dict()
# create an instance of V1BatchCreateFineTuneJobsRequest from a dict
v1_batch_create_fine_tune_jobs_request_form_dict = v1_batch_create_fine_tune_jobs_request.from_dict(v1_batch_create_fine_tune_jobs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


