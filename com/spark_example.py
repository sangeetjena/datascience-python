from pyspark import SparkConf,SparkContext



sc = SparkContext("local","sparkdemo")

a=[1,2,3,4]
x=sc.parallelize(a)
x.foreachPartition(print)