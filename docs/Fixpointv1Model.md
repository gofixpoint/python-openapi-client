# Fixpointv1Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**spend_cap** | [**V1SpendCap**](V1SpendCap.md) |  | [optional] 
**usage_totals** | [**V1UsageTotals**](V1UsageTotals.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.fixpointv1_model import Fixpointv1Model

# TODO update the JSON string below
json = "{}"
# create an instance of Fixpointv1Model from a JSON string
fixpointv1_model_instance = Fixpointv1Model.from_json(json)
# print the JSON string representation of the object
print(Fixpointv1Model.to_json())

# convert the object into a dict
fixpointv1_model_dict = fixpointv1_model_instance.to_dict()
# create an instance of Fixpointv1Model from a dict
fixpointv1_model_form_dict = fixpointv1_model.from_dict(fixpointv1_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


