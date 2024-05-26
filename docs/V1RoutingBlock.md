# V1RoutingBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**V1RoutingBlockType**](V1RoutingBlockType.md) |  | [optional] 
**spend_cap** | [**V1RoutingBlockSpendCap**](V1RoutingBlockSpendCap.md) |  | [optional] 
**ab** | [**RoutingBlockAB**](RoutingBlockAB.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_routing_block import V1RoutingBlock

# TODO update the JSON string below
json = "{}"
# create an instance of V1RoutingBlock from a JSON string
v1_routing_block_instance = V1RoutingBlock.from_json(json)
# print the JSON string representation of the object
print(V1RoutingBlock.to_json())

# convert the object into a dict
v1_routing_block_dict = v1_routing_block_instance.to_dict()
# create an instance of V1RoutingBlock from a dict
v1_routing_block_form_dict = v1_routing_block.from_dict(v1_routing_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


