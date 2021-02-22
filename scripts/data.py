# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:30:55 2021

@author: lself
"""

import pandas as pd
from collections import OrderedDict
import requests
import plotly.graph_objects as go
from plotly.offline import plot

states_default = OrderedDict([('Alabama', 'AL')])

def return_figures(states=states_default):
    """Creates a plotly visualization using the COVID tracking API
       (http://covidtracking.com/data/api)
    
    # Example of the COVID API endpoint:
    # https://api.covidtracking.com/v1/states/{state}/daily.json by state
    
    Args:
        state_default (tuple): tuple of the selected state for filtering the data
        
    Returns:
        list (dict): list containing the (possibly) multiple visualizations
        
    """
    
    # when the states variable is empty, use the states_default dictionary
    if not bool(states):
        states = states_default
        
    # prepare filter data for the COVID API
    states_filter = list(states.values())
    states_filter = [x.lower() for x in states_filter]
    #print(states_filter)
    
    url = "https://api.covidtracking.com/v1/states/" + states_filter[0] + "/daily.json"
    
    try:
        r = requests.get(url)
        data = pd.DataFrame(r.json())
    except:
        data = pd.DataFrame()
        print('could not load data ', )
        return data
        
    # sort values by date ascending
    data = data.sort_values('date').reset_index()
    # convert date column to a date data type (yyyy-mm-dd)
    data['date'] = pd.to_datetime(data['date'], format='%Y%m%d')
    # create 7-day moving average of new positives
    data['positives_SMA_07'] = data['positiveIncrease'].rolling(window=7).mean()
    # create 7-day moving average of new hospitalizations
    data['hospitalizations_SMA_07'] = data['hospitalizedIncrease'].rolling(window=7).mean()
    # create 7-day moving average of new deaths
    data['deaths_SMA_07'] = data['deathIncrease'].rolling(window=7).mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['date'], 
                             y=data['positives_SMA_07'],
                             fill='tozeroy',
                             name='Positives'))
    fig.add_trace(go.Scatter(x=data['date'], 
                             y=data['hospitalizations_SMA_07'],
                             fill='tozeroy',
                             name="Hospitalizations"))
    fig.add_trace(go.Scatter(x=data['date'], 
                             y=data['deaths_SMA_07'],
                             fill='tozeroy',
                             name='Deaths'))
    fig.update_layout(title='7-day moving averages for ' + list(states.keys())[0])

    figures = [fig]
    
    
    
    return figures
    
    
if __name__ == "__main__":
    state_dict = {'Washington': 'WA'}
    figures = return_figures(state_dict)
    
    plot(figures[0])