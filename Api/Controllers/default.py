from flask import Flask, Blueprint

# app_default = flask.Flask(__name__)
app_default = Blueprint('app_default', __name__)


@app_default.route('/')
def app_root():
    return "replace with html for app root"


# if __name__ == '__main__' or __name__ == '__default__':
#     app_default.run(debug=True)
