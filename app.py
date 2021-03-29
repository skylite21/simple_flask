from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # a flask most egy egyszerű string-et ad vissza:
    return 'hello from flask'


# ha a futtatott file, az éppen ez a file akkor induljon el
# az alkalmazás dev mode-ban, az 5000-es porton
if __name__ == '__main__':
    app.debug = True
    # akkor elindul a flask
    app.run(host='0.0.0.0', port=5000)
