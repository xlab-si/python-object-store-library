import boto3

from object_store.object_storage import ObjectStorage


class AwsS3(ObjectStorage):
    def __init__(self):
        super().__init__()

    def create_client(self):
        self.client = boto3.client('s3')

    def retrieve_from_bucket(self, source_bucket, file_name):
        try:
            self.client.download_file(source_bucket, file_name, "/tmp/" + file_name)
        except Exception as e:
            raise Exception("There was an error retrieving object from the bucket: " + str(e))

    def store_to_bucket(self, destination_bucket, file_name, img_path):
        try:
            self.client.upload_file(img_path, destination_bucket, file_name)
        except Exception as e:
            raise Exception("There was an error storing object to the bucket: " + str(e))
