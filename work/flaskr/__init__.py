from flask import Flask
import sqlalchemy
from sqlalchemy import text  # SQLクエリを直接実行するために使用

app = Flask(__name__)

# データベース接続情報
user = "boatrace_user"  # MySQLユーザー名
password = "your_password"  # MySQLパスワード
host = "db"  # MySQLホスト名 (localhostなど)
database = "boatrace_db"  # データベース名
table_name = "race_results" # テーブル名 (例: race_results)

app.config['TABLE_NAME'] = table_name # TABLE_NAMEを設定
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

try:
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

    with engine.connect() as connection:
        try:
            connection.execute(text(f"SELECT 1 FROM {table_name} LIMIT 1"))
            print(f"テーブル '{table_name}' への接続を確認しました。")
        except sqlalchemy.exc.ProgrammingError as e:
            if "1146" in str(e):  # テーブルが存在しないエラーコード
                print(f"テーブル '{table_name}' が存在しないため、作成します。")
                metadata_obj = sqlalchemy.MetaData()
                sqlalchemy.Table(table_name, metadata_obj,
                                sqlalchemy.Column("レースID", sqlalchemy.Integer),
                                sqlalchemy.Column("1の確率", sqlalchemy.Float),
                                sqlalchemy.Column("艇番", sqlalchemy.Integer),
                                sqlalchemy.Column("順位", sqlalchemy.Float)
                                ).create(engine)
                print(f"テーブル '{table_name}' を作成しました。")
            else:
                print(f"__init__.py でエラーが発生しました: {e}")
                raise e
except Exception as e:
    print(f"データベースエンジン作成時にエラーが発生しました: {e}")



#import flaskr.main  # main.py をインポート
from . import main


if __name__ == "__main__":
    app.run(debug=True)