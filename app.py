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

@app.route('/list_prof/<ol>')
def training(ol):
    profs = [
        "инженер исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]
    param = {}
    param["ol"] = ol
    param["profs"] = profs
    return render_template('list_prof.html', **param)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
