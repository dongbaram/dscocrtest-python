import os, json
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
