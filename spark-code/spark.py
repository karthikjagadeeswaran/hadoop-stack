import re
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

simpleData = [("d1","Sales","NY",90000,34,1), \
    ("d1","Sales","NY",86000,56,2), \
    ("d1","Sales","CA",81000,-30,3), \
    ("d2","Finance","CA",90000,24,1), \
    ("d2","Finance","CA",99000,40,2), \
    ("d2","Finance","NY",83000,36,3), \
    ("d3","Finance","NY",79000,53,1), \
    ("d3","Marketing","CA",80000,25,2), \
    ("d3","Marketing","NY",91000,50,3) \
  ]
columns= ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data = simpleData, schema = columns)
df.show(truncate=False)