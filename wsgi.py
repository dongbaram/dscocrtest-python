# -*- coding: UTF-8 -*-
import os, json
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@application.route("/")
def hello():
    return "OpenShift Hello World!"


@application.route('/fileUpload', methods=['POST'])
def upload_file(): 
    #업로드 경로가 존재하는지 확인 - 없으면 생성함
 
    if not os.path.isdir(application.config['UPLOAD_FOLDER']):
        print('create folder')
        os.mkdir(application.config['UPLOAD_FOLDER'])

    file = request.files['ocrfile']

    #jsontmp = request.get_json(silent=True, cache=False, force=True)
    #print(request)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
        #return redirect(url_for('uploaded_file', filename=filename))
        print('debug1')
        return 'uploaded'
    return 'error'

if __name__ == "__main__":
    application.run()
