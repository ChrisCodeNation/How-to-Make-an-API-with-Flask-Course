from flask import Flask
from flask import render_template

"""
render_template搭配參數傳遞
"""

# 固定格式
app = Flask(__name__)

# 參數傳遞
@app.route('/user/<username>')
def user(username):
    return render_template('abc2.html',  user_template = username)

if __name__ == "__main__":
    app.run(debug=True)