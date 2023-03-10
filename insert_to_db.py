import pandas as pd
import sqlite3
from sklearn import datasets

df = datasets.load_iris(as_frame=True).frame # データの取得
df = df.rename(columns = {"sepal length (cm)":"sepal_length_cm", "sepal width (cm)":"sepal_width_cm", "petal length (cm)":"petal_length_cm", "petal width (cm)":"petal_width_cm"}) # dfの列名を変更
print(df)

table_name = 'iris'

conn = sqlite3.connect('db.sqlite') # DBをつくるための準備


query = f'Create table if not Exists {table_name} (sepal_length_cm float, sepal_width_cm float, petal_length_cm float, target float)' # テーブルの定義
conn.execute(query) # テーブルの作成

df.to_sql(table_name,conn,if_exists='replace',index=False) # テーブルにデータを挿入
conn.commit() # DBへの変更を記録

print("DBへのデータの追加が完了しまいした")