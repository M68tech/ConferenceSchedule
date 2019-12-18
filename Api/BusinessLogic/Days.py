from Api.Repositories.Days import DaysRepo
from Api.Contracts.Days import Day




def GetDay(self) -> Day:
     model_day = DaysRepo.GetDay()

     contract_Day = Day(model_day.calendarDay, model_day.displayText)

     return contract_Day


def GetDays(self, displayText=None):

    model_days = DaysRepo.GetDays()
    contract_days = []
    for one_Day in model_days:

             contract_days.append(Day(one_Day.calendarDay, one_Day.displayText))

    return contract_days




