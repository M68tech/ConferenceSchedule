from flask import abort
from flask import Flask
from flask import jsonify, request
from flask import make_response

from Api.Controllers.Days import newDay

app = Flask(__name__)


# @app.route('/day', methods=['GET'])
# def get_all_day(day=""):
#     day = request.args.get('day', day)
#     return jsonify({'results': "Wow we did it"})

#
# @app.route('/day/<int:day_id>', methods=['GET'])
# def get_day(day_id):
#     day = [day for day in days if day['id'] == day_id]
#     if len(day) == 0:
#         abort(404)
#     return jsonify({'day': day[0]})
#
#
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
from Models import Day

class DaysRepo:

    def __init__(self, day, id, display_text): #defining the properties
          self.day = day
          self.id = id
          self.display_text = display_text

    def GetDay(self,day:str) -> Day:

      CalendarDay = Day[
        Day(1,"04/05/2020","Friday"),
        Day(2, "04/06/2020", "Saturday")
         ]


      return Day(1,"04/05/2020","Friday")


    def GetDays(self, day: str) -> Day:

        return Day[
            Day(1, "04/05/2020", "Friday"),
            Day(2, "04/06/2020", "Saturday")
        ]


    #sqlData = sql.getDay(day)




    # requestedDay = Day(sqlData.id, sqlData.day, sqlData.display)
    #
    # return requestedDay
