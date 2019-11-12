from flask import abort
from flask import Flask
from flask import jsonify, request
from flask import make_response

app = Flask(__name__)

Days = [
    {
        'id': 1,
        'day': u'Friday',
        'calendar_date': u'04/04/2020',
        'event_reference': u'Main floor ballroom, seats 180',

    },
    {
        'id': 2,
        'day': u'Saturday',
        'calendar_date': u'04/05/2020',
        'event_reference': u'Main floor ballroom, seats 180',

    }
]


@app.route('/day', methods=['GET'])
def get_all_day(day=""):
    day = request.args.get('day', day)
    return jsonify({'results': "Wow we did it"})


@app.route('/day/<int:day_id>', methods=['GET'])
def get_day(day_id):
    day = [day for day in days if day['id'] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({'day': day[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)