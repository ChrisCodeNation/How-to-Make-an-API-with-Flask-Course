from flask import Flask
from flask import url_for
from flask import redirect

"""
url_for與route的關聯
問題：如果把路由寫死，一但路由變更，就必須對所有路由做修正
flask可以透過url_for避免這個問題
"""

# 固定格式
app = Flask(__name__)

@app.route('/a')
def url_for_a():
    return "here is a"

@app.route('/b')
def b():
    # 'url_for_a'作為url_for的參數
    # 但這樣得到的結果會是'/a'（回傳值為路由，並不是function內容）
    # 透過url_for可以反過來找被裝飾的function的對應路由
    return url_for('url_for_a')

@app.route('/bb')
def bb():
    # 因此必須透過redirect搭配url_for
    # 才能將使用者指引到另一個路由
    return redirect(url_for('url_for_a'))

if __name__ == "__main__":
    app.run(debug=True)