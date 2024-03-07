class Table:
    def __init__(self, num_of_diners: int):
        self.num_of_diners = num_of_diners
        self.bill = list()

    # def order(self, item: str, price: float, quantity=1):
    #     for i in self.bill:
    #         if item in i["item"] and price in i["price"]:
    #             i["quantity"] += 1
    #         else:
    #             self.bill.append({"item": item, "price": price, "quantity": quantity})

    def order(self, item: str, price: float, quantity=1):
        for i in self.bill:
            if item == i["item"] and price == i["price"]:
                i["quantity"] += quantity
                break
        else:
            # If the item doesn't exist, add a new entry
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item: str, price: float, quantity: int):
        for i in self.bill:
            if item == i["item"] and price == i["price"] and i["quantity"] > quantity:
                i["quantity"] -= quantity
                return True
            elif item == i["item"] and price == i["price"] and i["quantity"] == quantity:
                self.bill.pop(self.bill.index(i))
            else:
                return False

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += i["price"] * i["quantity"]
        return round(subtotal, 2)

    def get_total(self, tip_percentage=0.1):
        sub_total = self.get_subtotal()
        service_charge = sub_total * tip_percentage
        total = sub_total + service_charge
        return {"Sub Total": "£" + "%.2f" % sub_total, "Service Charge": "£" + str(service_charge),
                "Total": "£" + str(total)}

    def split_bill(self):
        return round(self.get_subtotal() / self.num_of_diners, 2)
