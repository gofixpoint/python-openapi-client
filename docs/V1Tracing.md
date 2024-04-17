# V1Tracing

A session ties together multiple chat completions for a user or system session. For example, when a user logs into ChatGPT and has a conversation, that whole conversation thread is called a session.  A trace represents a chain of inference requests. Think similarly to OpenTelemetry and OpenTracing. A session can have multiple traces. The difference, is that the trace is one \"request\" from an end-user that might have multiple inference calls, while a \"session\" consists of multiple inference requests.  A trace contains multiple spans, which are one step of the trace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**span_id** | **str** |  | [optional] 
**parent_span_id** | **str** |  | [optional] 

## Example

```python
from fixpoint_openapi.models.v1_tracing import V1Tracing

# TODO update the JSON string below
json = "{}"
# create an instance of V1Tracing from a JSON string
v1_tracing_instance = V1Tracing.from_json(json)
# print the JSON string representation of the object
print(V1Tracing.to_json())

# convert the object into a dict
v1_tracing_dict = v1_tracing_instance.to_dict()
# create an instance of V1Tracing from a dict
v1_tracing_form_dict = v1_tracing.from_dict(v1_tracing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


