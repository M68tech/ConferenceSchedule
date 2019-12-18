from flask import Flask, Blueprint
# from flask import jsonify, request
import json
from Api.BusinessLogic import vendor as vendorBL


# app_vendor = Flask(__name__)
app_event = Blueprint('app_event', __name__)


@app_event.route('/event/<id>', methods=['GET'])
def get_by_id(id):
    # vendor = vendorBL.get_by_id(id)
    # return json.dumps(vendor.serialize())
    return json.dumps("'test': 'event.get_by_id'")


@app_event.route('/event', methods=['GET'])
@app_event.route('/event/', methods=['GET'])
@app_event.route('/events', methods=['GET'])
def get_all():
    # vendors = vendorBL.get_all()
    # vendors_serialized = []
    # for vendor in vendors:
    #     vendors_serialized.append(vendor.serialize())
    # return json.dumps(vendors_serialized)
    return json.dumps("'test': 'event.get_all'")


# if __name__ == '__main__' or __name__ == '__Vendor__':
#     app_vendor.run(debug=True)
