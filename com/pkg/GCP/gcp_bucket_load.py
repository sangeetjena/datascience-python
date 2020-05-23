#https://medium.com/@erdoganyesil/read-file-from-google-cloud-storage-with-python-cf1b913bd134

from google.cloud import storage
from google.cloud import bigquery
import pandas as pd
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField
from io import StringIO

# Explicitly use service account credentials by specifying the private key file.
storage_client = storage.Client.from_service_account_json('C:/Users/sangeet/PycharmProjects/datascience-python/com/pkg/GCP/gcp_auth.json')
bigquery_client = bigquery.Client.from_service_account_json('C:/Users/sangeet/PycharmProjects/datascience-python/com/pkg/GCP/gcp_auth.json')

# Make an authenticated API request
buckets = list(storage_client.list_buckets())
bucket = storage_client.get_bucket('landing_stage_standard')
blob = bucket.get_blob('landing/titanic.csv')
data = blob.download_as_string()
df = pd.read_csv(StringIO(data))
#data1 = (x.split(',') for x in data.decode("utf-8").split('\n'))
#df = pd.DataFrame(data1[1:],columns=data1[0])


dataset_ref = bigquery_client.dataset('my_dataset','datalake-270918')
table_id = "titanic"
schema = [
    bigquery.SchemaField("PassengerId", "STRING"),
    bigquery.SchemaField("Survived", "STRING"),
bigquery.SchemaField("Pclass", "STRING"),
bigquery.SchemaField("Name", "STRING"),
bigquery.SchemaField("Sex", "STRING"),
bigquery.SchemaField("Age", "STRING"),
bigquery.SchemaField("SibSp", "STRING"),
bigquery.SchemaField("Parch", "STRING"),
bigquery.SchemaField("Ticket", "STRING"),
bigquery.SchemaField("Fare", "STRING"),
bigquery.SchemaField("Cabin", "STRING"),
bigquery.SchemaField("Embarked", "STRING"),
]
table_ref=dataset_ref.table(table_id)
table = bigquery.Table(table_ref, schema=schema)
table = bigquery_client.create_table(table)

## Loading data
load_config = LoadJobConfig()
load_config.skip_leading_rows = 1
load_config.schema = schema
uri = 'gs://landing_stage_standard/landing/titanic.csv'
load_job = bigquery_client.load_table_from_uri(
    uri,
    table_ref,
    job_config=load_config)

load_job.result()

destination_table = bigquery_client.get_table(table_ref)
print('Loaded {} rows.'.format(destination_table.num_rows))
