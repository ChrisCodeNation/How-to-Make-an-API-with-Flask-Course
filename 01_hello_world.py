from flask import Flask
"""
建立一個app
"""

# 固定格式，記起來
app = Flask(__name__)

# 使用decorator定義路由
# 後面接的是一個function，當連接到'/'時，路由就知道要執行後面的function
@app.route('/')
def hello():
    return "hello world"


if __name__ == "__main__":
    # 固定格式
    app.run(debug=True)
