from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/recommend', methods=['POST'])
def recommend():
    day, period = request.form.get('day'), request.form.get('period')
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    res = conn.execute("SELECT * FROM classes WHERE day=? AND period=?", (day, period)).fetchone()
    conn.close()
    if not res: return "なし <a href='/'>戻る</a>"
    return f"<h2>結果：{res['name']}</h2><a href='/'>戻る</a>"
if __name__ == '__main__':
    app.run(debug=True, port=5001)
