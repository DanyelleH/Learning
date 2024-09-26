class MenuItem:
    def __init__(self,name,wholesale_cost,selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price
    
    def get_name(self):
        return self._name
    def get_wholesale_cost(self):
       return self._wholesale_cost
    def get_selling_price(self):
       return self._selling_price
        

class SalaesForDay:
    def __init__(self, number_of_days, sales_dictionary): # dictionary Key = name, value = number sold
        self._number_of_days = number_of_days
        self._sales_dictionaty = sales_dictionary # key: name of itemsold, value: items sold

    def get_day(self):
        return self._number_of_days
    def get_sales_dict(self):
        return self._sales_dictionaty

    
class InvalidSalesItemEror(Exception):
    pass

class LemonadeStand:
    def __init__(self,name):
        self._name = name
        self.__current_day = 0
        self._menu_items = {} # key :item name, value : MenuItem Object
        self._sales_record = []

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
        new_sales_for_day_object = SalaesForDay(self.__current_day, items_sold_dictionary)
        self._sales_record.append(new_sales_for_day_object)
        self.__current_day +=1

    def sales_of_menu_item_for_day(self, day, menu_item_name):
        if day is in 
        return 