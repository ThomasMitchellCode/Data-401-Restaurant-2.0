class Table:

    # bill = []  # instance variable called bill that is a list

    def __init__(self, people):
        self.people = people,
        self.bill = []

    def order(self, item, price, quantity=1):
        order_item = {"item": item, "price": price, "quantity": quantity}
        self.bill.append(order_item)

        # for order in self.bill:
        #     if order_item["item"] == item and order_item["price"] == price:
        #         quantity += 1
        #     else:
        #         self.bill.append(order_item)

    def remove(self, item, price, quantity):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                order["quantity"] = quantity - 1

