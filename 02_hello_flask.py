from flask import Flask
"""
透過url傳值
"""

# 固定格式
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

# 參數透過路由傳遞，default : str
@app.route('/user/<username>')
def username(username):
    return "I am " + username

# flask支援四種參數形式 : int, str, float, path
# <型態：參數>
@app.route('/age/<int:age>')
def userage(age):
    return "I am " + str(age) + "years old."


if __name__ == "__main__":
    app.run(debug=True)