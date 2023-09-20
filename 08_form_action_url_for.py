from flask import Flask
from flask import request
from flask import render_template

"""
07的範例中是把url寫死的，只要app.route('路由')調整了
就會像04範例中提到的，需要修改所有用到這個路由的文件
所以最好的辦法，還是透過url_for設置
"""

# 固定格式
app = Flask(__name__)

@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Hello ' + request.values['username']

    return render_template('/form_action_url_for.html')

if __name__ == "__main__":
    app.run(debug=True)