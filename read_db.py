import sqlite3
import pandas as pd

table_name = 'iris'
conn = sqlite3.connect('db.sqlite')

print("DBからデータを読み込みます・・・")

df = pd.read_sql("select * from iris", conn)
print(df)