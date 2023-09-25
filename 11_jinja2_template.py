from flask import Flask, request, redirect, url_for, render_template, flash

# 固定格式
app = Flask(__name__)

# 登入畫面
@app.route('/loginurl', methods=['GET', "POST"])
def login():
    if request.method == 'POST':
        if check(request.form['username'], request.form['password']):
            flash('Login Success')
            return redirect(url_for('hello', username=request.form.get('username')))
    
    return render_template('11_login.html')

def check(username, password):
    if username == "admin" and password == "hello":
        return True
    else:
        return False

# hello page畫面
@app.route('/hello/<username>')
def hello(username):
    return render_template('10_hello.html', username=username)

if __name__ == "__main__":
    app.secret_key = "Your Key"
    app.run(debug=True)