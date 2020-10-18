from google.cloud import bigquery
import GCP.gcp_credential_generator as cred
import pandas as pd
from google.cloud import bigquery_storage_v1beta1
import google.auth
import os
from google.auth import impersonated_credentials
from google.oauth2 import service_account
from google.cloud.exceptions import NotFound

#*******************
#   create big query client
#   assign credentioal to it
#*************************
os.environ[ 'GOOGLE_APPLICATION_CREDENTIALS' ] = "D:/Learning/GCP/key/admin.json"
cedential,project =  google.auth.default()
bqclient = bigquery.Client(
    credentials=cedential,
    project='datalake-287806',
)


#*****************
# create schema or data set in big query
#****************
bqclient.create_dataset("test_schema")

#******************
# create table in bigquery directly using sql
#******************

bqclient.query("create table datalake-287806.stg_tables.dept(dept_no  INT64 , deptname STRING)")

#other way in structure we can use genral data type but in above create we need to use
#  BQ internal data type

schema = [
    bigquery.SchemaField("emp_no", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("sal", "INTEGER", mode="REQUIRED"),
]
dataset_ref=bqclient.dataset('stg_tables')
table_ref=dataset_ref.table('sal')

table = bigquery.Table(table_ref, schema=schema)
table = bqclient.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)

#*********************
# insert data to table
#  batch processing using insert_row
# retrive data using sql
#*********************

record = [{'emp_id':1,'emp_name':'test1','dept_no':10}, \
               {'emp_id':2,'emp_name':'test2','dept_no':10}, \
                {'emp_id':3,'emp_name':'test3','dept_no':10}, \
                {'emp_id':4,'emp_name':'test4','dept_no':10}, \
                {'emp_id':5,'emp_name':'test5','dept_no':10}]
record_dept=[{'dept_no':10,'deptname':'hr'},
             {'dept_no': 20, 'deptname': 'finance'},
             {'dept_no': 30, 'deptname': 'operation'},]

dataset_ref=bqclient.dataset('stg_tables')
table_ref=dataset_ref.table('emp')
table=bqclient.get_table(table_ref)

bqclient.insert_rows(table,record)
#bqclient.insert_rows_from_dataframe()
#bqclient.insert_rows_json()

table_ref=dataset_ref.table('dept')
table=bqclient.get_table(table_ref)

#check if table exists ot not
try:
    bqclient.get_table(table_ref)
    bqclient.insert_rows(table,record_dept)
except NotFound:
    print("table not exists")


#create table if not exists .if table not exists in exception block table will be created.
table_ref = dataset_ref.table("location")
try:
    bqclient.get_table(table_ref)
except NotFound:
    print("creating table ----")
    bqclient.query("create table stg_tables.location(empno INT64, location STRING)")

for i in bqclient.query("select * from stg_tables.emp"):
    print(i)

# bigquery return the sql results in as row ( that is values )  with schema as dictionary field
# Row(('hr', 'test5'), {'deptname': 0, 'emp_name': 1})
bqclient.query("select deptname ,emp_name from stg_tables.emp e join stg_tables.dept d on (e.dept_no=d.dept_no)")


bqclient.query("delete from stg_tables.emp where emp_id='1'")

#******************
# load to table in bigquery using job config .
#******************
data_frame= pd.DataFrame.from_dict(record)
job_config = bigquery.LoadJobConfig()
job_config.write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
job_config.autodetect=True
#job_config.source_format=bigquery.SourceFormat.ORC
#job_config.source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
#job=bqclient.load_table_from_json(record,table_ref,job_config=job_config)
job=bqclient.load_table_from_dataframe(data_frame,table_ref,job_config=job_config)


#*********************
# read tables inside the data set
#*********************
for i in bqclient.list_datasets():
    print(i.dataset_id)
    if (i.dataset_id=='stg_tables'):
        dataset_ref=bqclient.dataset(i.dataset_id)
        print(bqclient.get_table(dataset_ref.table('emp')))
        table_ref=bqclient.get_table(dataset_ref.table('emp'))
        print(table_ref.table_id)
        print(table_ref.num_rows)


