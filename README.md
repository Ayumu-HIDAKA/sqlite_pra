# prepro_pra
sqliteの簡単なデモです。
scikit learnのtoyデータをsqliteにインサートします。

# setup
```
docker-compose up
```
コンテナにはいる(prepro_praにサフィックスがついていると思います)
```
docker exec -it コンテナ名 bash
```
ディレクトリの変更

```
cd work
```
前処理の実行
```
python3 insert_to_db.py
```
dbの読み取り
```
python3 read_db.py
```