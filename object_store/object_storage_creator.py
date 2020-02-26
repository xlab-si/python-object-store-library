from object_store.aws_s3 import AwsS3
from object_store.azure import Azure
from object_store.min_io import MinIO
from object_store.object_storage_type import ObjectStorageType


class ObjectStorageCreator:
    def __init__(self, object_storage_type):
        self.object_storage_type = object_storage_type

    def create_storage(self, *args, **kwargs):
        if self.object_storage_type is ObjectStorageType.MINIO:
            ip = kwargs.get('ip', None)
            access_key = kwargs.get('access_key', None)
            secret_key = kwargs.get('secret_key', None)
            minio = MinIO()
            minio.create_client(ip=ip, access_key=access_key, secret_key=secret_key)
            return minio
        elif self.object_storage_type is ObjectStorageType.AWS_S3:
            aws_s3 = AwsS3()
            aws_s3.create_client()
            return aws_s3
        else:
            conn_str = kwargs.get('connection_string', None)
            azure = Azure()
            azure.create_client(azure_connection_string=conn_str)
            return azure
