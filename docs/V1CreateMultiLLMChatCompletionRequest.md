# V1CreateMultiLLMChatCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[V1CreateMultiLLMChatCompletionRequestModel]**](V1CreateMultiLLMChatCompletionRequestModel.md) | The models we will route all inference requests to. We return the inference response from the first model in the list to the client. | [optional] 
**tracing** | [**V1Tracing**](V1Tracing.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**messages** | [**List[V1InputMessage]**](V1InputMessage.md) |  | [optional] 
**mode** | [**V1Mode**](V1Mode.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_create_multi_llm_chat_completion_request import V1CreateMultiLLMChatCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateMultiLLMChatCompletionRequest from a JSON string
v1_create_multi_llm_chat_completion_request_instance = V1CreateMultiLLMChatCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateMultiLLMChatCompletionRequest.to_json())

# convert the object into a dict
v1_create_multi_llm_chat_completion_request_dict = v1_create_multi_llm_chat_completion_request_instance.to_dict()
# create an instance of V1CreateMultiLLMChatCompletionRequest from a dict
v1_create_multi_llm_chat_completion_request_form_dict = v1_create_multi_llm_chat_completion_request.from_dict(v1_create_multi_llm_chat_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


