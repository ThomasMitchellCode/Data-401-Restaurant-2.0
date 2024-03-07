class Table:
    bill = []

    def __init__(self, num_diners):
        self.num_diners = num_diners
        self.bill = []

    def order(self, item, price, quantity=1):

        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                order["quantity"] += quantity
                break

        else:

            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                if order["quantity"] >= quantity:
                    order["quantity"] -= quantity
                    if order["quantity"] == 0:
                        self.bill.remove(order)
                    return True
                else:
                    return False
        return False

    def get_subtotal(self):

        subtotal = 0

        for order in self.bill:
            subtotal += order["price"] * order["quantity"]

        return subtotal
