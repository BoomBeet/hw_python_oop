    def __init__(self, limit):
        super().__init__(limit)
        self.RUB_RATE = 1.0
        self.USD_RATE = 80.0
        self.EURO_RATE = 90.0

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
                value = truncate(remainder / self.EURO_RATE, 2)
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
                value = truncate(abs(remainder) / self.EURO_RATE, 2)
                return f'Денег нет, держись: твой долг - {value} Euro'