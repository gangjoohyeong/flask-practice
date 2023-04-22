from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/login')

def login():
    user_email = request.args.get('email')
    user_pw = request.args.get('pw')
    
    # 변수 리턴 확인
    print(f'user_email: {user_email}, user_pw: {user_pw}')
    
    if user_email =='bles@kakao.com' and user_pw == '7777':
        data = {'auth' : 'success'}
    else:
        data = {'auth' : 'failed'}
    
    return jsonify(data)

@app.route('/bs_login_test')
def bootstrap_login():
   return render_template('bootstrap_login.html') 


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='8080')
    
# 접속 테스트
# http://127.0.0.1:8080/login?email=bles@kakao.com&pw=7777
# http://127.0.0.1:8080/bs_login_test 
# -> ID/Password submit 후 auth 결과 확인
# auth를 Front-end가 받으면 그걸 활용해서 이것 저것.. 하는 것