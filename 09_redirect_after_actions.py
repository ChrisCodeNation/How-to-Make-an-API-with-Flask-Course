from flask import Flask, request, render_template, redirect, url_for

"""
登入後，透過redirect做到畫面跳轉
redirect搭配url_for，並傳遞參數

1. 登入頁面，輸入username
2. 跳轉畫面到hello page
"""

# 固定格式
app = Flask(__name__)

@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 使用redirect(url_for('function')) 重新導向到要跳轉的function及url
        return redirect(url_for('hello', username=request.form.get('username')))

    return render_template('09_login.html')

# 接收login()內的redirect(url_for('function'))傳遞的參數
@app.route('/hello/<username>')
def hello(username):
    return render_template('09_hello.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)