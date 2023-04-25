from flask import Flask

app = Flask(__name__)

# 2021.12 업데이트 이후 debug 값을 미리 설정?
# debug = False: 실제 서비스 가정
app.debug = False

# debug가 False일 때, (개발이 아니라 상용화할 때 실행)
# 실제 서비스에서 오류가 발생하면 로그를 남겨야 하니까!
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    
    # 한 파일에 2000바이트까지
    # 10개의 파일까지 생성하겠다
    # 그 이후엔 덮어씌우는 식으로 계속 로깅함
    file_handler = RotatingFileHandler('joohyeong_server.log', maxBytes=2000, backupCount=10)
    
    # WARNING과 그것보다 심각한 상황에서 logging 하겠다.
    file_handler.setLevel(logging.WARNING)
    
    # app.logger.addHandler() 에 등록시켜줘야 app.logger로 사용 가능
    app.logger.addHandler(file_handler)
    

@app.errorhandler(404)
def page_not_found(error):
    # ERROR 레벨로 로깅
    # ERROR 레벨은 위에서 setLevel한 WARNING보다 심각한 Level이기 때문에 수행됨
    app.logger.error('404 ERROR !!, OMG!!')
    return "<h2>404 ERROR !!!!!</h2>", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')

# joohyeong_server.log

# 404 ERROR !!, OMG!!
# 404 ERROR !!, OMG!!
# 404 ERROR !!, OMG!!
# (에러 발생될 때마다 자동 생성)