# This code sets up a simple Flask web server and a background thread to keep it alive.

# Import the Flask framework to create a web application.
from flask import Flask

# Import the Thread class from the threading module to run the Flask app in the background.
from threading import Thread

# Create a Flask web application instance.
app = Flask('')


# Define a route for the root URL ('/'). When accessed, it returns a message indicating that the server is alive.
@app.route('/')
def home():
  return "Hello. I am alive!"


# Function to run the Flask app on the server.
def run():
  app.run(host='0.0.0.0', port=8080)


# Function to start the Flask app in a background thread.
def keep_alive():
  t = Thread(target=run)
  t.start()
