from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World! It's Cameron"


if __name__ == "__main__":
    app.run(debug=True)