from flask import Flask, render_template, session, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, ValidationError
from flask_bootstrap import Bootstrap
from compute import compute

class SearchForm(FlaskForm):
    year = SelectMultipleField('Year', choices=[('2017','2017'),('2018','2018'),('2019','2019')], validators = [DataRequired()])
    clg_name = StringField("College")
    branch = StringField("Branch")
    cat = SelectField('Category', choices=[('OPEN','OPEN'),('OBC', 'OBC-NCL'),('SC', 'SC'),('ST','ST'),('PwD','PwD'),('EWS','GEN-EWS')], validators = [DataRequired()])
    gender = SelectField('Gender Category', choices=[('Neut', 'Gender-Neutral'), ('Fem','Female-Only')], validators = [DataRequired()])
    #dur = SelectField('Program Type', choices=[('4', 'BTech (4 Years)'), ('5', 'Dual Degree (5 Years)')])
    submit = SubmitField("SUBMIT")


app=Flask(__name__)
app.config['SECRET_KEY'] ="replace_later"
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form=SearchForm(request.form)
    #if request.method=='POST' and form.validate():
    if form.validate_on_submit():
        print("Validate!")
        college = form.clg_name.data
        branch = form.branch.data
        sel_years = form.year.data
        cats = form.cat.data
        genders = form.gender.data
        #dur = form.dur.data
        tables = compute(college, branch, sel_years, cats, genders) #,dur
    else:
        tables = None

    return render_template('index.html', form=form, tables=tables, years = form.year.data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/intellitrak_home')
def intellitrak_home():
    return redirect('www.intellitrak.in/josaa')

if(__name__=="__main__"):
    app.run()