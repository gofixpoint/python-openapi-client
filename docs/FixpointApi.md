# fixpoint_openapi.FixpointApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fixpoint_create_api_secret**](FixpointApi.md#fixpoint_create_api_secret) | **POST** /v1/api_secrets | Store LLM inference API secret
[**fixpoint_create_app_logs**](FixpointApi.md#fixpoint_create_app_logs) | **POST** /v1/app_logs | Create application logs
[**fixpoint_create_dataset**](FixpointApi.md#fixpoint_create_dataset) | **POST** /v1/datasets | Create LLM dataset
[**fixpoint_create_likes**](FixpointApi.md#fixpoint_create_likes) | **POST** /v1/likes | Add LLM log feedback (\&quot;likes\&quot;)
[**fixpoint_create_log_attribute**](FixpointApi.md#fixpoint_create_log_attribute) | **POST** /v1/attributes | Attach attribute to LLM log
[**fixpoint_create_multi_llm_chat_completion**](FixpointApi.md#fixpoint_create_multi_llm_chat_completion) | **POST** /v1/chat/completions/multi_llm | 
[**fixpoint_create_open_ai_chat_input_log**](FixpointApi.md#fixpoint_create_open_ai_chat_input_log) | **POST** /v1/openai_chats/{modelName}/input_logs | Create an LLM input log
[**fixpoint_create_open_ai_chat_output_log**](FixpointApi.md#fixpoint_create_open_ai_chat_output_log) | **POST** /v1/openai_chats/{modelName}/output_logs | Create an LLM output log
[**fixpoint_create_routing_config**](FixpointApi.md#fixpoint_create_routing_config) | **POST** /v1/routing_configs | Create LLM routing config
[**fixpoint_delete_log_attribute**](FixpointApi.md#fixpoint_delete_log_attribute) | **DELETE** /v1/attributes/{name} | Remove LLM log attribute
[**fixpoint_list_api_secrets**](FixpointApi.md#fixpoint_list_api_secrets) | **GET** /v1/api_secrets | List LLM inference API secrets
[**fixpoint_list_app_logs**](FixpointApi.md#fixpoint_list_app_logs) | **GET** /v1/app_logs | List application logs
[**fixpoint_list_datasets**](FixpointApi.md#fixpoint_list_datasets) | **GET** /v1/datasets | List LLM datasets
[**fixpoint_list_likes**](FixpointApi.md#fixpoint_list_likes) | **GET** /v1/likes | List LLM log feedback (\&quot;likes\&quot;)
[**fixpoint_list_log_attributes**](FixpointApi.md#fixpoint_list_log_attributes) | **GET** /v1/attributes | List attributes on an LLM log
[**fixpoint_list_open_ai_chat_logs**](FixpointApi.md#fixpoint_list_open_ai_chat_logs) | **GET** /v1/{parent}/logs | List LLM logs
[**fixpoint_list_routing_configs**](FixpointApi.md#fixpoint_list_routing_configs) | **GET** /v1/routing_configs | List LLM routing configs
[**fixpoint_post_dataset_logs**](FixpointApi.md#fixpoint_post_dataset_logs) | **POST** /v1/datasets/{name}/logs | Add logs to a dataset
[**fixpoint_update_spending_totals**](FixpointApi.md#fixpoint_update_spending_totals) | **PATCH** /v1/routing_configs/{routeConfigId} | Update routing config spending totals


# **fixpoint_create_api_secret**
> V1ApiSecret fixpoint_create_api_secret(body)

Store LLM inference API secret

This lets Fixpoint make select inference interactions on your behalf, such as running a fine-tuning operation or running LLM evaluations on monitored LLM logs.

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_api_secret import V1ApiSecret
from fixpoint_openapi.models.v1_create_api_secret_request import V1CreateApiSecretRequest
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    body = fixpoint_openapi.V1CreateApiSecretRequest() # V1CreateApiSecretRequest | 

    try:
        # Store LLM inference API secret
        api_response = api_instance.fixpoint_create_api_secret(body)
        print("The response of FixpointApi->fixpoint_create_api_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_api_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateApiSecretRequest**](V1CreateApiSecretRequest.md)|  | 

### Return type

[**V1ApiSecret**](V1ApiSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_app_logs**
> V1CreateAppLogsResponse fixpoint_create_app_logs(body)

Create application logs

Create 1 or more application logs, which you can attach to an LLM log via a trace_id. This is useful when you want to see what was going on in the rest of your application when an LLM inference request was made.

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_create_app_logs_request import V1CreateAppLogsRequest
from fixpoint_openapi.models.v1_create_app_logs_response import V1CreateAppLogsResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    body = fixpoint_openapi.V1CreateAppLogsRequest() # V1CreateAppLogsRequest | 

    try:
        # Create application logs
        api_response = api_instance.fixpoint_create_app_logs(body)
        print("The response of FixpointApi->fixpoint_create_app_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_app_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateAppLogsRequest**](V1CreateAppLogsRequest.md)|  | 

### Return type

[**V1CreateAppLogsResponse**](V1CreateAppLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_dataset**
> V1CreateDatasetResponse fixpoint_create_dataset(body)

Create LLM dataset

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_create_dataset_request import V1CreateDatasetRequest
from fixpoint_openapi.models.v1_create_dataset_response import V1CreateDatasetResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    body = fixpoint_openapi.V1CreateDatasetRequest() # V1CreateDatasetRequest | 

    try:
        # Create LLM dataset
        api_response = api_instance.fixpoint_create_dataset(body)
        print("The response of FixpointApi->fixpoint_create_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateDatasetRequest**](V1CreateDatasetRequest.md)|  | 

### Return type

[**V1CreateDatasetResponse**](V1CreateDatasetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_likes**
> V1CreateLikesResponse fixpoint_create_likes(body)

Add LLM log feedback (\"likes\")

Create \"likes\" or user feedback for an LLM log. The user feedback can be from an internal user (such as LL prompt engineer) or an external end-user.

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_create_likes_request import V1CreateLikesRequest
from fixpoint_openapi.models.v1_create_likes_response import V1CreateLikesResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    body = fixpoint_openapi.V1CreateLikesRequest() # V1CreateLikesRequest | 

    try:
        # Add LLM log feedback (\"likes\")
        api_response = api_instance.fixpoint_create_likes(body)
        print("The response of FixpointApi->fixpoint_create_likes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_likes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateLikesRequest**](V1CreateLikesRequest.md)|  | 

### Return type

[**V1CreateLikesResponse**](V1CreateLikesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_log_attribute**
> V1CreateLogAttributeResponse fixpoint_create_log_attribute(body)

Attach attribute to LLM log

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_create_log_attribute_request import V1CreateLogAttributeRequest
from fixpoint_openapi.models.v1_create_log_attribute_response import V1CreateLogAttributeResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    body = fixpoint_openapi.V1CreateLogAttributeRequest() # V1CreateLogAttributeRequest | 

    try:
        # Attach attribute to LLM log
        api_response = api_instance.fixpoint_create_log_attribute(body)
        print("The response of FixpointApi->fixpoint_create_log_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_log_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateLogAttributeRequest**](V1CreateLogAttributeRequest.md)|  | 

### Return type

[**V1CreateLogAttributeResponse**](V1CreateLogAttributeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_multi_llm_chat_completion**
> V1MultiLLMChatCompletion fixpoint_create_multi_llm_chat_completion(body)



### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_create_multi_llm_chat_completion_request import V1CreateMultiLLMChatCompletionRequest
from fixpoint_openapi.models.v1_multi_llm_chat_completion import V1MultiLLMChatCompletion
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    body = fixpoint_openapi.V1CreateMultiLLMChatCompletionRequest() # V1CreateMultiLLMChatCompletionRequest | 

    try:
        api_response = api_instance.fixpoint_create_multi_llm_chat_completion(body)
        print("The response of FixpointApi->fixpoint_create_multi_llm_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_multi_llm_chat_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateMultiLLMChatCompletionRequest**](V1CreateMultiLLMChatCompletionRequest.md)|  | 

### Return type

[**V1MultiLLMChatCompletion**](V1MultiLLMChatCompletion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_open_ai_chat_input_log**
> V1OpenAIChatInputLog fixpoint_create_open_ai_chat_input_log(model_name, body)

Create an LLM input log

Store an LLM inference request's input in Fixpoint (aka the \"LLM input log\").

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.fixpoint_create_open_ai_chat_input_log_request import FixpointCreateOpenAIChatInputLogRequest
from fixpoint_openapi.models.v1_open_ai_chat_input_log import V1OpenAIChatInputLog
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    model_name = 'model_name_example' # str | 
    body = fixpoint_openapi.FixpointCreateOpenAIChatInputLogRequest() # FixpointCreateOpenAIChatInputLogRequest | 

    try:
        # Create an LLM input log
        api_response = api_instance.fixpoint_create_open_ai_chat_input_log(model_name, body)
        print("The response of FixpointApi->fixpoint_create_open_ai_chat_input_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_open_ai_chat_input_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 
 **body** | [**FixpointCreateOpenAIChatInputLogRequest**](FixpointCreateOpenAIChatInputLogRequest.md)|  | 

### Return type

[**V1OpenAIChatInputLog**](V1OpenAIChatInputLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_open_ai_chat_output_log**
> V1OpenAIChatOutputLog fixpoint_create_open_ai_chat_output_log(model_name, body)

Create an LLM output log

Store an LLM inference request's output in Fixpoint (aka the \"LLM output log\").

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.fixpoint_create_open_ai_chat_output_log_request import FixpointCreateOpenAIChatOutputLogRequest
from fixpoint_openapi.models.v1_open_ai_chat_output_log import V1OpenAIChatOutputLog
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    model_name = 'model_name_example' # str | 
    body = fixpoint_openapi.FixpointCreateOpenAIChatOutputLogRequest() # FixpointCreateOpenAIChatOutputLogRequest | 

    try:
        # Create an LLM output log
        api_response = api_instance.fixpoint_create_open_ai_chat_output_log(model_name, body)
        print("The response of FixpointApi->fixpoint_create_open_ai_chat_output_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_open_ai_chat_output_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 
 **body** | [**FixpointCreateOpenAIChatOutputLogRequest**](FixpointCreateOpenAIChatOutputLogRequest.md)|  | 

### Return type

[**V1OpenAIChatOutputLog**](V1OpenAIChatOutputLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_create_routing_config**
> V1RoutingConfig fixpoint_create_routing_config(body)

Create LLM routing config

Creates an LLM inference routing config so you can dynamically control to which LLM models or inference providers Fixpoint sends LLM inference requests.  Routing configs can:  - Have configurable spending caps per model

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_create_routing_config_request import V1CreateRoutingConfigRequest
from fixpoint_openapi.models.v1_routing_config import V1RoutingConfig
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    body = fixpoint_openapi.V1CreateRoutingConfigRequest() # V1CreateRoutingConfigRequest | 

    try:
        # Create LLM routing config
        api_response = api_instance.fixpoint_create_routing_config(body)
        print("The response of FixpointApi->fixpoint_create_routing_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_create_routing_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateRoutingConfigRequest**](V1CreateRoutingConfigRequest.md)|  | 

### Return type

[**V1RoutingConfig**](V1RoutingConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_delete_log_attribute**
> V1DeleteLogAttributeResponse fixpoint_delete_log_attribute(name)

Remove LLM log attribute

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_delete_log_attribute_response import V1DeleteLogAttributeResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    name = 'name_example' # str | 

    try:
        # Remove LLM log attribute
        api_response = api_instance.fixpoint_delete_log_attribute(name)
        print("The response of FixpointApi->fixpoint_delete_log_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_delete_log_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**V1DeleteLogAttributeResponse**](V1DeleteLogAttributeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_list_api_secrets**
> V1ListApiSecretsResponse fixpoint_list_api_secrets()

List LLM inference API secrets

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_list_api_secrets_response import V1ListApiSecretsResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)

    try:
        # List LLM inference API secrets
        api_response = api_instance.fixpoint_list_api_secrets()
        print("The response of FixpointApi->fixpoint_list_api_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_list_api_secrets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ListApiSecretsResponse**](V1ListApiSecretsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_list_app_logs**
> V1ListAppLogsResponse fixpoint_list_app_logs(trace_id=trace_id)

List application logs

List application logs stored in Fixpoint.

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_list_app_logs_response import V1ListAppLogsResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    trace_id = 'trace_id_example' # str |  (optional)

    try:
        # List application logs
        api_response = api_instance.fixpoint_list_app_logs(trace_id=trace_id)
        print("The response of FixpointApi->fixpoint_list_app_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_list_app_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**|  | [optional] 

### Return type

[**V1ListAppLogsResponse**](V1ListAppLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_list_datasets**
> V1ListDatasetsResponse fixpoint_list_datasets(dataset_name=dataset_name, mode=mode)

List LLM datasets

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_list_datasets_response import V1ListDatasetsResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    dataset_name = 'dataset_name_example' # str |  (optional)
    mode = 'MODE_UNSPECIFIED' # str |  (optional) (default to 'MODE_UNSPECIFIED')

    try:
        # List LLM datasets
        api_response = api_instance.fixpoint_list_datasets(dataset_name=dataset_name, mode=mode)
        print("The response of FixpointApi->fixpoint_list_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_list_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | [optional] 
 **mode** | **str**|  | [optional] [default to &#39;MODE_UNSPECIFIED&#39;]

### Return type

[**V1ListDatasetsResponse**](V1ListDatasetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_list_likes**
> V1ListLikesResponse fixpoint_list_likes(page_size=page_size, log_name=log_name, user_id=user_id, origin=origin, thumbs_reaction=thumbs_reaction)

List LLM log feedback (\"likes\")

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_list_likes_response import V1ListLikesResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    page_size = 56 # int |  (optional)
    log_name = 'log_name_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    origin = 'ORIGIN_UNSPECIFIED' # str |  (optional) (default to 'ORIGIN_UNSPECIFIED')
    thumbs_reaction = 'THUMBS_UNSPECIFIED' # str |  (optional) (default to 'THUMBS_UNSPECIFIED')

    try:
        # List LLM log feedback (\"likes\")
        api_response = api_instance.fixpoint_list_likes(page_size=page_size, log_name=log_name, user_id=user_id, origin=origin, thumbs_reaction=thumbs_reaction)
        print("The response of FixpointApi->fixpoint_list_likes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_list_likes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**|  | [optional] 
 **log_name** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] [default to &#39;ORIGIN_UNSPECIFIED&#39;]
 **thumbs_reaction** | **str**|  | [optional] [default to &#39;THUMBS_UNSPECIFIED&#39;]

### Return type

[**V1ListLikesResponse**](V1ListLikesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_list_log_attributes**
> V1ListLogAttributesResponse fixpoint_list_log_attributes(log_name=log_name)

List attributes on an LLM log

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_list_log_attributes_response import V1ListLogAttributesResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    log_name = 'log_name_example' # str |  (optional)

    try:
        # List attributes on an LLM log
        api_response = api_instance.fixpoint_list_log_attributes(log_name=log_name)
        print("The response of FixpointApi->fixpoint_list_log_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_list_log_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_name** | **str**|  | [optional] 

### Return type

[**V1ListLogAttributesResponse**](V1ListLogAttributesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_list_open_ai_chat_logs**
> V1ListOpenAIChatLogsResponse fixpoint_list_open_ai_chat_logs(parent, page_size=page_size, page_token=page_token, filters_relative_datetime_filters_from_s=filters_relative_datetime_filters_from_s, filters_userfeedback_filter_thumbs_reaction=filters_userfeedback_filter_thumbs_reaction, filters_attribute_filters_keys=filters_attribute_filters_keys, filters_attribute_filters_values=filters_attribute_filters_values, filters_dataset_filters_dataset_names=filters_dataset_filters_dataset_names, mode=mode, count_entries=count_entries)

List LLM logs

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_list_open_ai_chat_logs_response import V1ListOpenAIChatLogsResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    parent = 'parent_example' # str | The parent resource collection. In this case, \"/openai_chats/{model_name}\".
    page_size = 56 # int |  (optional)
    page_token = 'page_token_example' # str |  (optional)
    filters_relative_datetime_filters_from_s = 'filters_relative_datetime_filters_from_s_example' # str | Number of seconds from current datetime (optional)
    filters_userfeedback_filter_thumbs_reaction = 'THUMBS_UNSPECIFIED' # str |  (optional) (default to 'THUMBS_UNSPECIFIED')
    filters_attribute_filters_keys = ['filters_attribute_filters_keys_example'] # List[str] |  (optional)
    filters_attribute_filters_values = ['filters_attribute_filters_values_example'] # List[str] |  (optional)
    filters_dataset_filters_dataset_names = ['filters_dataset_filters_dataset_names_example'] # List[str] |  (optional)
    mode = 'MODE_UNSPECIFIED' # str |  (optional) (default to 'MODE_UNSPECIFIED')
    count_entries = True # bool | Whether to also return a count of all the entries matching the list query. (optional)

    try:
        # List LLM logs
        api_response = api_instance.fixpoint_list_open_ai_chat_logs(parent, page_size=page_size, page_token=page_token, filters_relative_datetime_filters_from_s=filters_relative_datetime_filters_from_s, filters_userfeedback_filter_thumbs_reaction=filters_userfeedback_filter_thumbs_reaction, filters_attribute_filters_keys=filters_attribute_filters_keys, filters_attribute_filters_values=filters_attribute_filters_values, filters_dataset_filters_dataset_names=filters_dataset_filters_dataset_names, mode=mode, count_entries=count_entries)
        print("The response of FixpointApi->fixpoint_list_open_ai_chat_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_list_open_ai_chat_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The parent resource collection. In this case, \&quot;/openai_chats/{model_name}\&quot;. | 
 **page_size** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 
 **filters_relative_datetime_filters_from_s** | **str**| Number of seconds from current datetime | [optional] 
 **filters_userfeedback_filter_thumbs_reaction** | **str**|  | [optional] [default to &#39;THUMBS_UNSPECIFIED&#39;]
 **filters_attribute_filters_keys** | [**List[str]**](str.md)|  | [optional] 
 **filters_attribute_filters_values** | [**List[str]**](str.md)|  | [optional] 
 **filters_dataset_filters_dataset_names** | [**List[str]**](str.md)|  | [optional] 
 **mode** | **str**|  | [optional] [default to &#39;MODE_UNSPECIFIED&#39;]
 **count_entries** | **bool**| Whether to also return a count of all the entries matching the list query. | [optional] 

### Return type

[**V1ListOpenAIChatLogsResponse**](V1ListOpenAIChatLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_list_routing_configs**
> V1ListRoutingConfigsResponse fixpoint_list_routing_configs()

List LLM routing configs

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.v1_list_routing_configs_response import V1ListRoutingConfigsResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)

    try:
        # List LLM routing configs
        api_response = api_instance.fixpoint_list_routing_configs()
        print("The response of FixpointApi->fixpoint_list_routing_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_list_routing_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ListRoutingConfigsResponse**](V1ListRoutingConfigsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_post_dataset_logs**
> V1PostDatasetLogsResponse fixpoint_post_dataset_logs(name, body)

Add logs to a dataset

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.fixpoint_post_dataset_logs_request import FixpointPostDatasetLogsRequest
from fixpoint_openapi.models.v1_post_dataset_logs_response import V1PostDatasetLogsResponse
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    name = 'name_example' # str | 
    body = fixpoint_openapi.FixpointPostDatasetLogsRequest() # FixpointPostDatasetLogsRequest | 

    try:
        # Add logs to a dataset
        api_response = api_instance.fixpoint_post_dataset_logs(name, body)
        print("The response of FixpointApi->fixpoint_post_dataset_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_post_dataset_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**FixpointPostDatasetLogsRequest**](FixpointPostDatasetLogsRequest.md)|  | 

### Return type

[**V1PostDatasetLogsResponse**](V1PostDatasetLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fixpoint_update_spending_totals**
> V1RoutingConfig fixpoint_update_spending_totals(route_config_id, body)

Update routing config spending totals

Update spending totals on a routing config.

### Example


```python
import fixpoint_openapi
from fixpoint_openapi.models.fixpoint_update_spending_totals_request import FixpointUpdateSpendingTotalsRequest
from fixpoint_openapi.models.v1_routing_config import V1RoutingConfig
from fixpoint_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fixpoint_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fixpoint_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fixpoint_openapi.FixpointApi(api_client)
    route_config_id = 'route_config_id_example' # str | 
    body = fixpoint_openapi.FixpointUpdateSpendingTotalsRequest() # FixpointUpdateSpendingTotalsRequest | 

    try:
        # Update routing config spending totals
        api_response = api_instance.fixpoint_update_spending_totals(route_config_id, body)
        print("The response of FixpointApi->fixpoint_update_spending_totals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixpointApi->fixpoint_update_spending_totals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_config_id** | **str**|  | 
 **body** | [**FixpointUpdateSpendingTotalsRequest**](FixpointUpdateSpendingTotalsRequest.md)|  | 

### Return type

[**V1RoutingConfig**](V1RoutingConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

