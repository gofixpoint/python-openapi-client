# V1OpenAIChatOutputLogUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **int** |  | [optional] 
**completion_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_open_ai_chat_output_log_usage import V1OpenAIChatOutputLogUsage

# TODO update the JSON string below
json = "{}"
# create an instance of V1OpenAIChatOutputLogUsage from a JSON string
v1_open_ai_chat_output_log_usage_instance = V1OpenAIChatOutputLogUsage.from_json(json)
# print the JSON string representation of the object
print(V1OpenAIChatOutputLogUsage.to_json())

# convert the object into a dict
v1_open_ai_chat_output_log_usage_dict = v1_open_ai_chat_output_log_usage_instance.to_dict()
# create an instance of V1OpenAIChatOutputLogUsage from a dict
v1_open_ai_chat_output_log_usage_form_dict = v1_open_ai_chat_output_log_usage.from_dict(v1_open_ai_chat_output_log_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


