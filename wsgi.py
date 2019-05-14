import os, json
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@application.route("/")
def hello():
    return "OpenShift Hello World!"


@application.route('/fileUpload', methods=['POST'])
def upload_file(): 
    file = request.files['ocrfile']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))

        print('debug1')
        return 'uploaded'
    return 'error'


if __name__ == "__main__":
    application.run()
