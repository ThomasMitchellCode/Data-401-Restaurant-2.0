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

    def get_total(self, service_charge_rate):

        if service_charge_rate == '':
            service_charge_rate = 0.10
        else:
            service_charge_rate = float(service_charge_rate)

        subtotal = self.get_subtotal()
        service_charge = subtotal * service_charge_rate
        total = subtotal + service_charge

        subtotal_str = f'£{subtotal:.2f}'
        service_charge_str = f'£{service_charge:.2f}'
        total_str = f'£{total:.2f}'

        final_message = {"Sub Total": subtotal_str, "Service Charge": service_charge_str, "Total": total_str}

        return final_message

    def split_bill(self):

        subtotal = self.get_subtotal()
        split_cost = (subtotal / self.num_diners)

        return split_cost


