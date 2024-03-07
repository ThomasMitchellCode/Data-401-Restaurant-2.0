class Table:

    # bill = []  # instance variable called bill that is a list

    def __init__(self, people: int):
        self.people = people
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

    def get_subtotal(self):
        sub_total = 0
        for order in self.bill:
            sub_total += order["price"] * order["quantity"]
        return sub_total

    def get_total(self, service_percent=0.1):
        sub_total = self.get_subtotal()
        service_charge = sub_total * service_percent
        total = sub_total + service_charge
        return {"Sub Total": "£" + "%.2f" % sub_total,
                "Service Charge": "£" + str(service_charge),
                "Total": "£" + str(total)}

    def split_bill(self):
        return round(self.get_subtotal() / self.people, 2)
