#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:21:02 2019

@author: bryant
"""

import pandas as pd 
import plotly.graph_objs as go

def plotly_model(df, forecast, title = "", xlab = 'ds', ylab = 'Y', trend = False, point_estimate = True):
  '''
  A function that produces a plotly plot of a prophet model
  
  
  Parameters
  ----------
  
  df - A pandas DataFrame used to fit a prophet model
  
  forecast - a pandas DataFrame produced by the prophet predict() function
  
  title - optional string to be used as plot title
  
  xlab - optional string to be used as x label. Defaults to 'ds', fbprophet convention.
  
  ylab - optional string to be used as y label. Defualts to 'y', fbprophet convention.
  
  Returns
  -------
  
  a plotly figure
  
  '''
  points = go.Scatter(
      name='Actual',
      x=df['ds'],
      y=df['y'],
      mode='markers',
      marker=dict(color="black"))

  upper_bound = go.Scatter(
      name='Upper Interval',
      x=forecast['ds'],
      y=forecast['yhat_upper'],
      mode='lines',
      marker=dict(color="#554"),
      line=dict(width=0),
      fillcolor='rgba(68, 68, 68, 0.3)',
      fill='tonexty')

  trace = go.Scatter(
      name='Predicted',
      x=forecast['ds'],
      y=forecast['yhat'],
      mode='lines',
      line=dict(color='rgb(31, 119, 180)'),
      fillcolor='rgba(68, 68, 68, 0.3)',
      fill='tonexty')

  trace_t = go.Scatter(
      name='trend',
      x=forecast['ds'],
      y=forecast['trend'],
      mode='lines',
      line=dict(color='rgb(31, 119, 180)'),
      fillcolor='rgba(68, 68, 68, 0.3)')

  lower_bound = go.Scatter(
      name='Lower Interval',
      x=forecast['ds'],
      y=forecast['yhat_lower'],
      marker=dict(color="#554"),
      line=dict(width=0),
      mode='lines')
  
  if trend == True and point_estimate == True:
      data = [points, trace_t,lower_bound, trace, upper_bound]
  elif trend == True and point_estimate == False:
      data = [points, trace_t,lower_bound, upper_bound]
  elif trend == False and point_estimate == False:
      data = [points,lower_bound, upper_bound]
  else:
      data = [points, lower_bound, trace, upper_bound]




  

  layout = go.Layout(
      yaxis=dict(title=ylab),
      xaxis=dict(title=xlab),
      title=title,
      showlegend = False)

  fig = go.Figure(data=data, layout=layout)
  return fig