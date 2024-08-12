# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "485d705c-1c4f-45a2-b438-ba4f6a965215",
# META       "default_lakehouse_name": "NewTest",
# META       "default_lakehouse_workspace_id": "731dc84c-bca4-4e25-90b8-4e3dd37b96b4",
# META       "known_lakehouses": [
# META         {
# META           "id": "485d705c-1c4f-45a2-b438-ba4f6a965215"
# META         }
# META       ]
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
zipDataUrl = "https://github.com/sql-bi/Contoso-Data-Generator-V2-Data/releases/download/ready-to-use-data/delta-100k.7z"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

response = requests.get(zipDataUrl)
zipFilePath = "/lakehouse/default/Files/delta-100k.7z"
with open(zipFilePath, 'wb') as file:
    file.write(response.content)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


with py7zr.SevenZipFile("/lakehouse/default/Files/delta-100k.7z", mode='r') as z:
    z.extractall(path='/lakehouse/default/Tables')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
