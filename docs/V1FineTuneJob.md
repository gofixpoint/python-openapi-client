# V1FineTuneJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**set_id** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**status** | [**V1FineTuneStatus**](V1FineTuneStatus.md) |  | [optional] 
**hyperparameters** | [**V1Hyperparameters**](V1Hyperparameters.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**secret_alias** | **str** |  | [optional] 
**fine_tuned_model** | **str** |  | [optional] 
**provider_job_id** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_fine_tune_job import V1FineTuneJob

# TODO update the JSON string below
json = "{}"
# create an instance of V1FineTuneJob from a JSON string
v1_fine_tune_job_instance = V1FineTuneJob.from_json(json)
# print the JSON string representation of the object
print(V1FineTuneJob.to_json())

# convert the object into a dict
v1_fine_tune_job_dict = v1_fine_tune_job_instance.to_dict()
# create an instance of V1FineTuneJob from a dict
v1_fine_tune_job_form_dict = v1_fine_tune_job.from_dict(v1_fine_tune_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


