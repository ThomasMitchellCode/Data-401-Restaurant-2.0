class Table:
    bill = []

    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

# new_table = Table(3)
# print(type(new_table))
# print(new_table.number_of_diners)

    def order(self, item, price, quantity=1):
        order_item = {}
        order_item["item"] = item
        order_item["price"] = price
        order_item["quantity"] = quantity
        self.bill.append(order_item)
