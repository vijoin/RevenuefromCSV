from datetime import timedelta, datetime


class BaseFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.values = self.process_file()

    def process_file(self):
        with open(self.file_path, 'r') as f:
            value_list = list()

            print()
            for i, value in enumerate(f.readlines()[1:], 0):
                date_delta = timedelta(days=i)
                date = datetime.today() - date_delta
                value_list.append((date, int(value.rstrip())))
        return value_list

class BasicCupcakes(BaseFile):

    def __init__(self, file_path, price):
        super().__init__(file_path)
        self.price = price
        self.year_total_amount = self.get_year_total()
        self.month_total_amount = self.get_month_total()
        self.week_total_amount = self.get_week_total()

    def get_year_total(self):
        total_year = 0
        for value in self.values:
            if value[0].year == datetime.now().year:
                total_year += value[1]
        return total_year

    def get_month_total(self):
        total_month = 0
        for value in self.values:
            if value[0].year == datetime.now().year and value[0].month == datetime.now().month:
                total_month += value[1]
        return total_month

    def get_week_total(self):
        total_week = 0
        for value in self.values:
            if value[0].year == datetime.now().year and value[0].isocalendar()[1] == datetime.now().isocalendar()[1]:
                total_week += value[1]
        return total_week
