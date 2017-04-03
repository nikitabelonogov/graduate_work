from flask import Flask

from MyGoogleAPI import MyGoogleAPI
from MyOpenFace import MyOpenFace


# a bunch of kludges
app = None
googleAPI = None
openFace = None


def init(google_api_key, dlib_path, network_model):
    # a bunch of kludges
    global app
    global googleAPI
    global openFace
    app = Flask(__name__)
    googleAPI = MyGoogleAPI(google_api_key)
    openFace = MyOpenFace(dlib_path, network_model)

    if app:
        import routs
