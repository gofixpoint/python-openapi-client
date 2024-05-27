# V1TuningConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_alias** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**hyperparameters** | [**V1Hyperparameters**](V1Hyperparameters.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_tuning_configuration import V1TuningConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1TuningConfiguration from a JSON string
v1_tuning_configuration_instance = V1TuningConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1TuningConfiguration.to_json())

# convert the object into a dict
v1_tuning_configuration_dict = v1_tuning_configuration_instance.to_dict()
# create an instance of V1TuningConfiguration from a dict
v1_tuning_configuration_form_dict = v1_tuning_configuration.from_dict(v1_tuning_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


