from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')

def index(title):
    param = {}
    param["h1"] = "Миссия Колонизация Марса"
    param["h4"] = "И на Марсе будут яблони цвести!"
    param["title"] = title
    return render_template('base.html', **param)




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
