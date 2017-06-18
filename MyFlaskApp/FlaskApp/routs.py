from FlaskApp import app, openFace, clf
from flask import redirect
from flask import render_template
from flask import request

from FlaskApp import helpers


@app.route('/', methods=['GET'])
def index():
    """
    Response user interface html.
    :return: user interface html
    """
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload():
    """
    Perform a face recognition, face align, NN forward and classification.
    :return: gender prediction.
    """
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    image = helpers.stream_to_image(file.stream)
    align = openFace.face_align(image)
    rep = openFace.forward(align)
    return str(clf.gender.predict([rep])[0])
