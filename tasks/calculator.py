
import datetime as dt

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().strftime('%d.%m.%Y')
        else:
            self.date = date

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self,record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now().strftime('%d.%m.%Y')
        today_spent = sum(record.amount for record in self.records if record.date == today)
        return today_spent

    def get_week_stats(self):
        today = dt.datetime.now()
        start_of_week = today - dt.timedelta(days=today.weekday())
        end_of_week = start_of_week + dt.timedelta(days=6)
        week_spent = sum(record.amount for record in self.records if start_of_week <= dt.datetime.strptime(record.date, '%d.%m.%Y') <= end_of_week.strftime('%d.%m.%Y'))
        return week_spent

class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        USD_RATE = 80
        EURO_RATE = 100
        spent_today = sum(record.amount * (USD_RATE if currency == "usd" else EURO_RATE if currency == "euro" else 1) for record in self.records)
        if spent_today < self.limit:
            return f"На сегодня осталось {self.limit-spent_today} руб/USD/Euro"
        if spent_today == self.limit:
            return f"Денег нет, держись"
        if spent_today > self.limit:
            return f"Денег нет, держись: твой долг - {abs(self.limit-spent_today)} руб/USD/Euro"

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        eaten_today = sum(record.amount for record in self.records)
        if  eaten_today < self.limit:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit-eaten_today} кКал"
        else:
            return f"Хватит есть!"

