class Table:
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
