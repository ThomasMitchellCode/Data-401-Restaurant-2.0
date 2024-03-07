import math
class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bill = []

    def order(self, item, price, quantity=1):
        # look for the item in the bill
        for i in self.bill:
            if i['item'] == item and i['price'] == price:
                i['quantity'] += quantity
                return
        self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item, price, quantity):
        for i in self.bill:
            if i['item'] == item and i['price'] == price:
                if i['quantity'] > quantity:
                    i['quantity'] -= quantity
                else:
                    self.bill.remove(i)
                return
        return False
    def get_subtotal(self):
        return sum(i['price'] * i['quantity'] for i in self.bill)
    def get_total(self, rate =0.10):
        return  {'Service Charge': f'£{(self.get_subtotal() * rate):.2f}', 'Sub Total': f'£{self.get_subtotal():.2f}' , 'Total': f'£{(self.get_subtotal() * (1 + rate)):.2f}'}

    def split_bill(self):
        return math.ceil(float((f'{(self.get_subtotal() / self.capacity):.3f}')) *100)/100


