from flask import Flask, Blueprint, Response, request
import Image
test = Blueprint('test', __name__)


@test.route('/hello')
def hello():
    return 'hello from img_api'


@test.route('/get_pic')
def get_pic():
    img = file('img_deal/img_api/img/img_test.jpg')
    resp = Response(img, mimetype="imgae/jpeg")

    return resp


@test.route('/upload_pic', methods=['post'])
def upload_pic():
    file_tmp = request.files['file']
    img = Image.open(file_tmp)
    img.show()
    print '===== img =====', img
    img.save('./img/upload_pic.png')

    output = open('img_deal/img_api/img/img_upload.jpg', 'w')
    output.write(file_tmp)
    output.close()

    return {'ok': 1}
