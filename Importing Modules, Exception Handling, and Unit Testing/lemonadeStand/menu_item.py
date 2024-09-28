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