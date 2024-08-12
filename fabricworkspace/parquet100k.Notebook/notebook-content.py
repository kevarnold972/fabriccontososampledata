# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "45fe99d8-0721-4519-98a3-483010bddcba",
# META       "default_lakehouse_name": "Contoso100K",
# META       "default_lakehouse_workspace_id": "731dc84c-bca4-4e25-90b8-4e3dd37b96b4"
# META     }
# META   }
# META }

# CELL ********************

pip install py7zr

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
import py7zr
zipDataUrl = "https://github.com/sql-bi/Contoso-Data-Generator-V2-Data/releases/download/ready-to-use-data/parquet-100k.7z"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

response = requests.get(zipDataUrl)
zipFilePath = "/lakehouse/default/Files/parquet-100k.7z"
with open(zipFilePath, 'wb') as file:
    file.write(response.content)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


with py7zr.SevenZipFile("/lakehouse/default/Files/delta-100k.7z", mode='r') as z:
    z.extractall(path='/lakehouse/default/Tables/dbo')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# df = spark.read.parquet("Files/currencyexchange.parquet")
# # df now is a Spark DataFrame containing parquet data from "Files/currencyexchange.parquet".
# display(df)
mssparkutils.fs.ls('Files')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
