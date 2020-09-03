import google.auth
import os
from google.auth import impersonated_credentials
from google.oauth2 import service_account

def get_credential(auth_type,target):
    os.environ[ 'GOOGLE_APPLICATION_CREDENTIALS' ] = "D:/Learning/GCP/key/admin.json"
    #credential = source_credentials = service_account.Credentials.from_service_account_file(
    #'/path/to/svc_account.json')
    if (auth_type=='default'):
        cedential,project =  google.auth.default()
        return [cedential,project]

    if( auth_type=='servicefile'):
        credential = source_credentials = service_account.Credentials.from_service_account_file( 'D:/Learning/GCP/key/admin.json')

    if (auth_type=='impersonate'):
        source_credentials, project = google.auth.default()
        target_credentials = impersonated_credentials.Credentials(
            source_credentials=source_credentials,
            target_principal='developer@datalake-287806.iam.gserviceaccount.com',
            target_scopes='https://www.googleapis.com/auth/compute',
            lifetime=500)
        return target_credentials
    

