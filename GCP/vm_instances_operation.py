#export GOOGLE_APPLICATION_CREDENTIALS="D:\Learning\GCP\key\admin.json"
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
import google.auth
import os
import googleapiclient
from googleapiclient.discovery import build
    #Client for discovery based APIs.
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#this is to set enviromnetal variable to get default credential from service account
#it use auth2 to get a credential from the service account.
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="D:/Learning/GCP/key/admin.json"

credential, project = google.auth.default()
#scope is optional if we want to specify scope of credential for a specific api


#client discovery build will discover right api for the resource.
#here credential is optional , if we are not using default credential then we can pass other credential by credentials  argument
compute = googleapiclient.discovery.build('compute', 'v1',credentials=credential)
image_response = compute.images().getFromFamily(
        project='debian-cloud', family='debian-9').execute()
source_disk_image = image_response['selfLink']
zone='us-central1-c'
machine_type = "zones/%s/machineTypes/e2-micro" % 'us-central1-c'

config = {
        'name': "instance-2",
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],
        "networkInterfaces": [
            {
              "subnetwork": "projects/datalake-287806/regions/us-central1/subnetworks/subnet1"
             }
       ]
}

"""
to get subnet url go to subnet in vpc and see equivalent   rest api 
"""


#create compute instance

#note: all the bellow functions will create http heade and release a post command and it is a state less event.
compute.instances().insert(
        project=project,
        zone='us-central1-c',
        body=config).execute()

result = compute.instances().list(project=project, zone=zone).execute()

instance_name = result['items'][0]['name']

#delete compute instance
compute.instances().delete(
        project=project,
        zone=zone,
        instance=instance_name).execute()