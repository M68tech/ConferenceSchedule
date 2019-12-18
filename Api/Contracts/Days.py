import json

class Day:
    def __init__(self, calendarDay, displayText):
                 self.calendarDay = calendarDay
                 self.displayText = displayText

    def serialize(self):
        return self.__dict__




