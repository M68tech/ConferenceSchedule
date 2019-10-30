from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/room/<id>', methods=['GET'])
def get_one_room(id):
    return jsonify({'results' : "output 123"})

@app.route('/room', methods=['GET'])
def get_all_room(room=""):
   room = request.args.get('room', room)
   #if room null
#insert more code here for returning results based on the query so that all rooms are not shown when only 1 is requested.
   return jsonify({'results' : "Wow we did it"})

if __name__ == '__main__':
    app.run(debug=True)