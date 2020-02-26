from enum import Enum


class ObjectStorageType(Enum):
    AWS_S3 = "aws_s3"
    MINIO = "minio"
    AZURE_CONTAINERS = "azure_containers"
