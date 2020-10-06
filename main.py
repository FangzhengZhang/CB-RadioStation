from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "The main page is working"

if __name__ == "__main__":
    app.run(host="192.168.1.182", port=8080, debug=True)