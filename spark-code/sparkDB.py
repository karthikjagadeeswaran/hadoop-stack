import re
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

df = spark.createDataFrame(data = [('2','Karthik')], schema = ['id','name'])

df.write.mode('append') \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://pgbouncer-pgbouncer:5432/registry_db") \
    .option("dbtable", "registry.test") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .save()

jdbcDF = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://pgbouncer-pgbouncer:5432/registry_db") \
    .option("dbtable", "registry.test") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .load()

jdbcDF.show()