from flask import Flask, render_template, flash, redirect, url_for
from forms import YearForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e388702a9f1ecf45eb7724f78c68825e'

@app.route('/', methods=['GET','POST'])
def homepage():
	form = YearForm()
	if form.validate_on_submit():
		#flash(f'Your year is {form.year.data}', 'success')
		return render_template('home.html', scroll='op', check=True, form=form)
	return render_template('home.html', form=form)

@app.route('/about')
def aboutpage():
	return render_template('about.html', title='About')

@app.route('/contact')
def contactpage():
	return render_template('contact.html', title='Contact')


if __name__ == '__main__':
	app.run(debug=True)