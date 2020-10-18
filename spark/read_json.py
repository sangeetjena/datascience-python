import pyspark.sql import SparkSession

spark = SparkSession.build.appName("test").enableHiveSupport().conf("","").getOrCreate()

# multiline option needed when reading miltiline json file
x= spark.read.option("multiline","true").json("file:///u/users/svccexp/temp/sangeet/sample/food.json")
print(x.rdd.getNumPartitions())