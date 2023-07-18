import sqlite3
import pandas as pd

# read the csv file to pandas dataframe
df = pd.read_csv("restaurants_small.csv")

# remove extra spaces present (if any)
df.columns = df.columns.str.strip()

# create/connect a/to a sqlite db 
connection = sqlite3.connect('demo.db')

# load data to db
df.to_sql('<table name>',connection,if_exists='replace')

# close connection
connection.close()
