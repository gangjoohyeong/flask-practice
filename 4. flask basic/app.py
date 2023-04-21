from flask import Flask

app = Flask(__name__)

# 기본 routing
@app.route("/")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/hello")
def hello_flask():
    return "<h1>Hello Flask!</h1>"

# 연산 적용해보기
@app.route("/profile/<user_id>")
def get_profile(user_id):
    return "User ID: " + user_id

@app.route("/times_5/<int:data>")
def times_5(data):
    return f"data * 5 = {data * 5}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")