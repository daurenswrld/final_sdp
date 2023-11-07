# Car Shop Project

The Car Shop System is a Python project that demonstrates the application of various design patterns to create a simplified car shop environment. In this README, I will provide an overview of the project, its components, and how design patterns are used to improve its structure and functionality.

## Project Components

### Singleton (CarShop)
The `CarShop` class is implemented as a Singleton. It ensures that there is only one instance of the car shop in the application. The key functionalities of the `CarShop` class include:

- Adding cars to the shop and notifying observers when new cars are added.
- Listing the available cars.
- Adding observers (customers) who are interested in updates.

### Factory (CarFactory)
The `CarFactory` class acts as a factory for creating `Car` objects. It provides a convenient way to create car objects with specified make, model, and price.

### Decorator (Car)
The `Car` class represents a basic car with attributes such as make, model, and price. It is used as the base class for other car-related classes. The `__str__` method is overridden to format car information as a string.

### Adapter (ManufacturerCar and ManufacturerCarAdapter)
The `ManufacturerCar` class represents a car in a different format. The `ManufacturerCarAdapter` is used to adapt `ManufacturerCar` objects to the `Car` class interface, allowing them to be seamlessly integrated into the car shop system.

### Strategy (PaymentStrategy, CashPayment, and LoanPayment)
The Strategy pattern is applied for payment methods. The `PaymentStrategy` is an abstract base class with a `pay` method. Two concrete payment strategies are provided: `CashPayment` and `LoanPayment`. These strategies encapsulate different payment methods and allow for flexible payment options.

### Observer (ShopObserver and Customer)
The Observer pattern is used for notifying customers about the availability of cars in the car shop. Key components include:

- `ShopObserver`: An abstract base class for observers.
- `Customer`: A concrete observer representing a customer. Customers can receive notifications and make car purchases. The `buy_car` method demonstrates the integration of payment strategies.

## Running the Code

To run the code, execute the `if __name__ == "__main__":` block at the end of the script. This block creates instances of the various classes, adds cars to the shop, defines payment strategies, and demonstrates customer purchases with different payment options.

## Conclusion

This project illustrates the application of various design patterns to create a well-structured and extensible car shop system. It showcases the use of Singleton, Factory, Decorator, Adapter, Strategy, and Observer patterns to improve code organization and maintainability. These design patterns help in achieving a more modular and flexible design for the car shop application. 

## This is UML Diagram below, also you can open in source folder in .pyns format

<img width="738" alt="Снимок экрана 2023-11-08 в 01 57 58" src="https://github.com/daurenswrld/final_sdp/assets/68074702/457bf1fd-3380-46ac-a683-58e539ad7afa">
