# V1OpenAIChatOutputLogChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [optional] 
**message** | [**V1OutputMessage**](V1OutputMessage.md) |  | [optional] 
**finish_reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_open_ai_chat_output_log_choice import V1OpenAIChatOutputLogChoice

# TODO update the JSON string below
json = "{}"
# create an instance of V1OpenAIChatOutputLogChoice from a JSON string
v1_open_ai_chat_output_log_choice_instance = V1OpenAIChatOutputLogChoice.from_json(json)
# print the JSON string representation of the object
print(V1OpenAIChatOutputLogChoice.to_json())

# convert the object into a dict
v1_open_ai_chat_output_log_choice_dict = v1_open_ai_chat_output_log_choice_instance.to_dict()
# create an instance of V1OpenAIChatOutputLogChoice from a dict
v1_open_ai_chat_output_log_choice_form_dict = v1_open_ai_chat_output_log_choice.from_dict(v1_open_ai_chat_output_log_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


