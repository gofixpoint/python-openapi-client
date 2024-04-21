# V1TracingFilters

Filter LLM logs to session, trace, or span info.  The top-level filter attributes (session_ids, trace_ids, etc.) combine with the \"AND\" filter, // while within a given field such as \"session_ids\", the items combine with the \"OR\" filter.  For example:    TracingFilters = {     session_ids: [\"session1\", \"session2\"],     trace_ids: [\"trace1\", \"trace2\"],   }  This will match all LLM logs that have either \"session1\" or \"session2\", and who also have either \"trace1\" or \"trace2\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_ids** | **List[str]** |  | [optional] 
**trace_ids** | **List[str]** |  | [optional] 
**span_ids** | **List[str]** |  | [optional] 
**parent_span_ids** | **List[str]** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_tracing_filters import V1TracingFilters

# TODO update the JSON string below
json = "{}"
# create an instance of V1TracingFilters from a JSON string
v1_tracing_filters_instance = V1TracingFilters.from_json(json)
# print the JSON string representation of the object
print(V1TracingFilters.to_json())

# convert the object into a dict
v1_tracing_filters_dict = v1_tracing_filters_instance.to_dict()
# create an instance of V1TracingFilters from a dict
v1_tracing_filters_form_dict = v1_tracing_filters.from_dict(v1_tracing_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


