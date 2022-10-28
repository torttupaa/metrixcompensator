from wtforms import Form, StringField, validators

class CalculationForm(Form):
    course_urll = StringField('Course metrix URL', [validators.DataRequired()])
    tuloss = StringField('Score (relative to par)', [validators.DataRequired()])
    ratingg = StringField('Player rating', [validators.DataRequired()])
