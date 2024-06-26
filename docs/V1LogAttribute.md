# V1LogAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**log_name** | **str** | The log_name should be the name of the input/output log pair or the name of the input log. Logs get attached to the LLM log input/output pair, which are identified by the input log name. | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_log_attribute import V1LogAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of V1LogAttribute from a JSON string
v1_log_attribute_instance = V1LogAttribute.from_json(json)
# print the JSON string representation of the object
print(V1LogAttribute.to_json())

# convert the object into a dict
v1_log_attribute_dict = v1_log_attribute_instance.to_dict()
# create an instance of V1LogAttribute from a dict
v1_log_attribute_form_dict = v1_log_attribute.from_dict(v1_log_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


