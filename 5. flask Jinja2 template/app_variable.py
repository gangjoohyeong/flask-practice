from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/hello/<username>')
def hello_name(username):
    return render_template('variable.html', username=username, time=datetime.now())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
    
# 접속 테스트
# http://127.0.0.1:8080/hello/joohyeong
# -> joohyeong, 현재 시간 출력 확인