import os, json
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
