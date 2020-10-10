import datetime as dt
import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

now = dt.datetime.now()
properdatenow = now.date()
nowstring = f'{now.day}.{now.month}.{now.year}'



class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.total = 0

    def add_record(self, recording):
        global properdatenow
        self.recording = recording
        self.records.append(recording)
        if recording.date == properdatenow:
            self.total += recording.amount

    def today_remainder(self):
        return self.limit - self.total

    def get_today_stats(self):
        return self.total

    def get_week_stats(self):
        global properdatenow
        weekstart = properdatenow - dt.timedelta(days=7)
        return sum([
            record.amount
            for record in self.records
            if weekstart < record.date <= properdatenow
        ])


class CashCalculator(Calculator):
    USD_RATE = 74.86
    EURO_RATE = 89.08
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        cash_remained = self.limit - self.get_today_stats()
        result = 'Денег нет, держись'

        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),
        }

        if currency not in currencies:
            raise ValueError

        currency_name, currency_rate = currencies[currency]

        if currency_rate == 1:
            result_cache = abs(cash_remained)
        else:
            result_cache = round(abs(cash_remained) / currency_rate, 2)

        if cash_remained > 0:
            result = f'На сегодня осталось {result_cache} {currency_name}'
        elif cash_remained < 0:
            result += f': твой долг - {result_cache} {currency_name}'

        return result



class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        remainder = self.today_remainder()
        if self.today_remainder() > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remainder} кКал'
        else:
            return f'Хватит есть!'

    

class Record:
    def __init__(self, amount, comment, date=nowstring):
        self.amount = amount
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment