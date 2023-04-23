from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_loop')
def hello_name():
    user_list = ['joohyeong', 'gildong', 'booduk']
    email_list = ['bles@kakao.com', 'gildong@gmail.com', 'booduk@naver.com']
    return render_template('loop.html', users = user_list, emails = email_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
    
    
# 접속 테스트
# http://127.0.0.1:8080/hello_loop