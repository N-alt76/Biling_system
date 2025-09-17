# billing_system.py

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def get_total_due(self):
        return sum(service.price for service in self.services)

    def generate_invoice(self):
        invoice = f"Invoice for {self.name} (ID: {self.customer_id})\n"
        invoice += "-" * 30 + "\n"
        for service in self.services:
            invoice += f"{service.name}: ${service.price:.2f}\n"
        invoice += "-" * 30 + "\n"
        invoice += f"Total Due: ${self.get_total_due():.2f}\n"
        return invoice


class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def main():
    # Create customers
    customer1 = Customer(1, "Alice")
    customer2 = Customer(2, "Bob")

    # Create services
    internet = Service("Internet", 50.0)
    phone = Service("Phone", 30.0)
    tv = Service("TV", 20.0)

    # Add services to customers
    customer1.add_service(internet)
    customer1.add_service(phone)

    customer2.add_service(internet)
    customer2.add_service(tv)

    # Generate invoices
    print(customer1.generate_invoice())
    print(customer2.generate_invoice())


if __name__ == "__main__":
    main()
