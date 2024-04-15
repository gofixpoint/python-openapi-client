# V1ToolCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**function** | [**ToolCallFunction**](ToolCallFunction.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_tool_call import V1ToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of V1ToolCall from a JSON string
v1_tool_call_instance = V1ToolCall.from_json(json)
# print the JSON string representation of the object
print(V1ToolCall.to_json())

# convert the object into a dict
v1_tool_call_dict = v1_tool_call_instance.to_dict()
# create an instance of V1ToolCall from a dict
v1_tool_call_form_dict = v1_tool_call.from_dict(v1_tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


