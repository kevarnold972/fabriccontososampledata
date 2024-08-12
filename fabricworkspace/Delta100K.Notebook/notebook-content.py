# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "8d7cd553-801e-48c3-9b36-fe77a9f5fb0b",
# META       "default_lakehouse_name": "ContosoData",
# META       "default_lakehouse_workspace_id": "731dc84c-bca4-4e25-90b8-4e3dd37b96b4",
# META       "known_lakehouses": [
# META         {
# META           "id": "8d7cd553-801e-48c3-9b36-fe77a9f5fb0b"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Overview
# This notebook can be used to setup a Contoso sample data lakehouse from the ready to use data available on https://github.com/sql-bi/Contoso-Data-Generator-V2-Data/releases/tag/ready-to-use-data. This is setup for the 100K rows of data, but the pattern can be used for the others. 
# 
# Note: When you create or attach a lakehouse to this notebook, be sure not to use the preview feature for schemas. 

# MARKDOWN ********************

# # Install
# This will install the 7zip package so it can be used. 

# CELL ********************

pip install py7zr

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Setup
# import the required packages and set the URL

# CELL ********************

import requests
import py7zr
zipDataUrl = "https://github.com/sql-bi/Contoso-Data-Generator-V2-Data/releases/download/ready-to-use-data/delta-100k.7z"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Get the file
# This cell will perform a GET request to obtain the file and then save it to the Files section of the lakehouse. 

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

# MARKDOWN ********************

# # Unzip
# This cell will unzip the files and save them to the Tables area of the lakehouse. 

# CELL ********************


with py7zr.SevenZipFile("/lakehouse/default/Files/delta-100k.7z", mode='r') as z:
    z.extractall(path='/lakehouse/default/Tables')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
