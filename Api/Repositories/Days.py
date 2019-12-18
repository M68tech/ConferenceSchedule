from Api.Models.Days import Day

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


