from flask import Flask, render_template, flash, redirect, url_for
from forms import YearForm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([[2010, 135852050, 137349430, 71795963],
				 [2011, 131478008, 132698098, 78700393],
				 [2012, 138690752, 139961329, 80311914],
				 [2013, 140538870, 140591029, 82583209],
				 [2014, 138039214, 139236392, 86299608],
				 [2015, 136044073, 134865553, 88157039],
				 [2016, 142854335, 142593453, 89447376],
				 [2017, 147561589, 146891116, 90252401],
				 [2018, 156478534, 156313637, 90769882]
				])

budget_df = pd.DataFrame(data, columns = ['year', 'budget', 'total_xpend', 'tax_mcp'])

class univariate_linear_regression_model:
		  
	def __init__(self):
		self.b = 0.0
		self.i = 0.0

	def ssxx(self, x):
		return sum((x-np.mean(x))**2)

	def ssxy(self, x, y):
		xmean = np.mean(x)
		ymean = np.mean(y)
		return sum((x-xmean)*(y-ymean))

	def train(self, x, y):
		# Verify the size of the features and labels match
		assert(len(x) == len(y)) 
		ss_xy = self.ssxy(x, y)
		ss_xx = self.ssxx(x)
		self.b = ss_xy/ss_xx
		mux = np.mean(x)
		muy = np.mean(y)
		self.i = muy - self.b*mux
	def predict(self, x):
		predictions = np.zeros(len(x))
		for i in range(len(x)):
			predictions[i] = self.b * x[i] + self.i
		return predictions



app = Flask(__name__)

app.config['SECRET_KEY'] = 'e388702a9f1ecf45eb7724f78c68825e'

@app.route('/', methods=['GET','POST'])
def homepage():
	form = YearForm()
	if form.validate_on_submit():

		year = budget_df['year']
		budget = budget_df['budget']
		total_xpend = budget_df['total_xpend']
		tax_mcp = budget_df['tax_mcp']

		
		bdgt = univariate_linear_regression_model()
		txpd = univariate_linear_regression_model()
		tmcp = univariate_linear_regression_model()

		bdgt.train(year, budget)
		txpd.train(year, total_xpend)
		tmcp.train(year, tax_mcp)

		y_pred_b = []
		x_pred_b = np.linspace(2009, 2018)
		for index in range(len(x_pred_b)):
			y_pred_b.append(bdgt.predict([x_pred_b[index]]))

		y_pred_e = []
		x_pred_e = np.linspace(2009, 2018)
		for index in range(len(x_pred_e)):
			y_pred_e.append(txpd.predict([x_pred_e[index]]))

		y_pred_t = []
		x_pred_t = np.linspace(2009, 2018)
		for index in range(len(x_pred_t)):
			y_pred_t.append(tmcp.predict([x_pred_t[index]]))

		
		fig, ax = plt.subplots()
		ax.plot(year, budget, 'o')
		ax.plot(x_pred_b, y_pred_b)
		plt.ylabel('USD (hundreds of thousands)')
		plt.xlabel('Year')
		plt.title('')
		plt.savefig('static/images/plot4.png')

		fig, ax = plt.subplots()
		ax.plot(year, total_xpend, 'o')
		ax.plot(x_pred_e, y_pred_e)
		plt.ylabel('USD (hundreds of thousands)')
		plt.xlabel('Year')
		plt.title('')
		plt.savefig('static/images/plot5.png')

		fig, ax = plt.subplots()
		ax.plot(year, tax_mcp, 'o')
		ax.plot(x_pred_t, y_pred_t)
		plt.ylabel('USD (thousands)')
		plt.xlabel('Year')
		plt.title('')
		plt.savefig('static/images/plot6.png')

		pred_year = form.year.data

		p_1 = int(bdgt.predict([pred_year]))
		p_2 = int(txpd.predict([pred_year]))
		p_3 = int(tmcp.predict([pred_year]))

		p_1 = '{:,}'.format(p_1)
		p_2 = '{:,}'.format(p_2)
		p_3 = '{:,}'.format(p_3)

		return render_template('home.html', scroll='input', check=True, 
								budget_df=budget_df, form=form, 
								url1='/static/images/plot4.png', url2='/static/images/plot5.png',
								url3='/static/images/plot6.png', p1 = p_1, p2 = p_2,
								p3 = p_3)
	return render_template('home.html', scroll='bl', form=form)

@app.route('/about')
def aboutpage():
	return render_template('about.html', title='About')

@app.route('/contact')
def contactpage():
	return render_template('contact.html', title='Contact')


if __name__ == '__main__':
	app.run(debug=True)