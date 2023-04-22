from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login')

def login():
    user_name = request.args.get('name')
    user_pw = request.args.get('pw')
    user_email = request.args.get('email')
    
    # 변수 리턴 확인
    print(f'user_name: {user_name}, user_pw: {user_pw}, user_email: {user_email}')
    
    if user_name =='joohyeong':
        data = {'auth' : 'success'}
    else:
        data = {'auth' : 'failed'}
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='8080')
    
# 접속 테스트
# http://127.0.0.1:8080/login?name=joohyeong
# http://127.0.0.1:8080/login?name=joohyeong&pw=1234&email=bles@kakao.com
# http://127.0.0.1:8080/login?name=gildong&pw=1111&email=gildong@naver.com