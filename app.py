# Import modules and packages
from flask import (
    Flask,
    request,
    render_template,
    url_for
)
import pickle
import numpy as np
from scipy.spatial import distance
import plotly.graph_objs as go
from plotly.offline import plot

app = Flask(__name__)

@app.route('/')
def index():
    # if request.method == 'GET':
    #     return 'The URL /predict is accessed directly. Go to the main page firstly'
    
    # if request.method == 'POST':
    #     input_val = request.form.to_dict()

    #     # Example: Load your DataFrame here
    #     # For demonstration, assuming a DataFrame `data` exists
    #     data = pd.DataFrame({
    #         'coord_x': [1,2],
    #         'coord_y': [1,2],
    #         'player_name': ['adf','fd']
    #     })
        # filtered_data = data[(data['PlayerName'] == player_name) & (data['Season'] >= start_season)]

    #     # Instead of calculating Euclidean distances to centroids,
    #     # let's directly plot the DataFrame for demonstration purposes
    #     # You can replace this part with your actual data processing logic

    #     # Generate a Plotly figure
    #     fig = go.Figure(data=go.Scatter(x=data['coord_x'], y=data['coord_y'], mode='markers', marker_color=data['player_name'], text=data['player_name']))

    #     # Convert the figure to HTML
    #     plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    #     return render_template('index.html', plot_div=plot_div)
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_input_values():
    val = request.form['my_form']

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'
    
    if request.method == 'POST':
        input_val = request.form.to_dict()

        # Example: Load your DataFrame here
        # For demonstration, assuming a DataFrame `data` exists
        data = pd.DataFrame({
            'coord_x': [1,2],
            'coord_y': [1,2],
            'player_name': ['adf','fd']
        })

        # Instead of calculating Euclidean distances to centroids,
        # let's directly plot the DataFrame for demonstration purposes
        # You can replace this part with your actual data processing logic

        # Generate a Plotly figure
        fig = go.Figure(data=go.Scatter(x=data['coord_x'], y=data['coord_y'], mode='markers', marker_color=data['player_name'], text=data['player_name']))

        # Convert the figure to HTML
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)

        return render_template('predict.html', plot_div=plot_div)

# @app.route('/predict', methods=['POST', 'GET'])
# def predict():
#     if request.method == 'GET':
#         return 'The URL /predict is accessed directly. Go to the main page firstly'

#     if request.method == 'POST':
#         input_val = request.form

#         if input_val != None:
#             # collecting values
#             vals = []
#             for key, value in input_val.items():
#                 vals.append(float(value))

#         # Calculate Euclidean distances to freezed centroids
#         with open('freezed_centroids.pkl', 'rb') as file:
#             freezed_centroids = pickle.load(file)

#         assigned_clusters = []
#         l = []  # list of distances

#         for i, this_segment in enumerate(freezed_centroids):
#             dist = distance.euclidean(*vals, this_segment)
#             l.append(dist)
#             index_min = np.argmin(l)
#             assigned_clusters.append(index_min)

#         return render_template(
#             'predict.html', result_value=f'Segment = #{index_min}'
#             )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
