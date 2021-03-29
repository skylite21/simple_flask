from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # get_data()
    # a flask alapértelmezetten a templates mappában keresi a html
    return 'hello from flask!'


# ha a futtatott file, az éppen ez a file
if __name__ == '__main__':
    app.debug = True
    # akkor elindul a flask
    app.run(host='0.0.0.0', port=5000)
