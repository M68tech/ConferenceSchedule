app = Flask(__name__)

# @app.route('/day/<id>', methods=['GET'])                 #the app.route things tell flask framework where to direct http
# def get_one_day(id):                                          #request or url
#     return jsonify({'results' : "0000000"})                     # call id and pass down to the  business logic and
#                                                                    # business logic will call repository and pass the id in
                                                                        #repository will data from database
                                                                           #ie - from business logic import 'class object'
                                                                            # or method
# @app.route('/day/calendar_day', methods=['GET'])
# def get_all_day(day=""):
#    day = request.args.get('day', day)
#    if day isNull():
# insert more code here for returning results based on the query so that all rooms are not shown when only 1 is requested.
#    return jsonify({'results' : "Monday!!!"})
#
# @app.route('/day/display_text', methods=['GET'])
# def get_all_day(day=""):
#    day = request.args.get('day', day)
#    #if session null
# #insert more code here for returning results based on the query so that all rooms are not shown when only 1 is requested.
#    return jsonify({'results' : "BURGER!!!"})
#
# if __name__ == '__main__':
#     app.run(debug=True)
def getDay:

    day = requests.args.get('day', day)

    return newDay


class DaysController:

newDay:str
