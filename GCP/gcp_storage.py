import GCP.gcp_credential_generator as cred
from google.cloud import storage

def get_bucket_list():
    credential=cred.get_credential("default")
    storage_client = storage.Client(credentials=credential)
    storage_client.create_bucket("datalake-23331")
    storage_client.list_buckets()
    storage_client.get_bucket('datalake-23331')\
            .blob('travell/train_ticket1').\
            upload_from_filename('C:/Users/sangeet/Documents/baba_train_ticket.pdf')
    storage_client.list_blobs('datalake-23331')
    storage_client.get_bucket('datalake-23331').delete_blob('travell/train_ticket')