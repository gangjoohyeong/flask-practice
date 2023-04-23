from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_condition')
def hello_html():
    age = 26
    return render_template('condition.html', my_age=age)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
    
    
    
# 접속 테스트
# http://127.0.0.1:8080/hello_condition
# router로 age를 지정하고 싶으면 어떻게 할까?