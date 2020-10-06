from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "The main page is working"

if __name__ == "__main__":
    app.run()