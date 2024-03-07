

class Table:
    def __init__(self, num_diners):
        self.num_diners = num_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                order["quantity"] += quantity
                return
        self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                if order["quantity"] >= quantity:
                    order["quantity"] -= quantity
                    if order["quantity"] == 0:
                        self.bill.remove(order)
                    return True  # Item successfully removed
                else:
                    return False  # Quantity desired for removal exceeds available quantity
        return False  # Item with corresponding name and price not found in bill

    def get_subtotal(self):
        subtotal = sum(item["price"] * item["quantity"] for item in self.bill)
        return subtotal

    def get_total(self, service_charge_percentage=0.10):
        subtotal = self.get_subtotal()
        service_charge = subtotal * service_charge_percentage
        total = subtotal + service_charge
        return {
            "Sub Total": "£{:.2f}".format(subtotal),
            "Service Charge": "£{:.2f}".format(service_charge),
            "Total": "£{:.2f}".format(total)
        }

    def split_bill(self):
        subtotal = self.get_subtotal()
        return round(subtotal / self.num_diners, 2)

```

