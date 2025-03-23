from flask import render_template, request
from sqlalchemy import text
from . import app, engine

@app.route('/', methods=['GET', 'POST'])
def index():
    table_name = app.config['TABLE_NAME']
    filters = {}
    races = [] # racesを初期化

    if request.method == 'POST':  # フォームが送信された場合
        filters['日付'] = request.form.get('date')
        filters['レース場'] = request.form.get('racecourse')
        filters['レースNo'] = request.form.get('race_no')

        try: # try...exceptブロックをPOSTリクエストの中に移動
            with engine.connect() as connection:
                where_clause = "WHERE " + " AND ".join([f"{key} = '{value}'" for key, value in filters.items() if value]) if filters else ""
                query = f"""
                    SELECT 日付, レース場, レースNo, １着確率, 予測順位, 艇番, 選手登番, 選手名, 年齢, 支部, 体重, 級別, 全国勝率, 全国2連率, 当地勝率, 当地2連率, モーターNO, モーター2連率
                    FROM {table_name}
                    {where_clause}
                """
                db_races = connection.execute(text(query)).fetchall()
            races = [row._asdict() for row in db_races] # POSTリクエストが成功した場合のみracesに代入
        except Exception as e:
            return f"エラーが発生しました: {e}"

    return render_template('index.html', races=races, filters=filters) # racesを渡す