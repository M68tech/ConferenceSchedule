from flask import Flask, Blueprint
# from flask import jsonify, request
import json
from Api.BusinessLogic import vendor as vendorBL


# app_vendor = Flask(__name__)
app_vendor = Blueprint('app_vendor', __name__)


@app_vendor.route('/vendor/<id>', methods=['GET'])
def get_by_id(id):
    vendor = vendorBL.get_by_id(id)
    return json.dumps(vendor.serialize())


@app_vendor.route('/vendor', methods=['GET'])
@app_vendor.route('/vendor/', methods=['GET'])
@app_vendor.route('/vendors', methods=['GET'])
def get_all():
    vendors = vendorBL.get_all()
    vendors_serialized = []
    for vendor in vendors:
        vendors_serialized.append(vendor.serialize())
    return json.dumps(vendors_serialized)


# if __name__ == '__main__' or __name__ == '__Vendor__':
#     app_vendor.run(debug=True)
