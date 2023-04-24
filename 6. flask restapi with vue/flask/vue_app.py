from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['GET'])
def test():
    return make_response(jsonify(success=True), 200)

if __name__=="__main__":
    app.run(host="0.0.0.0", port="8080")

# 접속 테스트
# http://127.0.0.1:8080/test