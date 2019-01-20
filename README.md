### wasabis3

Wrapper for boto3 library, created to be used with [Wasabi Hot Cloud Storage](https://wasabi.com).
Wasabi is S3 compatible, so it can be used with `boto3` by overriding AWS-related parameters.
Created client is usual `boto3` S3 clint, so can be used in usual manner.

#### Example:

```python
from wasabis3 import get_client

wasabi = get_client('<WASABI_SECRET_ACCESS_KEY_ID>', '<WASABI_SECRET_ACCESS_KEY>')

resp = wasabi.list_buckets()

buckets = [bucket['Name'] for bucket in resp['Buckets']]

print(buckets)

```