import datetime as dt
import math

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.total = 0

    def add_record(self, recording):
        self.records.append(self.recording)

    def get_today_stats(self):
        properdatenow = dt.datetime.now().date()
        if recording.date == properdatenow:
            self.total += recording.amount
        return self.total

    def get_today_remainder(self):
        return self.limit - self.total

    def get_week_stats(self):
        properdatenow = dt.datetime.now().date()
        weekstart = properdatenow - dt.timedelta(days=7)
        return sum(
            record.amount
            for record in self.records
            if weekstart < record.date <= properdatenow
        )


class CashCalculator(Calculator):
    USD_RATE = 74.86
    EURO_RATE = 89.08
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        cash_remained = get_today_remainder()
        result = 'Денег нет, держись'

        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),
        }

        if currency not in currencies:
            raise ValueError

        currency_name, currency_rate = currencies[currency]

        pre_result = round(abs(cash_remained) / currency_rate, 2)

        if cash_remained > 0:
            result = f'На сегодня осталось {pre_result} {currency_name}'
        elif cash_remained < 0:
            result += f': твой долг - {pre_result} {currency_name}'
        
        return result



class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remainder = self.get_today_remainder()
        if remainder > 0:
            return f'Сегодня можно съесть что-нибудь ещё, \
            но с общей калорийностью не более {remainder} кКал'
        else:
            return f'Хватит есть!'

    

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        now = dt.datetime.now()
        nowstring = f'{now.day}.{now.month}.{now.year}'
        if self.date is None:
            self.date = dt.datetime.strptime(nowstring, '%d.%m.%Y').date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
