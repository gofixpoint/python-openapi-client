# FixpointCreateOpenAIChatInputLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[V1InputMessage]**](V1InputMessage.md) |  | [optional] 
**temperature** | **float** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tracing** | [**V1Tracing**](V1Tracing.md) |  | [optional] 
**mode** | [**V1Mode**](V1Mode.md) |  | [optional] 
**log_attributes** | [**List[V1LogAttribute]**](V1LogAttribute.md) | Optional attributes to attach to LLM input log when creating it. | [optional] 

## Example

```python
from fixpoint_openapi.models.fixpoint_create_open_ai_chat_input_log_request import FixpointCreateOpenAIChatInputLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FixpointCreateOpenAIChatInputLogRequest from a JSON string
fixpoint_create_open_ai_chat_input_log_request_instance = FixpointCreateOpenAIChatInputLogRequest.from_json(json)
# print the JSON string representation of the object
print(FixpointCreateOpenAIChatInputLogRequest.to_json())

# convert the object into a dict
fixpoint_create_open_ai_chat_input_log_request_dict = fixpoint_create_open_ai_chat_input_log_request_instance.to_dict()
# create an instance of FixpointCreateOpenAIChatInputLogRequest from a dict
fixpoint_create_open_ai_chat_input_log_request_form_dict = fixpoint_create_open_ai_chat_input_log_request.from_dict(fixpoint_create_open_ai_chat_input_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


