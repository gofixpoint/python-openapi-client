# V1MultiLLMChatCompletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This is the ID of the multi-LLM chat completion. It is also the LLM log ID/name of the input/output log for the primary LLM (aka the completion we return to the client).  If we failed to log the request but succeeded in making the chat completion, we will still return a success, but the \&quot;id\&quot; will be empty. In that case, you can use the primary_external_id to find the logged completions. | [readonly] 
**primary_external_id** | **str** | The external ID of the first model in the multi-LLM inference request. This is the primary model, whose response we return to the client. We can only return the first model ID because other model inference occurs asynchronously. | [optional] 
**model_names** | **List[str]** |  | 
**display_model** | **int** | The index of the model displayed. | [optional] 
**tracing** | [**V1Tracing**](V1Tracing.md) |  | [optional] 
**completion** | [**V1ChatCompletion**](V1ChatCompletion.md) |  | 
**mode** | [**V1Mode**](V1Mode.md) |  | 

## Example

```python
from fixpoint_openapi.models.v1_multi_llm_chat_completion import V1MultiLLMChatCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of V1MultiLLMChatCompletion from a JSON string
v1_multi_llm_chat_completion_instance = V1MultiLLMChatCompletion.from_json(json)
# print the JSON string representation of the object
print(V1MultiLLMChatCompletion.to_json())

# convert the object into a dict
v1_multi_llm_chat_completion_dict = v1_multi_llm_chat_completion_instance.to_dict()
# create an instance of V1MultiLLMChatCompletion from a dict
v1_multi_llm_chat_completion_form_dict = v1_multi_llm_chat_completion.from_dict(v1_multi_llm_chat_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


