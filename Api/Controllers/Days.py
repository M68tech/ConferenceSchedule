app = Flask(__name__)

@app.route('/day/<id>', methods=['GET'])
def get_one_day(id):
    return jsonify({'results' : "0000000"})

@app.route('/day/calendar_day', methods=['GET'])
def get_all_day(day=""):
   day = request.args.get('day', day)
   #if session null
#insert more code here for returning results based on the query so that all rooms are not shown when only 1 is requested.
   return jsonify({'results' : "Monday!!!"})

@app.route('/day/display_text', methods=['GET'])
def get_all_day(day=""):
   day = request.args.get('day', day)
   #if session null
#insert more code here for returning results based on the query so that all rooms are not shown when only 1 is requested.
   return jsonify({'results' : "BURGER!!!"})

if __name__ == '__main__':
    app.run(debug=True)