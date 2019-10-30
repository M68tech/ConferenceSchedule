from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/session/<id>', methods=['GET'])
def get_one_session(id):
    return jsonify({'results' : "000000"})

@app.route('/session', methods=['GET'])
def get_all_sessions(session=""):
   session = request.args.get('session', session)
   #if session null
#insert more code here for returning results based on the query so that all rooms are not shown when only 1 is requested.
   return jsonify({'results' : "Let's get some burger!!!"})

if __name__ == '__main__':
    app.run(debug=True)