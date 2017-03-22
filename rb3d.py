from img_deal.__init__ import create_app

app = create_app()


@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True, port=2333)
