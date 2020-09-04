import datetime as dt
import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

now = dt.datetime.now()
properdatenow = now.date()
nowstring = f'{now.day}.{now.month}.{now.year}'


records = []

class Calculator:
    def __init__(self, limit):
        self.limit = limit

    def add_record(self, recording):
        records.append(recording)

    total = 0
    for record in records:
        if record.date == properdatenow:
             total += record.amount

    def get_today_stats(self):
        return self.total

    def get_week_stats(self):
        week = range((properdatenow - dt.timedelta(days=7)), (properdatenow + dt.timedelta(days=1)))
        weektotal = 0
        for record in records:
            if record.date in week:
                weektotal += record.amount
        return weektotal


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        self.currency = currency
        RUB_RATE = float(1)
        USD_RATE = float(70)
        EUR_RATE = float(80)
        remainder = float(self.limit - self.total)
        if remainder > 0:
            if currency == 'rub':
                value = truncate(remainder / RUB_RATE, 2)
                return f'На сегодня осталось {value} руб'
            elif currency == 'usd':
                value = truncate(remainder / USD_RATE, 2)
                return f'На сегодня осталось {value} USD'
            elif currency == 'eur':
                value = truncate(remainder / EUR_RATE, 2)
                return f'На сегодня осталось {value} Euro'

        if remainder == 0:
            return f'Денег нет, держись'

        if remainder < 0:
            if currency == 'rub':
                value = truncate(abs(remainder) / RUB_RATE, 2)
                return f'Денег нет, держись: твой долг - {value} руб'
            elif currency == 'usd':
                value = truncate(abs(remainder) / USD_RATE, 2)
                return f'Денег нет, держись: твой долг - {value} USD'
            elif currency == 'eur':
                value = truncate(abs(remainder) / EUR_RATE, 2)
                return f'Денег нет, держись: твой долг - {value} Euro'


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        remainder = float(self.limit - self.total)
        if remainder > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remainder} кКал'
        else:
            return f'Хватит есть!'

    

class Record:
    def __init__(self, amount, comment, date=nowstring):
        self.amount = amount
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment
    def __str__(self):
        return str(self.amount) + self.comment + str(self.date)


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("eur"))
print(*records)
print(properdatenow)
