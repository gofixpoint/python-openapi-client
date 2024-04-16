# FixpointCreateOpenAIChatInputLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_name** | **str** |  | [optional] 
**messages** | [**List[V1InputMessage]**](V1InputMessage.md) |  | [optional] 
**temperature** | **float** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**mode** | [**V1Mode**](V1Mode.md) |  | [optional] 

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


