from azure.storage.blob import BlockBlobService

from object_store.object_storage import ObjectStorage


class Azure(ObjectStorage):
    def __init__(self):
        super().__init__()

    def create_client(self, azure_connection_string):
        self.client = BlockBlobService(connection_string=azure_connection_string)

    def retrieve_from_bucket(self, source_bucket, file_name):
        try:
            self.client.get_blob_to_path(source_bucket, file_name, "/tmp/" + file_name)
        except Exception as e:
            raise Exception("There was an error retrieving object from the bucket: " + str(e))

    def store_to_bucket(self, destination_bucket, file_name, img_path):
        try:
            self.client.create_blob_from_path(destination_bucket, file_name, img_path)
        except Exception as e:
            raise Exception("There was an error storing object to the bucket: " + str(e))
