from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

# データベース接続用の補助関数
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # カラム名でデータを取り出せるようにする
    return conn

# スコアリングロジック（Service層の役割）
def calculate_score(course, user_faculty):
    score = 0
    # 学科一致ボーナス
    if course['faculty'] == user_faculty or course['faculty'] == '全学科':
        score += 10
    
    # 難易度が低い（1〜2）ほど「楽単」として加点
    score += (5 - course['difficulty']) * 2
    
    # ガチャのランダム要素
    score += random.uniform(0, 5)
    return score

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend_all', methods=['POST'])
def recommend():
    # フォームからのデータ取得
    user_faculty = request.form.get('faculty')
    locked_slots = request.form.getlist('locked_slots') # ['月-1', '火-3'] のような形式

    # 1. 必ず入れる「カフプラ」のデータ（特殊枠）
    kahu_pura = {
        'id': 999,
        'name': '★サークル：カフプラ',
        'day': '水',
        'period': 4,
        'faculty': '全学科',
        'difficulty':
