# Import modules and packages
from flask import (
    Flask,
    request,
    render_template,
    url_for,
    flash,
    redirect
)
import pickle
import numpy as np
from scipy.spatial import distance
import plotly.graph_objs as go
from plotly.offline import plot
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'
    
    if request.method == 'POST':
        input_val = request.form.to_dict()
        print(input_val)
        player_name = input_val['player_name']
        start_date = input_val['start-date']
        end_date = input_val['end-date']
        # if player_name =="" or start_date =="" or end_date =="":
        #     flash('Invalid input: Input cannot be empty.', 'warning')
        #     return redirect(url_for('index'))
        # Example: Load your DataFrame here
        # For demonstration, assuming a DataFrame `data` exists
        data = pd.DataFrame({
            'coord_x': [1,2],
            'coord_y': [1,2],
            'player_name': ['adf','fd']
        })


        # Generate a Plotly figure
        fig = go.Figure(data=go.Scatter(x=data['coord_x'], y=data['coord_y'], mode='markers', marker_color='#ff0000', text=data['player_name']))

        # Convert the figure to HTML
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        
        

        title = f"{player_name} hotspots from {start_date} to {end_date}"
        
        return render_template('index.html', plot_div=plot_div, title =title)

@app.route('/filter', methods=['POST', 'GET'])
def fitler():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'
    
    if request.method == 'POST':
        input_val = request.form.to_dict()
        print(input_val)
        player_name = input_val['player_name']
        start_date = input_val['start-date']
        end_date = input_val['end-date']
        # if player_name =="" or start_date =="" or end_date =="":
        #     flash('Invalid input: Input cannot be empty.', 'warning')
        #     return redirect(url_for('index'))
        # Example: Load your DataFrame here
        # For demonstration, assuming a DataFrame `data` exists
        data = pd.DataFrame({
            'coord_x': [1,2],
            'coord_y': [1,2],
            'player_name': ['adf','fd']
        })


        # Generate a Plotly figure
        fig = go.Figure(data=go.Scatter(x=data['coord_x'], y=data['coord_y'], mode='markers', marker_color='#ff0000', text=data['player_name']))

        # Convert the figure to HTML
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        
        

        title = f"{player_name} hotspots from {start_date} to {end_date}"
        
        return render_template('index.html', plot_div=plot_div, title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
