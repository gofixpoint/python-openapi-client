# V1OutputMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**tool_calls** | [**List[V1ToolCall]**](V1ToolCall.md) | Optional tool calls, if the model called any. | [optional] 

## Example

```python
from openapi_client.models.v1_output_message import V1OutputMessage

# TODO update the JSON string below
json = "{}"
# create an instance of V1OutputMessage from a JSON string
v1_output_message_instance = V1OutputMessage.from_json(json)
# print the JSON string representation of the object
print(V1OutputMessage.to_json())

# convert the object into a dict
v1_output_message_dict = v1_output_message_instance.to_dict()
# create an instance of V1OutputMessage from a dict
v1_output_message_form_dict = v1_output_message.from_dict(v1_output_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


