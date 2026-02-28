import random
from flask import Flask, render_template, request

app = Flask(__name__)

# 仮の授業データ（後で自由に追加してね！）
subjects = [
    {"name": "経済学基礎", "day": "月", "period": 1},
    {"name": "心理学入門", "day": "月", "period": 2},
    {"name": "プログラミングI", "day": "火", "period": 1},
    {"name": "統計学", "day": "水", "period": 3},
    {"name": "デザイン思考", "day": "木", "period": 4},
    {"name": "英語コミュニケーション", "day": "金", "period": 2},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend_all', methods=['POST'])
def recommend_all():
    locked_slots = request.form.getlist('locked_slots')
    days = ['月', '火', '水', '木', '金']
    timetable_data = [] 
    gacha_cards = []    

    for period in range(1, 6):
        row = []
        for day in days:
            slot_id = f"{day}-{period}"
            if slot_id in locked_slots:
                content = "必修ロック"
                is_locked = True
            else:
                possible = [s for s in subjects if s['day'] == day and s['period'] == period]
                content = random.choice(possible)['name'] if possible else "空きコマ"
                is_locked = False
                if content != "空きコマ":
                    gacha_cards.append({"day": day, "period": period, "name": content})
            
            row.append({"name": content, "locked": is_locked})
        timetable_data.append(row)

    return render_template('result.html', cards=gacha_cards, timetable=timetable_data)

import os

if __name__ == '__main__':
    # Renderが指定するポート番号を読み込む設定です
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)