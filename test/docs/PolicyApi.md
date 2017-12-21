# opsgenie_swagger.PolicyApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_alert_policy_order**](PolicyApi.md#change_alert_policy_order) | **POST** /v1/policies/{policyId}/change-order | Change Alert Policy Order
[**create_alert_policy**](PolicyApi.md#create_alert_policy) | **POST** /v1/policies | Create Alert Policy
[**delete_alert_policy**](PolicyApi.md#delete_alert_policy) | **DELETE** /v1/policies/{policyId} | Delete Alert Policy
[**disable_alert_policy**](PolicyApi.md#disable_alert_policy) | **POST** /v1/policies/{policyId}/disable | Disable Alert Policy
[**enable_alert_policy**](PolicyApi.md#enable_alert_policy) | **POST** /v1/policies/{policyId}/enable | Enable Alert Policy
[**get_alert_policy**](PolicyApi.md#get_alert_policy) | **GET** /v1/policies/{policyId} | Get Alert Policy
[**list_alert_policies**](PolicyApi.md#list_alert_policies) | **GET** /v1/policies | List Alert Policies
[**update_alert_policy**](PolicyApi.md#update_alert_policy) | **PUT** /v1/policies/{policyId} | Update Alert Policy


# **change_alert_policy_order**
> SuccessResponse change_alert_policy_order(policy_id, body)

Change Alert Policy Order

Change execution order of the alert policy with given id

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
body = opsgenie_swagger.ChangeAlertPolicyOrderPayload() # ChangeAlertPolicyOrderPayload | Change order payload

try:
    # Change Alert Policy Order
    api_response = api_instance.change_alert_policy_order(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->change_alert_policy_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **body** | [**ChangeAlertPolicyOrderPayload**](ChangeAlertPolicyOrderPayload.md)| Change order payload | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert_policy**
> CreateAlertPolicyResponse create_alert_policy(body)

Create Alert Policy

Creates a new alert policy

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
body = opsgenie_swagger.AlertPolicy() # AlertPolicy | Payload of created alert policy

try:
    # Create Alert Policy
    api_response = api_instance.create_alert_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertPolicy**](AlertPolicy.md)| Payload of created alert policy | 

### Return type

[**CreateAlertPolicyResponse**](CreateAlertPolicyResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_policy**
> SuccessResponse delete_alert_policy(policy_id)

Delete Alert Policy

Delete alert policy with given id

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Delete Alert Policy
    api_response = api_instance.delete_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_alert_policy**
> SuccessResponse disable_alert_policy(policy_id)

Disable Alert Policy

Disable the alert policy with given id

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Disable Alert Policy
    api_response = api_instance.disable_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->disable_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_alert_policy**
> SuccessResponse enable_alert_policy(policy_id)

Enable Alert Policy

Enable the alert policy with given id

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Enable Alert Policy
    api_response = api_instance.enable_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->enable_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_policy**
> GetAlertPolicyResponse get_alert_policy(policy_id)

Get Alert Policy

Used to get details of a single policy with id

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy

try:
    # Get Alert Policy
    api_response = api_instance.get_alert_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 

### Return type

[**GetAlertPolicyResponse**](GetAlertPolicyResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_policies**
> ListAlertPoliciesResponse list_alert_policies()

List Alert Policies

Returns list alert policies

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))

try:
    # List Alert Policies
    api_response = api_instance.list_alert_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->list_alert_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAlertPoliciesResponse**](ListAlertPoliciesResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_policy**
> SuccessResponse update_alert_policy(policy_id, body)

Update Alert Policy

Update alert policy with given id

### Example
```python
from __future__ import print_function
import time
import opsgenie_swagger
from opsgenie_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: GenieKey
configuration = opsgenie_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = opsgenie_swagger.PolicyApi(opsgenie_swagger.ApiClient(configuration))
policy_id = 'policy_id_example' # str | Id of the requested policy
body = opsgenie_swagger.AlertPolicy() # AlertPolicy | Payload of updated alert policy

try:
    # Update Alert Policy
    api_response = api_instance.update_alert_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_alert_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Id of the requested policy | 
 **body** | [**AlertPolicy**](AlertPolicy.md)| Payload of updated alert policy | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

