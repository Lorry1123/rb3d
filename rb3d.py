from img_deal.__init__ import create_app
import sys

app = create_app('app', ['app'])
app.config['SECRET_KEY'] = '123456789'

reload(sys)
sys.setdefaultencoding("utf-8")


@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True, port=2333)
