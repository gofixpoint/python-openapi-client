# Llmproxyv1Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**spend_cap** | [**V1SpendCap**](V1SpendCap.md) |  | [optional] 
**usage_totals** | [**V1UsageTotals**](V1UsageTotals.md) |  | [optional] 

## Example

```python
from fixpoint_openapi.models.llmproxyv1_model import Llmproxyv1Model

# TODO update the JSON string below
json = "{}"
# create an instance of Llmproxyv1Model from a JSON string
llmproxyv1_model_instance = Llmproxyv1Model.from_json(json)
# print the JSON string representation of the object
print(Llmproxyv1Model.to_json())

# convert the object into a dict
llmproxyv1_model_dict = llmproxyv1_model_instance.to_dict()
# create an instance of Llmproxyv1Model from a dict
llmproxyv1_model_form_dict = llmproxyv1_model.from_dict(llmproxyv1_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


