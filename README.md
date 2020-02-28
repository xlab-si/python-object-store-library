# Python object store library for different platforms

This is a python library for different object storages that have common methods.

It is currently meant to support the following object storage platforms:

- [MinIO](https://min.io/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Azure BLOB Container Storage](https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction)

The library allows and adheres basic functionalities of object store platforms that are listed below:

* connecting to particular object store
* storing objects to buckets
* retrieving object from buckets


## Table of Contents
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Cleanup](#cleanup)
  - [Usage](#usage)
    - [Creating a specific object storage client](#creating-a-specific-object-storage-client)
        - [MinIO](#minio)
        - [AWS S3](#aws-s3)
        - [Azure](#azure)
    - [Reading from bucket](#reading-from-bucket)
    - [Writing to bucket](#writing-to-bucket)

## Prerequisites

To properly build and use the library, you have to install python2 (with pip) or python3 (with pip3) and set up 
a virtual environment. You might need to run the following commands for python installation:

```bash
sudo apt update
sudo apt install -y python3-venv python3-wheel python-wheel-common
```

## Installation

The easiest way to install `object_store` library is to install it into virtual environment:

```bash
# clone this repository
git clone git@github.com:xlab-si/python-object-store-library.git

# setup virtual environment
python3 -m venv .venv && . .venv/bin/activate
pip install object_store

# python2
python setup.py bdist_wheel
pip install dist/object_store-0.0.1-py2-none-any.whl

# python3
python3 setup.py bdist_wheel
pip3 install dist/object_store-0.0.1-py3-none-any.whl

# this will be relevant when the package gets published to PyPi
pip install object_store
```

After this you can import the library in your python files using `import object_store`.

## Cleanup

The cleanup process is also important. To unistall this library run `pip uninstall object store` for python2 or/and `pip3 uninstall object store` for python3. You
should also remove files from your interpreter path (for example `rm -rf ~/.local/lib/python3.7/site-packages/object_store/` and also any wheel files like `rm -rf ~/.local/lib/python3.7/site-packages/object_store-0.1.0.dist-info/`).
Wheel files are also present in `dist` folder of the library. If you want to reinstall the library you should probabaly remove them.

## Usage

This library provides different functions that are available to be used along with different object stores.

Supported object storages are stored in python Enum type, named `ObjectStorageType`, where three constants representing three object
storages are specified: `AWS_S3`, `AZURE_CONTAINERS` and `MINIO`.

Currently you can use the following methods:

| Method | Purpose
|:-------------|:-------------|
| **create_client** | Creates a new objest store client |
| **retrieve_from_bucket** | Retrieves object from bucket |
| **store_to_bucket** | Stores object to bucket |

These methods are further explained in the next sections. 

### Creating a specific object storage client

To create an object storage client you have to use `create_client(self, *args, **kwargs)` method.

#### MinIO

If you are using MinIO object storage you have to somehow provide the IP of the storage and its access and
secret key. You can do this directly by putting keyworded arguments into `create client` method like
this: 

```python
from object_store.min_io import MinIO

minio = MinIO()
minio.create_client(ip='192.0.2.1',
                    access_key='AKIAIOSFODNN7EXAMPLE',
                    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')
```

To avoid direct contact with different object storages the is a class called `ObjectStorageCreator` that creates
object storage objects for us by using `create_storage` function. Be careful pass the proper `ObjectStorageType` to its constructor. So in case of MinIO we will use `ObjectStorageType.MINIO`. The full usage is shown in the example below (for MinIO credentials we use example IPs, access key and secret key):

```python
from object_store.object_storage_creator import ObjectStorageCreator
from object_store.object_storage_type import ObjectStorageType

object_storage_creator = ObjectStorageCreator(ObjectStorageType.MINIO)
minio_client = object_storage_creator.create_storage(ip='192.0.2.1',
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

For the Azure Container BLOB storage you have to set the type of storage to `ObjectStorageType.AZURE_CONTAINERS`. From there you can use `create_storage` function to create your client and pass your Azure connection string (you can find it in Azure Portal inder Azure Active Directory Settings).

```python
from object_store.object_storage_creator import ObjectStorageCreator
from object_store.object_storage_type import ObjectStorageType

object_storage_creator = ObjectStorageCreator(ObjectStorageType.AZURE_CONTAINERS)
azure_client = object_storage_creator.create_storage(connection_string="your-connection-string")
```

### Reading from bucket

To get something from your bucket in your object storage, you can freely use `retrieve_from_bucket(self, source_bucket, file_name)` method where you pass `source_bucket` variable as a name of your bucket and `file_name` which is the name of your element in the bucket that you want to retrieve (the file/element will be also stored in `/tmp` folder under the same name). See
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
minio_client = object_storage_creator.create_storage(ip='192.0.2.1',
                     access_key='AKIAIOSFODNN7EXAMPLE',
                     secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')
minio_client.store_to_bucket("my_destination_bucket", "my_new_picture", "/home/pc/image.png")
```
