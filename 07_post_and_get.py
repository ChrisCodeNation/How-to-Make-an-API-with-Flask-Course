from flask import Flask
from flask import request
from flask import render_template
"""
設計一個login頁面接收使用者的名字，
並回傳歡迎的訊息給使用者
"""

# 固定格式
app = Flask(__name__)

# 設置要用的method
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 利用request來捕捉使用者的動作是否為POST
    if request.method == 'POST':
        # 透過request.values取得form的內容
        return 'Hello ' + request.values['username']
    # html文件記得放入templates資料夾
    return render_template('./post_and_get.html')

if __name__ == "__main__":
    app.run(debug=True)