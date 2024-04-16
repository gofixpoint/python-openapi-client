# FixpointUpdateSpendingTotalsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[Fixpointv1Model]**](Fixpointv1Model.md) | Spend cap and totals for each model are deltas so that the client cannot alter usage metrics. | [optional] 

## Example

```python
from fixpoint_openapi.models.fixpoint_update_spending_totals_request import FixpointUpdateSpendingTotalsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FixpointUpdateSpendingTotalsRequest from a JSON string
fixpoint_update_spending_totals_request_instance = FixpointUpdateSpendingTotalsRequest.from_json(json)
# print the JSON string representation of the object
print(FixpointUpdateSpendingTotalsRequest.to_json())

# convert the object into a dict
fixpoint_update_spending_totals_request_dict = fixpoint_update_spending_totals_request_instance.to_dict()
# create an instance of FixpointUpdateSpendingTotalsRequest from a dict
fixpoint_update_spending_totals_request_form_dict = fixpoint_update_spending_totals_request.from_dict(fixpoint_update_spending_totals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


