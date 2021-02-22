# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:35:08 2021

@author: lself
"""
from covidwebapp import app

import plotly
import json
from flask import render_template, request
from scripts.data import return_figures



@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    
    # List of states for filter
	state_codes = [['Alabama','AL'],['Arkansas','AR'],['Florida','FL'],
	['Georgia','GA'],['Kentucky','KY'],['Louisiana','LA'],['Mississippi','MS'],
	['North Carolina','NC'],['South Carolina','SC'],['Tennessee','TN']]

	# Parse the POST request countries list
	if (request.method == 'POST') and request.form:
		figures = return_figures(request.form)
		states_selected = []

		for state in request.form.lists():
			states_selected.append(state[1][0])
	
	# GET request returns all states for initial page load
	else:
		figures = return_figures()
		states_selected = []
		for state in state_codes:
			states_selected.append(state[1])

	# plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html', ids=ids,
		figuresJSON=figuresJSON,
		all_states=state_codes,
		states_selected=states_selected)




if __name__ == '__main__':
    pass