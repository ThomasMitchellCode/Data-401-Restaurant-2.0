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

    # def remove(self, item, price, quantity):
    #     order_item = {"item": item, "price": price, "quantity": quantity}
    #     # remove_order_item = {"item": order_item["item"], "price": order_item["price"],
    #     #                      "quantity": order_item["quantity"] - quantity}
    #     # remove_order_item = {"item": item, "price": price, "quantity": quantity}
    #     # self.bill.append(remove_order_item)
    #     self.bill.append(order_item)
    #     # new_bill = self.bill[quantity] - order_item[quantity]

    def remove(self, item, price, quantity):
        for i in self.bill:
            if i["item"] == item and i["price"] == price:
                i["quantity"] -= quantity

    def get_subtotal(self, item, price, quantity):
        #     item_cost = 0
        #     for item in self.bill:
        #         item_cost += price * quantity
        # print(get_subtotal(Table, 'Food', 5, 2))
        # order_item = {"item": item, "price": price, "quantity": quantity}
        # self.bill.append(order_item)
        # item_cost = 0
        for i in self.bill:
            subtotal_amount = sum(i["price"] * i["quantity"])
            return subtotal_amount

    # def get_subtotal(self):
    #     return sum(i['price'] * i['quantity'] for i in self.bill)
