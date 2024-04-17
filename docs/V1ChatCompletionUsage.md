# V1ChatCompletionUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **int** |  | [optional] 
**completion_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_chat_completion_usage import V1ChatCompletionUsage

# TODO update the JSON string below
json = "{}"
# create an instance of V1ChatCompletionUsage from a JSON string
v1_chat_completion_usage_instance = V1ChatCompletionUsage.from_json(json)
# print the JSON string representation of the object
print(V1ChatCompletionUsage.to_json())

# convert the object into a dict
v1_chat_completion_usage_dict = v1_chat_completion_usage_instance.to_dict()
# create an instance of V1ChatCompletionUsage from a dict
v1_chat_completion_usage_form_dict = v1_chat_completion_usage.from_dict(v1_chat_completion_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


