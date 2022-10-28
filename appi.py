from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from forms import CalculationForm
from metrixohjelma import getcompensation

app = Flask(__name__, static_folder='static')
app.secret_key = '1234567'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CalculationForm(request.form)
    if request.method == 'POST':
        course_url = form.course_urll.data
        tulos = form.tuloss.data
        rating = form.ratingg.data

        dicti = getcompensation(course_url, tulos, rating)
        if "error" in dicti:
            flash(dicti["error"])
        else:
            stringi = """
            Round Rating: {ratingg}
            Compensated result: {result}
            """.format(ratingg=dicti["round_rating"], result=dicti["suhteutettu"])
            flash(stringi)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)