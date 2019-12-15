from flask import Flask
from Api.Controllers import default, vendor, event


app = Flask(__name__)
app.register_blueprint(default.app_default)
app.register_blueprint(vendor.app_vendor)
app.register_blueprint(event.app_event)


if __name__ == '__main__':
    app.run(debug=True)
