class BurgerBillingSystem:
    def __init__(self):
        self.menu = {
            1: {'name': 'Aloo Tikki', 'price': 5},
            2: {'name': 'Maharaja', 'price': 10},
            3: {'name': 'Mac Special', 'price': 15}
        }
        self.orders = []
        self.final_total = 0

    def display_menu(self):
        print("\n********** Burger Menu **********")
        for sr, item in self.menu.items():
            print(f"{sr}. {item['name']} - {item['price']}$")
        print("*********************************")

    def take_order(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter the serial number of the burger you want to order: "))
                if choice not in self.menu:
                    print("Invalid choice. Please select again.")
                    continue
                
                quantity = int(input("How many quantities? "))
                if quantity < 1:
                    print("Quantity should be at least 1.")
                    continue

                self.orders.append({'item': self.menu[choice], 'quantity': quantity})
                
                more_orders = input("Do you want to order another burger? (yes/no): ").strip().lower()
                if more_orders != 'yes':
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def calculate_bill(self):
        if not self.orders:
            print("You haven't ordered anything yet!")
            return

        subtotal = sum(order['item']['price'] * order['quantity'] for order in self.orders)
        print(f"\nSubtotal: {subtotal}$")

        # Apply student discount if applicable
        student_discount = 0
        is_student = input("Are you a student? (yes/no): ").strip().lower()
        if is_student == 'yes':
            student_discount = subtotal * 0.2
            subtotal -= student_discount
            print(f"Student Discount (20%): -{student_discount}$")

        # Add delivery charge if required
        delivery_charge = 0
        delivery = input("Do you want delivery? (yes/no): ").strip().lower()
        if delivery == 'yes':
            delivery_charge = subtotal * 0.05
            subtotal += delivery_charge
            print(f"Delivery Charge (5%): +{delivery_charge}$")

        # Add tip if provided
        tip = 0
        tip_choice = input("Do you want to give a tip? (yes/no): ").strip().lower()
        if tip_choice == 'yes':
            while True:
                try:
                    tip = int(input("How much tip would you like to give? (2$, 5$, 10$): "))
                    if tip not in [2, 5, 10]:
                        print("Invalid tip amount. Please enter 2$, 5$, or 10$.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            subtotal += tip
            print(f"Tip: +{tip}$")

        self.final_total = subtotal
        print("\n****************** Final Bill ******************")
        print("Sr.\tName\t\tPrice\tQuantity\tTotal Price")
        for i, order in enumerate(self.orders, start=1):
            item = order['item']
            quantity = order['quantity']
            total_price = item['price'] * quantity
            print(f"{i}\t{item['name']}\t\t{item['price']}$\t{quantity}\t\t{total_price}$")
        print("------------------------------------------")
        print(f"Total Bill: {self.final_total}$")
        print("Thank you and come again >>>>>>>>>>>>>>>>>>>>>>>>>>")

if __name__ == "__main__":
    system = BurgerBillingSystem()
    system.take_order()
    system.calculate_bill()
