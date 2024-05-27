# V1BatchCreateFineTuneJobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fine_tune_jobs** | [**List[V1FineTuneJob]**](V1FineTuneJob.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_batch_create_fine_tune_jobs_response import V1BatchCreateFineTuneJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1BatchCreateFineTuneJobsResponse from a JSON string
v1_batch_create_fine_tune_jobs_response_instance = V1BatchCreateFineTuneJobsResponse.from_json(json)
# print the JSON string representation of the object
print(V1BatchCreateFineTuneJobsResponse.to_json())

# convert the object into a dict
v1_batch_create_fine_tune_jobs_response_dict = v1_batch_create_fine_tune_jobs_response_instance.to_dict()
# create an instance of V1BatchCreateFineTuneJobsResponse from a dict
v1_batch_create_fine_tune_jobs_response_form_dict = v1_batch_create_fine_tune_jobs_response.from_dict(v1_batch_create_fine_tune_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


