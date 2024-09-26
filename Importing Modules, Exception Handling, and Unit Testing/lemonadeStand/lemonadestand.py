from menu_item import MenuItem
from sales_for_day import SalesForDay

class InvalidSalesItemEror(Exception):
    pass

class LemonadeStand:
    def __init__(self,name):
        self._name_of_stand = name
        self.__current_day = 0
        self._menu = {} # key :item name, value : MenuItem Object
        self._sales_record = []# list of sales per day objects.

    def get_name(self):
        return self._name
    
    def add_menu_item (self, MenuItem_object):
        item_name = MenuItem_object.get_name()
        self._menu_items = item_name, MenuItem_object

    def enter_sales_for_today(self,items_sold_dictionary):
         # day_0_sales = {day_0_sales = { 'lemonade' : 5,'cookie'   : 2}
        for k in items_sold_dictionary.keys():
            if k not in self._menu_items:
                raise InvalidSalesItemEror (f"The item {k} was not on menu")
        new_sales_for_day_object = SalesForDay(self.__current_day, items_sold_dictionary)
        self._sales_record.append(new_sales_for_day_object)
        self.__current_day +=1

    def sales_of_menu_item_for_day(self, day, name_of_menu_item):
        for sales in self._sales_record:
            if day == sales.get_day()

        return 