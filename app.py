import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def wel_msg():
    # color = os.environ.get('COLOR', "green") 
    message = "Hello from the App's Docker image deployed on Minishift" 
    return message

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run()
