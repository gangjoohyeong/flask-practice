from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_condition')
def hello_html():
    age = 26
    return render_template('condition.html', my_age=age)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')