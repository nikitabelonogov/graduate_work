from flask import Flask

from MyClassificator import MyClassificator
from MyOpenFace import MyOpenFace

app = None
openFace = None
clf = None


def init(dlib_path, network_model, data_path):
    """

    :param dlib_path:
    :param network_model:
    :param data_path:
    :return:
    """
    global app
    global openFace
    global clf
    app = Flask(__name__)
    openFace = MyOpenFace(dlib_path, network_model)
    clf = MyClassificator(data_path)

    if app:
        import routs
