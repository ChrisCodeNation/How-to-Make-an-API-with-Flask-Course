from flask import Flask
from flask import render_template

"""
在01的範例中，可以透過return string將內容印在網頁上
但實際上不可能把整個HTML都跟python寫在一起
所以可以透過render_template來解決

需建立一個templates資料夾，當使用render_plate的時候
flask就會先到templates資料夾尋找對應的文件
"""

# 固定格式
app = Flask(__name__)


@app.route('/')
def render():
    return render_template('./abc.html')

if __name__ == "__main__":
    app.run(debug=True)