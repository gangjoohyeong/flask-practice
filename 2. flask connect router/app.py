# Flask 객체를 가져오기
from flask import Flask

# app이라는 이름으로 객체 생성
app = Flask(__name__)

# /hello 라우터 접속
@app.route("/hello")
def test(): # 함수명 무관                           
    Title = '<h1>Hello Flask!</h1>'
    contents = '반갑습니다, 내 이름은 강주형, 플라스크 공부하기'
    
    return Title + contents

# 이 파일이 모듈이 아니면 웹 서버를 띄워라
if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8080")
    
    
# http://127.0.0.1:8080/hello -> 접속 가능