from flask import Flask
import requests

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(err0r):
    return '<h2>404 Error!!!</h2>', 404

@app.route('/google')
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
    
# 접속 테스트
# http://127.0.0.1:8080/
# http://127.0.0.1:8080/google
