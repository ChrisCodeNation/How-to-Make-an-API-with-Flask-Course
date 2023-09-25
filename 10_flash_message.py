from flask import Flask, request, render_template, redirect, url_for, flash

"""
flash可將訊息由後端傳至前端

使用者成功登入後，透過flash丟出一個成功登入訊息，
並redirect到跳轉畫面

1. 登入頁面，輸入username
2. 利用flash丟出訊息
3. 跳轉畫面到hello page
"""
# 固定格式
app = Flask(__name__)

@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 檢查帳號密碼
        if check(request.form['username'], request.form['password']):
            # 丟出成功訊息
            flash('Login Success')
            # 跳轉畫面
            return redirect(url_for('hello', username=request.form.get('username')))

    return render_template('10_login.html')

# 檢查帳號密碼
def check(username, password):
    if username=='admin' and password=='hello':
        return True
    else:
        return False

@app.route('/hello/<username>')
def hello(username):
    return render_template('10_hello.html', username=username)


if __name__ == "__main__":
    app.secret_key = "Your Key"
    app.run(debug=True)