# Cинглтон
class CarShop:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CarShop, cls).__new__(cls)
            cls._instance.cars = []
            cls._instance.observers = []
        return cls._instance

    def add_car(self, car):
        self.cars.append(car)
        for observer in self.observers:
            observer.notify(f"{car} есть в наличии.")

    def list_cars(self):
        return self.cars

    def add_observer(self, observer):
        self.observers.append(observer)

# Фактори
class CarFactory:
    @staticmethod
    def create_car(make, model, price):
        return Car(make, model, price)

# Декоратор 
class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.make} {self.model}: ${self.price}"
       
# Адаптер
class ManufacturerCar:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

class ManufacturerCarAdapter(Car):
    def __init__(self, manufacturer_car):
        super().__init__(manufacturer_car.make, manufacturer_car.model, manufacturer_car.price)

# Стратегия 
class PaymentStrategy:
    def pay(self, amount):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"${amount} наличными."

class LoanPayment(PaymentStrategy):
    def pay(self, amount):
        return f"${amount} в рассрочку."

# Наблюдатель
class ShopObserver:
    def notify(self, message):
        pass

class Customer(ShopObserver):
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"{self.name} получил обновление: {message}")

    def buy_car(self, car, payment_strategy):
        payment_details = payment_strategy.pay(car.price)
        print(f"{self.name} купил {car} используя {payment_details}")

# Вывод

if __name__ == "__main__":
    car_shop = CarShop()

    car1 = CarFactory.create_car("Toyota", "Camry", 50000)
    car2 = CarFactory.create_car("Lada", "Priora",  20000)
    
    car_shop.add_car(car1)
    car_shop.add_car(car2)

    manufacturer_car = ManufacturerCar("Lada", "2114", 10000)
    manufacturer_car_adapter = ManufacturerCarAdapter(manufacturer_car)
    car_shop.add_car(manufacturer_car_adapter)

    cash_payment = CashPayment()
    loan_payment = LoanPayment()

    customer1 = Customer("Dauren")
    customer2 = Customer("Alen")

    car_shop.add_observer(customer1)
    car_shop.add_observer(customer2)

    for car in car_shop.list_cars():
        for observer in car_shop.observers:
            observer.notify(f"{car} есть в наличии.")

    customer1.buy_car(car1, cash_payment)
    customer2.buy_car(car2, loan_payment)

