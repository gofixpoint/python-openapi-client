# V1Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Supported model providers are:  - openai - anthropic | 
**temperature** | **float** |  | [optional] 
**api_key** | **str** | Optional API key for the model provider that serves this model. If you do not specify this, we will try to load in the corresponding API key stored within Fixpoint. | [optional] 
**max_tokens** | **int** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_model import V1Model

# TODO update the JSON string below
json = "{}"
# create an instance of V1Model from a JSON string
v1_model_instance = V1Model.from_json(json)
# print the JSON string representation of the object
print(V1Model.to_json())

# convert the object into a dict
v1_model_dict = v1_model_instance.to_dict()
# create an instance of V1Model from a dict
v1_model_form_dict = v1_model.from_dict(v1_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


