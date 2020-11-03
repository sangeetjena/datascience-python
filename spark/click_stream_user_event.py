import pyspark.sql.functions as fn
import datetime
from pyspark.sql.types import StructField, StringType, IntegerType, TimestampType, DateType, StructType

spark = SparkSession.builder.appName("session_read").enableHiveSupport().getOrCreate()


# this function will return record containing
#
#  time_stamp, user_id,session_id, sctivity_date
#

def enhance_session_id(x):
    prev = None
    session_lst = [ ]
    enhanced_record = [ ]
    cnt = 0
    for i in x:
        if prev == None:
            prev = i[ 0 ]
            session_lst.append(i[ 0 ])
            enhanced_record.append([ i[ 0 ], str(i[ 1 ]), i[ 2 ], "s" + str(cnt) ])
            continue
        elif ((i[ 0 ] - session_lst[ -1 ]).total_seconds() / 60) > 120:
            print((i[ 0 ] - session_lst[ -1 ]).total_seconds() / 60)
            cnt = cnt + 1
            enhanced_record.append([ i[ 0 ], str(i[ 1 ]), i[ 2 ], "s" + str(cnt) ])
            session_lst.append(i[ 0 ])
            prev = i[ 0 ]
            continue
        elif ((i[ 0 ] - prev).total_seconds() / 60) > 30:
            print((session_lst[ -1 ] - prev).total_seconds() / 60)
            cnt = cnt + 1
            enhanced_record.append([ i[ 0 ], str(i[ 1 ]), i[ 2 ], "s" + str(cnt) ])
            session_lst.append(i[ 0 ])
            prev = i[ 0 ]
            continue
        else:
            enhanced_record.append([ i[ 0 ], str(i[ 1 ]), i[ 2 ], "s" + str(cnt) ])
            prev = i[ 0 ]
    print(enhanced_record)
    return enhanced_record


session_df = spark.read.option("header", "true").format("csv").load(
    "file:///u/users/svccexp/temp/sangeet/sample/session.csv")

# partitioning data based on userid , because i want to process partition by user data
# so that i will be able to call get seesion function for entire one user data and able to apply session allocation logic
users = session_df.select(col("userid")).distinct().count()
session_rdd = session_df.select(fn.to_timestamp(col("timestamp")).alias("timestamp"),
                                fn.date_format(fn.to_timestamp(col("timestamp")), "YYYY-MM-DD").alias("dt"),
                                fn.col("userid")) \
    .orderBy(fn.col("userid").asc(), fn.col("timestamp").asc()).repartition(users, col("userid")).rdd

# called foreach partition to process partition data and it will return a rdd with session column added .

get_session = session_rdd.foreachPartition(enhance_session_id)

get_session1 = session_rdd.mapPartitions(lambda x: enhance_session_id(x))

schema = StructType([ StructField('timestamp', StringType(), True),
                      StructField('dt', DateType(), True),
                      StructField('userid', StringType(), True),
                      StructField('session', StringType(), True) ])
new_session_df = spark.createDataFrame(get_session1, [ "timestamp", "dt", "userid", "session" ])

new_session_df.show(100)

"""
create table user_session (timestamp timestamp,
                            dt date,
                            userid varchar(20),
                            session varchar(20),

                            )
partitioned by (activity_date date)
clustered by (userid) sorted by timestamp  into 32 buckets
stored as ORC
location 'user/hive/warehouse/stg_schema/user_session'
"""

new_session_df.registerTempTable("session")

spark.sql("select userid,count(distinct session) from session group by userid,dt").show(100)

spark.sql(
    "select userid,unix_timestamp(max(timestamp ))-unix_timestamp( min(timestamp)) as total_time_day  from session group by userid,dt").show(
    100)

spark.sql("select userid,count(distinct session) from session group by userid,month(cast(dt as date))").show(100)

new_session_df.write.partitionBy("activity_date").mode("overwrite").insertInto("stg_schema.user_session")
