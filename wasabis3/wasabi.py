from boto3 import client

SERVICE_ENDPOINT = 'https://s3.wasabisys.com'


def get_client(access_key_id,
               secret_access_key,
               session_token=None):
    """
    Factory function that creates `Wasabi storage` client.

    :param access_key_id: access id for `Wasabi`
    :param secret_access_key: secret key for `Wasabi`
    :param session_token: session token for `Wasabi`
    :return: s3 client, attached to Wasabi service
    """
    storage = _WasabiStorage(access_key_id, secret_access_key, session_token).storage
    return storage


class _WasabiStorage:
    """
    Wraps S3 client from `boto3` library.
    Overrides AWS endpoint and uses Wasabi credentials to create compatible client.
    """

    def __init__(self,
                 access_key_id,
                 secret_access_key,
                 session_token=None):
        self.storage = client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            aws_session_token=session_token,
            endpoint_url=SERVICE_ENDPOINT
        )
