# V1CreateABChatCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[V1Model]**](V1Model.md) | The models we will route all inference requests to. We return the inference response from the first model in the list to the client. | [optional] 
**experiment_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tracing** | [**V1Tracing**](V1Tracing.md) |  | [optional] 
**messages** | [**List[V1InputMessage]**](V1InputMessage.md) |  | [optional] 
**mode** | [**V1Mode**](V1Mode.md) |  | [optional] 
**log_attributes** | [**List[V1LogAttribute]**](V1LogAttribute.md) | Optional attributes to attach to LLM logs created. | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_create_ab_chat_completion_request import V1CreateABChatCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateABChatCompletionRequest from a JSON string
v1_create_ab_chat_completion_request_instance = V1CreateABChatCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateABChatCompletionRequest.to_json())

# convert the object into a dict
v1_create_ab_chat_completion_request_dict = v1_create_ab_chat_completion_request_instance.to_dict()
# create an instance of V1CreateABChatCompletionRequest from a dict
v1_create_ab_chat_completion_request_form_dict = v1_create_ab_chat_completion_request.from_dict(v1_create_ab_chat_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


