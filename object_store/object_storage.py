class ObjectStorage:
    def __init__(self):
        self.client = None

    def create_client(self, *args, **kwargs):
        pass

    def retrieve_from_bucket(self, source_bucket, file_name):
        pass

    def store_to_bucket(self, destination_bucket, file_name, img_path):
        pass
