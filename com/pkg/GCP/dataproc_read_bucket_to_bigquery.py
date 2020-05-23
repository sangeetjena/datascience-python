from pyspark.sql import SparkSession,SQLContext

spark = SparkSession.builder.appName('gcs-big-query').getOrCreate()
df = spark.read.format('csv').load('gs://landing_stage_standard/landing/titanic.csv')
df.write.mode('overwrite').csv('gs://landing_stage_standard/landing/output/titanic_output/')