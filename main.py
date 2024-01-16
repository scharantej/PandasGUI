 
# Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd

# Create a Flask app
app = Flask(__name__)

# Load the pandas DataFrame
df = pd.read_csv('data.csv')

# Define the main route
@app.route('/')
def index():
    return render_template('index.html', df=df)

# Define the about route
@app.route('/about')
def about():
    return render_template('about.html')

# Define the filter route
@app.route('/filter', methods=['POST'])
def filter():
    # Get the filter criteria from the form
    filter_column = request.form.get('filter_column')
    filter_value = request.form.get('filter_value')

    # Filter the DataFrame
    filtered_df = df[df[filter_column] == filter_value]

    # Return the filtered DataFrame
    return render_template('index.html', df=filtered_df)

# Define the sort route
@app.route('/sort', methods=['POST'])
def sort():
    # Get the sort criteria from the form
    sort_column = request.form.get('sort_column')
    sort_order = request.form.get('sort_order')

    # Sort the DataFrame
    sorted_df = df.sort_values(sort_column, ascending=sort_order == 'asc')

    # Return the sorted DataFrame
    return render_template('index.html', df=sorted_df)

# Run the app
if __name__ == '__main__':
    app.run()
