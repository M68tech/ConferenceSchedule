import displayText as displayText

from Api import Repositories, Contracts
from Api.Models.Days import Day


class Day:

    def GetDay(self) -> Day:
        model_day = Repositories.DaysRepo.GetDay()

        contract_Day = Contracts.Day(model_day.calendarDay, model_day.displayText)

        return contract_Day

class Days:
    def GetDays(self, displayText=None) -> Day:

        model_days = Repositories.DaysRepo.GetDays()
        contract_days = []
        for one_Day in model_days:

            contract_days += [Contracts.Day(one_Day.calendarDay, one_Day.displayText)]

        return contract_days





        # contracstDays = Day.days
        #       for(day in days):
        #           ### basically create an array from days and then create another empty list and iterate values into the
        #           ###whatever is the difference between the model and contract days is.


        return contract_Days
