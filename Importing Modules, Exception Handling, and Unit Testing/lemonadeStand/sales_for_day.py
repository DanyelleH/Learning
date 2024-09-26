class SalesForDay:
    def __init__(self, number_of_days, sales_dictionary): # dictionary Key = name, value = number sold
        self._number_of_days_open = number_of_days
        self._sales_dict = sales_dictionary # key: name of itemsold, value: items sold

    def get_day(self):
        return self._number_of_days_open
    def get_sales_dict(self):
        return self._sales_dict
