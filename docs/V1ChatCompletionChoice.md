# V1ChatCompletionChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**message** | [**V1OutputMessage**](V1OutputMessage.md) |  | 
**finish_reason** | **str** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_chat_completion_choice import V1ChatCompletionChoice

# TODO update the JSON string below
json = "{}"
# create an instance of V1ChatCompletionChoice from a JSON string
v1_chat_completion_choice_instance = V1ChatCompletionChoice.from_json(json)
# print the JSON string representation of the object
print(V1ChatCompletionChoice.to_json())

# convert the object into a dict
v1_chat_completion_choice_dict = v1_chat_completion_choice_instance.to_dict()
# create an instance of V1ChatCompletionChoice from a dict
v1_chat_completion_choice_form_dict = v1_chat_completion_choice.from_dict(v1_chat_completion_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


