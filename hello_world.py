# Import the Flask framework
from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Main driver function
if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
