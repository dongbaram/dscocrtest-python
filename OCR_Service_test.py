import io,os

#credential_path = "D:/Python\MS OCR/My Project 65933-d15c1d73ef84.json"
credential_path = "./uploads/My Project 65933-d15c1d73ef84.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

#img_path="D:/Python/test.jpg"
img_path=""
#img_path=os.path.join('D:', os.sep, 'work', '_유지보수', 'B_외주OCR', '_문서 샘플', '계약이행보증_샘플', '_샘플2차', '서울보증보험', 'test.jpg')

# [START vision_text_detection]
def ufn_detect_text(p_path):
    try:
        """Detects text in the file."""
        # Imports the Google Cloud client library
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()

        # [START vision_python_migration_text_detection]
        with io.open(p_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        image_context = vision.types.ImageContext(language_hints=['ko'])

        response = client.text_detection(image=image,
                                         image_context=image_context)

        texts = response.text_annotations
        text_result = texts[0].description
        print('type : ', type(text_result))
        print(text_result)

        """
        texts = response.text_annotations
        print('Texts:')
    
        for text in texts:
            print('\n"{}"'.format(text.description))
    
           # vertices = (['({},{})'.format(vertex.x, vertex.y)
           #             for vertex in text.bounding_poly.vertices])
    
            #print('bounds: {}'.format(','.join(vertices)))
        """
    except Exception as msg:
        errmsg = 'runocr Exception:'+str(msg)
        print(errmsg)
        return errmsg
    else:
        return text_result
    # [END vision_python_migration_text_detection]
# [END vision_text_detection]
# END def ufn_detect_text(p_path):
if __name__ == "__main__":
    ufn_detect_text(img_path)
