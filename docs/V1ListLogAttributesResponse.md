# V1ListLogAttributesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_attributes** | [**List[V1LogAttribute]**](V1LogAttribute.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_list_log_attributes_response import V1ListLogAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListLogAttributesResponse from a JSON string
v1_list_log_attributes_response_instance = V1ListLogAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(V1ListLogAttributesResponse.to_json())

# convert the object into a dict
v1_list_log_attributes_response_dict = v1_list_log_attributes_response_instance.to_dict()
# create an instance of V1ListLogAttributesResponse from a dict
v1_list_log_attributes_response_form_dict = v1_list_log_attributes_response.from_dict(v1_list_log_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


