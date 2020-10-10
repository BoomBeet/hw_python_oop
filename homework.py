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
    def __init__(self, limit):
        super().__init__(limit)
        RUB_RATE = float(1)
        USD_RATE = float(80)
        EUR_RATE = float(90)

    def get_today_cash_remained(self, currency):
        self.currency = currency
        remainder = self.today_remainder()
        if remainder > 0:
            if currency == 'rub':
                value = truncate(remainder / self.RUB_RATE, 2)
                return f'На сегодня осталось {value} руб'
            elif currency == 'usd':
                value = truncate(remainder / self.USD_RATE, 2)
                return f'На сегодня осталось {value} USD'
            elif currency == 'eur':
                value = truncate(remainder / self.EUR_RATE, 2)
                return f'На сегодня осталось {value} Euro'
        elif remainder == 0:
            return f'Денег нет, держись'
        else:
            if currency == 'rub':
                value = truncate(abs(remainder) / self.RUB_RATE, 2)
                return f'Денег нет, держись: твой долг - {value} руб'
            elif currency == 'usd':
                value = truncate(abs(remainder) / self.USD_RATE, 2)
                return f'Денег нет, держись: твой долг - {value} USD'
            elif currency == 'eur':
                value = truncate(abs(remainder) / self.EUR_RATE, 2)
                return f'Денег нет, держись: твой долг - {value} Euro'


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