import boto3


class WasabiStorage:
    """
    Wraps S3 client from `boto3` library.
    Overrides AWS endpoint and uses Wasabi credentials to create compatible client.
    """

    def __init__(self,
                 access_key_id,
                 secret_access_key,
                 region,
                 session_token=None):
        self.client = boto3.client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            aws_session_token=session_token,
            endpoint_url='https://s3.{}.wasabisys.com'.format(region)
        )

    def upload(self, file_path, bucket_name, wasabi_file_name):
        """ Upload file to specific bucket

        :type file_path: str
        :param file_path: The path of file.

        :type bucket_name: str
        :param bucket_name: The name of bucket that you want to upload the file on it.

        :type wasabi_file_name: str
        :param wasabi_file_name: File name on Wasabi Cloud
        """
        self.client.upload_file(file_path, bucket_name, wasabi_file_name)
