# RoutingBlockAB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_id** | **str** |  | [optional] 
**models** | [**List[V1Model]**](V1Model.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.routing_block_ab import RoutingBlockAB

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingBlockAB from a JSON string
routing_block_ab_instance = RoutingBlockAB.from_json(json)
# print the JSON string representation of the object
print(RoutingBlockAB.to_json())

# convert the object into a dict
routing_block_ab_dict = routing_block_ab_instance.to_dict()
# create an instance of RoutingBlockAB from a dict
routing_block_ab_form_dict = routing_block_ab.from_dict(routing_block_ab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


