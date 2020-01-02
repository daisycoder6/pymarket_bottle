from bottle import Bottle, run, get, post, request, route, template, response
from pymarket.pymarket import dashboard
import pandas as pd


@route('/')
#@view('topten')
def topten():

	# print(dict(request.headers))

	# topten = dashboard('ftse100'). This runs the code

	topten = pd.read_csv('dashboard.csv').head(10).to_html()

	print(topten)

	output = template('topten', table=topten)

	return output


if __name__ == '__main__':

	run(host='localhost', port=8080,debug=True,reload=True)