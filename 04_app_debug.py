from flask import Flask
"""
app.debug = True通常是在開發時做的設置
正式環境中絕對不會設置
"""

# 固定格式
app = Flask(__name__)

@app.route('/age')
def userage():
    age = 3
    return "I am " + age + "years old."

if __name__ == "__main__":
    # 在開發時，不寫app.debug = True會痕難判斷異常來源
    #app.debug = True
    app.run()