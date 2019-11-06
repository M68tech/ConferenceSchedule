from flask import abort
from flask import Flask
from flask import jsonify, request
from flask import make_response

app = Flask(__name__)

rooms = [
    {
        'id': 1,
        'title': u'Grand Ballroom',
        'capacity': u'180',
        'description': u'Main floor ballroom, seats 180',
        'done': False
    },
    {
        'id': 2,
        'title': u'Side Room A',
        'capacity': u'30',
        'description': u'Off north side seats 30',
        'done': False
    }
]

@app.route('/room', methods=['GET'])
def get_all_room(room=""):
   room = request.args.get('room', room)
   return jsonify({'results' : "Wow we did it"})

@app.route('/room/<int:room_id>', methods=['GET'])
def get_room(room_id):
    room = [room for room in rooms if room['id'] == room_id]
    if len(room) == 0:
        abort(404)
    return jsonify({'room' : room[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)  
  
if __name__ == '__main__':
    app.run(debug=True)