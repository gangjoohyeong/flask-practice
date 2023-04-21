from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json_test')
def json_test1():
    # Python의 Dictionary 타입
    data ={'name': '강주형', 'mail': 'bles@kakao.com'}
    return jsonify(data)

@app.route('/server_info')
def json_test2():
    data = { 'server_name' : '0.0.0.0', 'server_port' : '8081' }
    return jsonify(data)

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8081")


# 접속 테스트
# http://127.0.0.1:8081/json_test
# http://127.0.0.1:8081/server_info