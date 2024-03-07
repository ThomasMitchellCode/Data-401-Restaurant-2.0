class Table:
    def __init__(self, num_diners):
        # Initialize an empty list to store orders
        self.bill = []
        # Store the number of diners
        self.num_diners = num_diners

    def order(self, item, price, quantity=1):
        # Add an order to the bill list
        self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item, price, quantity):
        # Iterate through the bill list to find and remove an order
        for order in self.bill:
            if order['item'] == item and order['price'] == price:
                if order['quantity'] >= quantity:
                    # If quantity to remove is less than or equal to the order quantity, update the order
                    order['quantity'] -= quantity
                    # If order quantity becomes 0, remove the order from the bill
                    if order['quantity'] == 0:
                        self.bill.remove(order)
                    return True
                else:
                    # If quantity to remove is greater than order quantity, return False
                    return False
        # If the item is not found in the bill, return False
        return False

    def get_subtotal(self):
        # Calculate subtotal of the bill
        subtotal = 0
        for order in self.bill:
            item_sum = order['price'] * order['quantity']
            subtotal += item_sum
        return subtotal

    def get_total(self, service_charge_percentage=0.10):
        # Calculate total bill including service charge
        subtotal = self.get_subtotal()
        service_charge = subtotal * service_charge_percentage
        total = subtotal + service_charge
        # Format amounts to strings with 2 decimal places
        subtotal_str = f"£{subtotal:.2f}"
        service_charge_str = f"£{service_charge:.2f}"
        total_str = f"£{total:.2f}"
        return {'Sub Total': subtotal_str, 'Service Charge': service_charge_str, 'Total': total_str}

    def split_bill(self):
        # Calculate amount each diner needs to pay
        subtotal = self.get_subtotal()
        num_diners = self.num_diners
        return round(subtotal / num_diners, 2)
