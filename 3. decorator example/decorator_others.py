from flask import Flask 

app = Flask(__name__)   
# app.debug = True
@app.before_first_request
def before_first_request():
    print ("Flask 실행 후 첫 요청 때 실행")
 
@app.before_request
def before_request():
    print ("HTTP 요청 들어올 때마다 실행")
 
@app.after_request
def after_request(response):
    print ("HTTP 요청 처리 끝나고 브라우저에 응답하기 전에 실행")
    return response

    
@app.route("/hello")
def hello():                           
    return "<h1>Decorator Test Page</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
    
# http://127.0.0.1:8080/ 접속 후 터미널 출력 확인