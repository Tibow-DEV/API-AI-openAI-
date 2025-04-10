from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/json")
def hello_json():
    return { "message": "Hello, World!" }

# Flask app simple_server run
if __name__ == "__main__":
    app.run(host="localhost", port=9090, debug=True)
