# FixpointCreateOpenAIChatOutputLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_name** | **str** |  | [optional] 
**openai_id** | **str** |  | [optional] 
**session_name** | **str** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**mode** | [**V1Mode**](V1Mode.md) |  | [optional] 
**choices** | [**List[V1OpenAIChatOutputLogChoice]**](V1OpenAIChatOutputLogChoice.md) |  | [optional] 
**usage** | [**V1OpenAIChatOutputLogUsage**](V1OpenAIChatOutputLogUsage.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.fixpoint_create_open_ai_chat_output_log_request import FixpointCreateOpenAIChatOutputLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FixpointCreateOpenAIChatOutputLogRequest from a JSON string
fixpoint_create_open_ai_chat_output_log_request_instance = FixpointCreateOpenAIChatOutputLogRequest.from_json(json)
# print the JSON string representation of the object
print(FixpointCreateOpenAIChatOutputLogRequest.to_json())

# convert the object into a dict
fixpoint_create_open_ai_chat_output_log_request_dict = fixpoint_create_open_ai_chat_output_log_request_instance.to_dict()
# create an instance of FixpointCreateOpenAIChatOutputLogRequest from a dict
fixpoint_create_open_ai_chat_output_log_request_form_dict = fixpoint_create_open_ai_chat_output_log_request.from_dict(fixpoint_create_open_ai_chat_output_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


