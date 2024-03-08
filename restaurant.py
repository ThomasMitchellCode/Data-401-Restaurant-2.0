class Table:

    def __init__(self, diners:int):
        self.diners = diners
        self.bill = []


    def order(self, item, price, quantity: int = 1):
        item_present = False
        for each_item in self.bill:
            if each_item["item"] == item and each_item["price"] == price:
                each_item["quantity"] += quantity
                item_present = True
                break
        if item_present == False:
            menu_item = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(menu_item)

    def remove(self, item, price, quantity: int = 1):
        item_removal = False
        for each_item in self.bill:
            if each_item["item"] == item and each_item["price"] == price and each_item["quantity"] >= quantity:
                item_removal = True
                if each_item["quantity"] == quantity:
                    self.bill.remove(each_item)
                else:
                    each_item["quantity"] -= quantity
                break
        return item_removal

    def get_subtotal(self):
        total_cost = 0
        for each_item in self.bill:
            total_cost += each_item["price"] * each_item["quantity"]
        return total_cost

    def get_total(self, service_charge: float = 0.10):
        total_cost = self.get_subtotal()
        total_bill = {}
        total_bill["Sub Total"] = "£" + '{0:.2f}'.format(total_cost)
        service_charge_amount = total_cost * service_charge
        total_bill["Service Charge"] = "£" + str(round(service_charge_amount,2))
        total_bill_amount = total_cost + service_charge_amount
        total_bill["Total"] = "£" + '{0:.2f}'.format(total_bill_amount)
        return total_bill

    def split_bill(self):
        sub_total = self.get_subtotal()
        bill_per_person = round((sub_total/self.diners),2)
        return bill_per_person









