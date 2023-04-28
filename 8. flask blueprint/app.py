from flask import Flask
from sub_blueprint import blog_test


app = Flask(__name__)
# (blueprint 객체명, url_prefix: 기본 경로명)
app.register_blueprint(blog_test.blog_ab, url_prefix='/blog')

# http://127.0.0.1:8080/기본 경로명/라우팅 경로

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
    
    
# 접속 테스트
# http://127.0.0.1:8080/blog/blog1
# http://127.0.0.1:8080/blog/blog2