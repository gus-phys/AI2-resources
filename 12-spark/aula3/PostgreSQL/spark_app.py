from random import SystemRandom
import sys, getopt
from pyspark.sql import SparkSession

if __name__ == "__main__":
        spark = SparkSession \
            .builder \
            .appName("Solution by Luiszera") \
            .config("spark.jars", "/usr/local/postgresql-42.3.3.jar") \
            .getOrCreate()

    opts, args = getopt.getopt(sys.argv[1:], "p:t")

    filepath, tablename = "", ""

    for opt, arg in opts:
        if opt == "-p":
            print('ok1')
            filepath = arg
        elif opt == "-t":
            print('ok2')
            tablename = arg

    df = spark.read_load(filepath, inferSchema=True)