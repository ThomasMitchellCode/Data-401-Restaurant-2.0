class Table:
    def __init__(self, num_of_diners: int):
        self.num_of_diners = num_of_diners
        self.bill = list()

    def order (self, item: str, price: float, quantity=1):
        for i in self.bill:
            if item in i["item"] and price in i["price"]:
                i["quantity"] += 1
            else:
                self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove (self, item: str, price:int):
        for i in self.bill:
            if item in i["item"] and price in i["price"]:
                self.bill.pop(self.bill.index(i))
                return True
        else:
            return False

    def get_subtotal (self):
        subtotal = 0
        for i in self.bill:
            subtotal += i["price"] * i["quantity"]
        return subtotal

    def get_total(self, tip_percentage=0.1):
        sub_total = self.get_subtotal()
        service_charge = sub_total*tip_percentage
        total = sub_total + service_charge
        return {"Sub Total": sub_total, "Service Charge": service_charge, "Total": total}

    def split_bill(self):
        return round(self.get_subtotal() / self.num_of_diners, 2)



