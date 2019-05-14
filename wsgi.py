import os, json
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
application = Flask(__name__)

@application.route("/")
def hello():
    return "OpenShift Hello World!"

if __name__ == "__main__":
    application.run()
