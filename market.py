from bottle import Bottle, run, get, post,static_file
from bottle import request, route, template, response
from pymarket.pymarket import dashboard
import pandas as pd


@route('/')
#@view('topten')
def topten():

    # topten = dashboard('ftse100'). This runs the code
    topten = pd.read_csv('dashboard.csv').head(10).to_html()
    output = template('topten2', table=topten)

    return output

@route('/static/<filename:path>')
def fetch_static(filename):
    """
    Serves upthe static content. we require the path filter
    as wehave subdirectories under static
    """
    #response.set_header('Cache-Control', 'max-age=600')
    return static_file(filename, root='static')


if __name__ == '__main__':

    run(host='localhost', port=8080,debug=True,reload=True)