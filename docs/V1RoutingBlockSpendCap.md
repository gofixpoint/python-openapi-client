# V1RoutingBlockSpendCap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_strategy** | [**V1FallbackStrategy**](V1FallbackStrategy.md) |  | [optional] 
**terminal_state** | [**V1TerminalState**](V1TerminalState.md) |  | [optional] 
**models** | [**List[V1SpendCapModel]**](V1SpendCapModel.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_routing_block_spend_cap import V1RoutingBlockSpendCap

# TODO update the JSON string below
json = "{}"
# create an instance of V1RoutingBlockSpendCap from a JSON string
v1_routing_block_spend_cap_instance = V1RoutingBlockSpendCap.from_json(json)
# print the JSON string representation of the object
print(V1RoutingBlockSpendCap.to_json())

# convert the object into a dict
v1_routing_block_spend_cap_dict = v1_routing_block_spend_cap_instance.to_dict()
# create an instance of V1RoutingBlockSpendCap from a dict
v1_routing_block_spend_cap_form_dict = v1_routing_block_spend_cap.from_dict(v1_routing_block_spend_cap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


