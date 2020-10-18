
from com.pkg.s3 import s3conn


class s3operation(s3conn):
    def createbucket(self):
        obj1 = s3conn().conn
        obj1.create_bucket('ipythoninheritancesecurebucket')



s3 = s3operation()
s3.createbucket()
