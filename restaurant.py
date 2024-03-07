class Table:
    def __init__(self, num_diners):
        self.bill = []
        self.num_diners = num_diners

    def order(self, item, price, quantity=1):
        self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item, price, quantity):
        for order in self.bill:
            if order['item'] == item and order['price'] == price:
                if order['quantity'] >= quantity:
                    order['quantity'] -= quantity
                    if order['quantity'] == 0:
                        self.bill.remove(order)
                    return True
                else:
                    return False
        return False

    def get_subtotal(self):
        subtotal = 0
        for order in self.bill:
            item_sum = order['price'] * order['quantity']
            subtotal += item_sum
        return subtotal

    def get_total(self, service_charge_percentage=0.10):
        subtotal = self.get_subtotal()
        service_charge = subtotal * service_charge_percentage
        total = subtotal + service_charge
        subtotal_str = f"£{subtotal:.2f}"
        service_charge_str = f"£{service_charge:.2f}"
        total_str = f"£{total:.2f}"
        return {'Sub Total': subtotal_str, 'Service Charge': service_charge_str, 'Total': total_str}

    def split_bill(self):
        subtotal = self.get_subtotal()
        num_diners = self.num_diners
        return round(subtotal / num_diners, 2)
