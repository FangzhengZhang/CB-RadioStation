"""This py class will be the main class to start the server"""

from flask import Flask, redirect, url_for
import sys
import service_class

service = service_class.service()


app = Flask(__name__)


@app.route("/")
def home():
    return "The home page is working"

@app.route("/sys_status")
def sys_status():
    return service.debug_print()

@app.route("/get_local_music_list")
def get_local_music_list():
    """json example {"local_music_list": ["AJR - Sober UpCopy.mp3", "AJR - Sober Up.mp3"]}"""
    return service.get_local_music_list()

@app.route("/play_music")
def play_music(music_name):
    """"""
    return service.play_music(request.args.get('song'))



if __name__ == "__main__":
    if len(sys.argv) == 3:
        addr = sys.argv[1]
        port = sys.argv[2]
    else:
        print("Did not give address and port, so use default address and port.")
        addr="192.168.1.182"
        port=8080
    app.run(host=addr, port=port, debug=True)