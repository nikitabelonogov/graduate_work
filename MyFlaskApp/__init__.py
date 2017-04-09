import pickle

from sklearn import svm

from flask import Flask

from MyGoogleAPI import MyGoogleAPI
from MyOpenFace import MyOpenFace

app = None
openFace = None
clf = None


def init(dlib_path, network_model, datapath):
    global app
    global openFace
    global clf
    app = Flask(__name__)
    openFace = MyOpenFace(dlib_path, network_model)
    clf = svm.SVC()
    with open(datapath, 'rb') as input:
        data = pickle.load(input)
    reps = []
    y = []
    for k, v in data.items():
        if v[1].has_key('gender'):
            rep = v[0]
            gender = v[1]['gender']
            reps.append(rep)
            y.append(gender)
    clf.fit(reps, y)

    if app:
        import routs
