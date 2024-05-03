
import datetime as dt

""" create class record to store all records"""
class Record:
    """init it with 3 args, set date to none as it is optional"""
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        """ if no date, calculate today's date with dt and delete time to get the right format"""
        if date is None:
            self.date = dt.datetime.now().strftime('%d.%m.%Y')
        else:
            self.date = date

""" create class calculator to reuse for future calculators"""

class Calculator:
    """it takes one param - limit and creates an empty list for class Record objects"""
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    """add record takes a record as an input and appends it to the list records"""
    def add_record(self,record):
        self.records.append(record)
    def get_time_stats(self, start_date, end_date):
        time_spent = sum(record.amount for record in self.records if start_date <= dt.datetime.strptime(record.date, '%d.%m.%Y') <= end_date)
        return time_spent
    """all records with date matching today are summed in amount"""
    def get_today_stats(self):
        today = dt.datetime.now().strftime('%d.%m.%Y')
        today_spent = sum(record.amount for record in self.records if record.date == today)
        return today_spent
    """all records within one week are summed in amount, the first day of the week
    is calculated by extracting how many days passed since today from today and getting the date
    end of the week is calculated by adding 6 to monday
    the week should be in between the dates """
    def get_week_stats(self):
        today = dt.datetime.now()
        start_of_week = today - dt.timedelta(days=today.weekday())
        end_of_week = start_of_week + dt.timedelta(days=6)
        week_spent = self.get_time_stats(start_of_week, end_of_week)
        return week_spent


"""TODO вынести """

""" calculate money in 3 currencies"""
class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        USD_RATE = 80
        EURO_RATE = 100
        currency_symbol = {"rub": "руб", "usd": "USD", "euro": "Euro"}
        currency_str = currency_symbol.get(currency, "руб")
        spent_today = sum(record.amount * (USD_RATE if currency == "usd" else EURO_RATE if currency == "euro" else 1) for record in self.records)
        if spent_today < self.limit:
            return f"На сегодня осталось {self.limit-spent_today} руб/USD/Euro"
        if spent_today == self.limit:
            return f"Денег нет, держись"
        if spent_today > self.limit:
            return f"Денег нет, держись: твой долг - {abs(self.limit-spent_today)} {currency_str}"

""" calculate calories"""
class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    """ how many calories left """
    def get_calories_remained(self):
        if  self.get_today_stats() < self.limit:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit-self.get_today_stats()} кКал"
        return f"Хватит есть!"

