from flask import Flask

app = Flask(__name__)

if app:
    import routs
