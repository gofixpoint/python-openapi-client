# ToolCallFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**arguments** | **str** | A JSON string of the arguments. Note, it&#39;s possible that the AI does not generate valid JSON. | [optional] 

## Example

```python
from fixpoint_openapi.models.tool_call_function import ToolCallFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallFunction from a JSON string
tool_call_function_instance = ToolCallFunction.from_json(json)
# print the JSON string representation of the object
print(ToolCallFunction.to_json())

# convert the object into a dict
tool_call_function_dict = tool_call_function_instance.to_dict()
# create an instance of ToolCallFunction from a dict
tool_call_function_form_dict = tool_call_function.from_dict(tool_call_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


