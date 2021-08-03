### wasabis3

Wrapper for boto3 library, created to be used with [Wasabi Hot Cloud Storage](https://wasabi.com).
Wasabi is S3 compatible, so it can be used with `boto3` by overriding AWS-related parameters.
Created client is usual `boto3` S3 clint, so can be used in usual manner.

#### Examples:

```python
from wasabis3 import WasabiStorage

wasabi = WasabiStorage('<WASABI_SECRET_ACCESS_KEY_ID>', '<WASABI_SECRET_ACCESS_KEY>', '<WASABI_BUCKET_REGION>')

resp = wasabi.client.list_buckets()

buckets = [bucket['Name'] for bucket in resp['Buckets']]

print(buckets)

```

```python
from wasabis3 import WasabiStorage

wasabi = WasabiStorage('<WASABI_SECRET_ACCESS_KEY_ID>', '<WASABI_SECRET_ACCESS_KEY>', '<WASABI_BUCKET_REGION>')

wasabi.upload('<FILE_PATH>', '<WASABI_BUCKET_NAME>', '<FILE_NAME_ON_THE_CLOUD>')
```