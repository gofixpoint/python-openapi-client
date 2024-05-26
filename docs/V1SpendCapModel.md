# V1SpendCapModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**spend_cap** | [**Fixpointv1SpendCap**](Fixpointv1SpendCap.md) |  | [optional] 
**usage_totals** | [**V1UsageTotals**](V1UsageTotals.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_spend_cap_model import V1SpendCapModel

# TODO update the JSON string below
json = "{}"
# create an instance of V1SpendCapModel from a JSON string
v1_spend_cap_model_instance = V1SpendCapModel.from_json(json)
# print the JSON string representation of the object
print(V1SpendCapModel.to_json())

# convert the object into a dict
v1_spend_cap_model_dict = v1_spend_cap_model_instance.to_dict()
# create an instance of V1SpendCapModel from a dict
v1_spend_cap_model_form_dict = v1_spend_cap_model.from_dict(v1_spend_cap_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


