# Python object store library for different platforms

This is a python library for different object storages that have common methods.

It is meant to support the following object storage platforms:

- [MinIO](https://min.io/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Azure BLOB Container Storage](https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction)

The library allows basic functionalities of object store platforms that are listed below:

- connecting to particular object store
- storing objects to buckets
- retrieving object from buckets

## Table of Contents
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Creating a specific object storage client](#creating-a-specific-object-storage-client)
  - [MinIO](#minio)
  - [AWS S3](#aws-s3)
  - [Azure](#azure)
  - [Reading from bucket](#reading-from-bucket)
  - [Writing to bucket](#writing-to-bucket)

## Prerequisites

To properly build and use library, you have to install Python2 (with pip) and/or Python3 (with pip3). 

## Installation

To install and to be able to use this library do the following:

- clone this repository
- for python2 run `python setup.py bdist_wheel` to build a python wheel file and install it using `pip install dist/object_store-0.0.1-py2-none-any.whl`
- for python3 run `python3 setup.py bdist_wheel` to build a python wheel file and install it using `pip3 install dist/object_store-0.0.1-py3-none-any.whl`

After this you can import the library in your python files usinf `import object_store`.

## Cleanup

The cleanup process is also important. To unistall this library run `pip uninstall object store` for python2 or/and `pip3 uninstall object store` for python3. You
should also remove files from your interpreter path (for example `rm -rf ~/.local/lib/python3.7/site-packages/object_store/` and also any wheel files like `rm -rf ~/.local/lib/python3.7/site-packages/object_store-0.1.0.dist-info/`).
Wheel files are also present in `dist` folder of the library. If you want to reinstall the library you should probabaly remove them.

## Usage

This library provides different functions that are available to be used along with different object stores.

Supported object storages are stored in python Enum type, named `ObjectStorageType`, where two constants representing two object
storages are specified: `AWS_S3` and `MINIO`.

Currently you can use the following methods:

### Creating a specific object storage client

To create an object storage client you have to use `create_client(self, *args, **kwargs)` method.

#### MinIO

If you are using MinIO object storage you have to somehow provide the IP of the storage and its access and
secret key. You can do this directly by putting keyworded arguments into `create client` method like
this: 

```python
from object_store.min_io import MinIO

minio = MinIO()
minio.create_client(ip='10.10.43.217',
                    access_key='AKIAIOSFODNN7EXAMPLE',
                    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')
```

To avoid direct contact with different object storages the is a class called `ObjectStorageCreator` that creates
object storage objects for us by using `create_storage` function. Be careful pass the proper `ObjectStorageType` to its constructor.
So in case of MinIO we will `ObjectStorageType.MINIO`. The full usage is shown in the example below:

```python
from object_store.object_storage_creator import ObjectStorageCreator
from object_store.object_storage_type import ObjectStorageType

object_storage_creator = ObjectStorageCreator(ObjectStorageType.MINIO)
minio_client = object_storage_creator.create_storage(ip='10.10.43.217',
                     access_key='AKIAIOSFODNN7EXAMPLE',
                     secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')
```

#### AWS S3

For the AWS S3 bucket storage you have to set the type of storage to `ObjectStorageType.AWS_S3`. From there you can just
use `create_storage` function to create your client because this will automatically take you AWS credentials that
were set up on your system.

```python
from object_store.object_storage_creator import ObjectStorageCreator
from object_store.object_storage_type import ObjectStorageType

object_storage_creator = ObjectStorageCreator(ObjectStorageType.AWS_S3)
aws_s3_client = object_storage_creator.create_storage()
```

#### Azure

For the AWS S3 bucket storage you have to set the type of storage to `ObjectStorageType.AWS_S3`. From there you can just
use `create_storage` function to create your client because this will automatically take you AWS credentials that
were set up on your system.

```python
from object_store.object_storage_creator import ObjectStorageCreator
from object_store.object_storage_type import ObjectStorageType

object_storage_creator = ObjectStorageCreator(ObjectStorageType.AZURE_CONTAINERS)
azure_client = object_storage_creator.create_storage(connection_string="your-connection-string")
```

### Reading from bucket

To get something from your bucket in your object storage, you can freely use `retrieve_from_bucket(self, source_bucket, file_name)`
method where you pass `source_bucket` variable as a name of your bucket and `file_name` which is the name of your element
in the bucket that you want to retrieve (the file/element will be also stored in `/tmp` folder under the same name). See
the example below:

```python
from object_store.object_storage_creator import ObjectStorageCreator
from object_store.object_storage_type import ObjectStorageType

object_storage_creator = ObjectStorageCreator(ObjectStorageType.AWS_S3)
aws_s3_client = object_storage_creator.create_storage()
aws_s3_client.retrieve_from_bucket("my_bucket", "my_picture")
```

### Writing to bucket

To store something into an existing bucket use `store_to_bucket(self, destination_bucket, file_name, img_path)` method, where
you pass `destination_bucket` argument as the name of the bucket where you want to store your object. The name of the
element in the bucket must be specified with `file_name` argument, whereas `img_path` argument is used fot
the absolute/relative path to the element. See the example below:

```python
from object_store.object_storage_creator import ObjectStorageCreator
from object_store.object_storage_type import ObjectStorageType

object_storage_creator = ObjectStorageCreator(ObjectStorageType.MINIO)
minio_client = object_storage_creator.create_storage(ip='10.10.43.217',
                     access_key='AKIAIOSFODNN7EXAMPLE',
                     secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')
minio_client.store_to_bucket("my_destination_bucket", "my_new_picture", "/home/pc/image.png")
```
