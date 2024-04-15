# V1InputMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_input_message import V1InputMessage

# TODO update the JSON string below
json = "{}"
# create an instance of V1InputMessage from a JSON string
v1_input_message_instance = V1InputMessage.from_json(json)
# print the JSON string representation of the object
print(V1InputMessage.to_json())

# convert the object into a dict
v1_input_message_dict = v1_input_message_instance.to_dict()
# create an instance of V1InputMessage from a dict
v1_input_message_form_dict = v1_input_message.from_dict(v1_input_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


