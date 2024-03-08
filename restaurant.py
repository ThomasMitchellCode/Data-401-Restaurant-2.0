class Table:
    pass

    # check to see if I can save this file on my branch
    # successful

    # constructor
    def __init__(self, number_of_diners):  # instantiated with the number of diners per table
        self.bill = []  # an instance variable (an empty list)

    def order(self, item, price,
              quantity=1):  # order is the method of the class, we will have more methods within the class

        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                quantity += order["quantity"]

        self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price):

        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                if order["item"] > item['quantity']:
                    quantity -= order["quantity"]
                    if order["quantity"] == 0:
                        self.bill.remove(order)
                    return True
                else:
                    return False
        return False

    def get_subtotal(self):
        return sum(order["price"] * order["quantity"] for order in self.bill)

    def get_total(self, service_charge = 0.1):
        subtotal = self.get_subtotal()
        service_charge = subtotal * service_charge_percentage
        total = subtotal + service_charge


        return {"Sub Total": subtotal_str, "Service Charge": service_charge_str, "Total": total_str}

    def split_bill():
        subtotal = self.get_subtotal()
        per_person_cost = math.ceil(subtotal / self.number_of_people * 100) / 100.0  # Round up to the nearest penny
        return per_person_cost

    #commit 2




