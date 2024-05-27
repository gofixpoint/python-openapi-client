# Fixpointv1SpendCap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**reset_interval** | [**V1ResetInterval**](V1ResetInterval.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.fixpointv1_spend_cap import Fixpointv1SpendCap

# TODO update the JSON string below
json = "{}"
# create an instance of Fixpointv1SpendCap from a JSON string
fixpointv1_spend_cap_instance = Fixpointv1SpendCap.from_json(json)
# print the JSON string representation of the object
print(Fixpointv1SpendCap.to_json())

# convert the object into a dict
fixpointv1_spend_cap_dict = fixpointv1_spend_cap_instance.to_dict()
# create an instance of Fixpointv1SpendCap from a dict
fixpointv1_spend_cap_form_dict = fixpointv1_spend_cap.from_dict(fixpointv1_spend_cap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


