from flask import Flask, render_template
from forms import YearForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e388702a9f1ecf45eb7724f78c68825e'

@app.route('/', methods=['GET','POST'])
def homepage():
	form = YearForm()
	return render_template('home.html', form=form)

@app.route('/about')
def aboutpage():
	return render_template('about.html', title='About')

@app.route('/contact')
def contactpage():
	return render_template('contact.html', title='Contact')


if __name__ == '__main__':
	app.run(debug=True)