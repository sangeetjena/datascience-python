from abc import ABC ,abstractclassmethod
from boto.s3.connection import S3Connection

class s3conn(ABC):
    conn = None
    def __init__(self):
        self.conn = S3Connection('AKIAJZOKVIUV3CDR2VCA', 'T5CbRCQbv6pV3eSUZ2My9cz7lRkCA1Rq0LvQ5nbS')
        #conn.create_bucket(bucketname)

