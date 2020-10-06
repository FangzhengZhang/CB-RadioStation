"""This py class will be the main class to start the server"""

from flask import Flask, redirect, url_for
import sys
import service


app = Flask(__name__)

@app.route("/")
def home():
    return "The home page is working"

@app.route("/sys_status")
def sys_status():
    return "Sys status page is showing."




if __name__ == "__main__":
    if len(sys.argv) == 3:
        addr = sys.argv[1]
        port = sys.argv[2]
    else:
        print("Did not give address and port, so use default address and port.")
        addr="192.168.1.182"
        port=8080
    app.run(host=addr, port=port, debug=True)