from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_route():
    print("route is called")

    return "<h1>Hello, Python course!</h1> <p>Test</p>"
