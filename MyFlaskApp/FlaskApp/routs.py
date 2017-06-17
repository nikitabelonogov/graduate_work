from FlaskApp import app, openFace, clf
from flask import redirect
from flask import render_template
from flask import request

from FlaskApp import helpers


@app.route('/', methods=['GET'])
def index():
    """

    :return:
    """
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload():
    """

    :return:
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
