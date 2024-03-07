class Table:
    bill = []

    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    # new_table = Table(3)
    # print(new_table.diners)

    def order(self, item, price, quantity=1):
        # if not quantity:
        #     quantity = 1
        order_item = {"item": item, "price": price, "quantity": quantity}
        # order_item = {}
        # order_item["item"] = item
        # order_item["price"] = price
        # order_item["quantity"] = quantity
        self.bill.append(order_item)

    def order_no_quantity(self, item, price):
        order_item = {"item": item, "price": price, "quantity": 1}
        self.bill.append(order_item)

    def remove(self, item, price, quantity):
        for i in self.bill:
            if i["item"] == item and i["price"] == price:
                i["quantity"] -= quantity

    def get_subtotal(self):
        subtotal_amount = 0
        for i in self.bill:
            subtotal_amount += i["price"] * i["quantity"]
        return subtotal_amount
