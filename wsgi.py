#-*- encoding: utf-8 -*-
import os, json
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

##한글사용 - 한글사용은 되나 print해도 log에 안나옴... 서버에 올릴때 활성화
#import sys, io
#sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
#sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
 

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'tif'])

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def checkdir_d():
    if os.path.isdir(application.config['UPLOAD_FOLDER']):
        return True
    else:
        return False


@application.route("/")
def hello():
    return "Hello World!"

@application.route('/fileUpload', methods=['POST'])
def upload_file(): 
    #업로드 경로가 존재하는지 확인 - 없으면 생성함
    import datetime
    now  = datetime.datetime.now()
    #print(now) 
    #print(now.strftime('%Y-%m-%d %H:%M:%S:%f')) 

    if not os.path.isdir(application.config['UPLOAD_FOLDER']):
        print('create folder')
        os.mkdir(application.config['UPLOAD_FOLDER'])

    file = request.files['ocrfile']
    print(file.filename) 

    #jsontmp = request.get_json(silent=True, cache=False, force=True)
    #print(request)

    if file and allowed_file(file.filename):
        #업로드 되는 파일명은 날짜+원래 파일명으로 처리함
        #filename = secure_filename(file.filename)
        filename = now.strftime('%Y%m%d%H%M%S%f_'+secure_filename(file.filename))   #한글.특수문자 제거함
        file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
        #return redirect(url_for('uploaded_file', filename=filename))
        
        return filename     #생성된 파일명 리턴
    return 'error'

#ocr 처리
@application.route('/runocr', methods=['POST'])
def runocr():
    try:
        #from runocr_tmp2 import main    #호출할 파이썬 파일 ( 동일경로에 있어야 함 )
        #jsontmp = request.get_json(silent=True, cache=False, force=True)    #json type으로 파라미터를 받음
        #print(jsontmp["filename"])  #파일명
        #main_return = main(jsontmp) #파이썬 호출시 파라미터는 dict type으로 전송
        #return_data = main_return["key1"] + "/" + main_return["key2"]
        #print(return_data) 
        from OCR_Service_test import ufn_detect_text    #호출할 파이썬 파일 ( 동일경로에 있어야 함 )
        jsontmp = request.get_json(silent=True, cache=False, force=True)    #json type으로 파라미터를 받음
        file_path = os.path.join(application.config['UPLOAD_FOLDER']) + '/' + jsontmp["filename"] #서버에 올려놓은 파일명
        apitype = jsontmp["apitype"]    #ocr type ( google / ms )

        if apitype == "google":
            print('run google ocr:'+file_path)
            return_data = ufn_detect_text(file_path)
            #os.remove(file_path)    #처리후에는 파일삭제
        else:
            return_data = ''

    except Exception as msg:
        errmsg = 'runocr Exception:'+str(msg)
        print(errmsg)
        return errmsg
    else:
        return return_data
# TEST -----------------------------------------------------------
@application.route('/dirname', methods=['POST'])
def dirname(): 
    print(os.getcwd())
    return os.getcwd() # 'upload ok'

@application.route('/checkdir', methods=['POST'])
def checkdir(): 
    if not os.path.isdir(application.config['UPLOAD_FOLDER']):
        os.mkdir(application.config['UPLOAD_FOLDER'])
    return 'ok'

    
@application.route('/koreancheck', methods=['POST'])
def koreancheck(): 
    print('---1----------------------')
    jsontmp = request.get_json(silent=True, cache=False, force=True)    #json type으로 파라미터를 받음
    print('---2----------------------')
    hangul = jsontmp["key1"] #서버에 올려놓은 파일명
    print(hangul)
    print(hangul.encode("utf-8"))
    print('---3----------------------') 
    hangul = secure_filename(hangul)
    print('---5----------------------')
    print(hangul)
    print("한글")
    print(u"한글")
    print('---6----------------------')

    return hangul
# TEST END -----------------------------------------------------------


if __name__ == '__main__':
    #서버 실행
#   app.run(debug = True)
   application.run()
