from menu_item import MenuItem
from sales_for_day import SalesForDay

class InvalidSalesItemError(Exception):
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
        self._menu[item_name] = MenuItem_object

    def enter_sales_for_today(self,items_sold_dictionary):
         # day_0_sales = {day_0_sales = { 'lemonade' : 5,'cookie'   : 2}
        for k in items_sold_dictionary.keys():
            if k not in self._menu:
                raise InvalidSalesItemError (f"The item {k} was not on menu")
        new_sales_for_day_object = SalesForDay(self.__current_day, items_sold_dictionary)
        self._sales_record.append(new_sales_for_day_object)
        self.__current_day +=1

    def sales_of_menu_item_for_day(self, day, name_of_menu_item):
        for sales in self._sales_record:
            if day == sales.get_day():
                sales_log = sales.get_sales_dict()
                return sales_log.get(name_of_menu_item,0) # get the menu item passed in from the sales log dictionary
                # if not found it will return "0"
                # if name_of_menu_item in sales_log:
                #     return sales_log[name_of_menu_item]
                # else:
                #     return 0
        return "No information found for that day"
    
    def total_sales_for_menu_item (self, name_of_menu_item):
        total_sale = 0
        for sale in self._sales_record:
            day = sale.get_day()
            sales_for_day = self.sales_of_menu_item_for_day(day,name_of_menu_item)
            total_sale += sales_for_day
        return total_sale
    
    def total_profit_for_menu_item(self,name_of_menu_item):
        total_sales = self.total_sales_for_menu_item(name_of_menu_item)
        menu_object = self._menu.get(name_of_menu_item)
        profit = menu_object.get_selling_price() - menu_object.get_wholesale_cost()
        return profit * total_sales
    
    def total_profit_for_stand(self):
        total_profit = 0
        for menu_item in self._menu.keys():
            total_profit += self.total_profit_for_menu_item(menu_item)
        return total_profit

def main():
    stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
    item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    item3 = MenuItem('cookie', 0.2, 1) # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'
    day_0_sales = {
    'lemonade' : 5,
    'cookie'   : 2
    }
    stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")
           # print the total profit for lemonade so far


if __name__ == "__main__":
    main()