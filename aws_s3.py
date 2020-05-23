from boto.s3.connection import S3Connection

## create connection to the service
conn = S3Connection('AKIAJZOKVIUV3CDR2VCA', 'T5CbRCQbv6pV3eSUZ2My9cz7lRkCA1Rq0LvQ5nbS')


## creating a bucket
bucket = conn.create_bucket('go4expert_python')
