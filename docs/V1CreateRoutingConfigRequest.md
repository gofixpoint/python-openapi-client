# V1CreateRoutingConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**blocks** | [**List[V1RoutingBlock]**](V1RoutingBlock.md) |  | [optional] 
**models** | [**List[V1SpendCapModel]**](V1SpendCapModel.md) |  | [optional] 
**fallback_strategy** | [**V1FallbackStrategy**](V1FallbackStrategy.md) |  | [optional] 
**terminal_state** | [**V1TerminalState**](V1TerminalState.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_create_routing_config_request import V1CreateRoutingConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateRoutingConfigRequest from a JSON string
v1_create_routing_config_request_instance = V1CreateRoutingConfigRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateRoutingConfigRequest.to_json())

# convert the object into a dict
v1_create_routing_config_request_dict = v1_create_routing_config_request_instance.to_dict()
# create an instance of V1CreateRoutingConfigRequest from a dict
v1_create_routing_config_request_form_dict = v1_create_routing_config_request.from_dict(v1_create_routing_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


