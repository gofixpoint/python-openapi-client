# V1AbChatCompletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This is the ID of the multi-LLM chat completion. | [readonly] 
**primary_external_id** | **str** | The external ID of the chat completion. | [optional] 
**model** | [**V1Model**](V1Model.md) |  | 
**tracing** | [**V1Tracing**](V1Tracing.md) |  | [optional] 
**completion** | [**V1ChatCompletion**](V1ChatCompletion.md) |  | 
**mode** | [**V1Mode**](V1Mode.md) |  | 

## Example

```python
from fixpoint_openapi.models.v1_ab_chat_completion import V1AbChatCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of V1AbChatCompletion from a JSON string
v1_ab_chat_completion_instance = V1AbChatCompletion.from_json(json)
# print the JSON string representation of the object
print(V1AbChatCompletion.to_json())

# convert the object into a dict
v1_ab_chat_completion_dict = v1_ab_chat_completion_instance.to_dict()
# create an instance of V1AbChatCompletion from a dict
v1_ab_chat_completion_form_dict = v1_ab_chat_completion.from_dict(v1_ab_chat_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


