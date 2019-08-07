from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/about')
def aboutpage():
	return render_template('about.html', title='About')

@app.route('/contact')
def contactpage():
	return render_template('contact.html', title='Contact')


if __name__ == '__main__':
	app.run(debug=True)