from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test", methods =['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method == 'POST':
        print('POST')
        data = request.get_json()
        print(data)
        # POST는 파라미터들도 다 들고 와서 사전처럼 꺼내서 사용
        print(data['email'])
    if request.method == 'GET':
        print('GET')
        user = request.args.get('email')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print(user)
    if request.method == 'DELETE':
        print('DELETE')
        user = request.args.get('email')
        print(user)
    return make_response(jsonify({'status' : True}), 200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
    
    
    
# 접속 테스트
# vue_restapi.html을 Liver server로 실행 후 button 클릭해서
# console에서 interaction 확인