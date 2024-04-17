# V1ChatCompletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**external_id** | **str** |  | [optional] 
**model** | **str** | The model used for inference. Normally, we identify the model name with &#x60;model_name&#x60; field, but for OpenAI compatibility we just use &#x60;model&#x60; here. | 
**tracing** | [**V1Tracing**](V1Tracing.md) |  | [optional] 
**choices** | [**List[V1ChatCompletionChoice]**](V1ChatCompletionChoice.md) |  | 
**usage** | [**V1ChatCompletionUsage**](V1ChatCompletionUsage.md) |  | 

## Example

```python
from fixpoint_openapi.models.v1_chat_completion import V1ChatCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of V1ChatCompletion from a JSON string
v1_chat_completion_instance = V1ChatCompletion.from_json(json)
# print the JSON string representation of the object
print(V1ChatCompletion.to_json())

# convert the object into a dict
v1_chat_completion_dict = v1_chat_completion_instance.to_dict()
# create an instance of V1ChatCompletion from a dict
v1_chat_completion_form_dict = v1_chat_completion.from_dict(v1_chat_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


