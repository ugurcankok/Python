import datetime


# parent class
class VehicleRent:

    def __init__(self, stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        print(f"{self.stock} vehicle available to rent")
        return self.stock

    def rentHourly(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry, {self.stock} vehicle available to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print(f"Rented a {n} vehicle for hourly at {self.now.hour} hours")
            self.stock -= n
            return self.now

    def rentDaily(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry, {self.stock} vehicle available to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print(f"Rented a {n} vehicle for daily at {self.now.hour} hours")
            self.stock -= n
            return self.now

    def returnVehicle(self, request, brand):
        car_h_price = 10
        car_d_price = car_h_price * 8 / 10 * 24
        bike_h_price = 5
        bike_d_price = bike_h_price * 7 / 10 * 24

        rentalTime, rentalBasis, numberOfVehicle = request, request, request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now().hour
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.second / 3600 * car_h_price * numberOfVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.second / (3600 * 24) * car_d_price * numberOfVehicle
                if (2 <= numberOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill * (0.8)

                print("Thank you for returning your car")
                print(f"Price: ${bill}")
                return bill

        elif brand == "bike":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now().hour
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.second / 3600 * bike_h_price * numberOfVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.second / (3600 * 24) * bike_d_price * numberOfVehicle
                if (2 <= numberOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill * 0.8

                print("Thank you for returning your bike")
                print(f"Price: ${bill}")
                return bill

        else:
            print("You do not rent a vehicle")
            return None


# child class 1
class CarRent(VehicleRent):
    global discount_rate
    discount_rate = 15

    def __init__(self, stock):
        super().__init__(stock)

    def discount(self, b):
        bill = b - (b * discount_rate) / 100
        return bill


# child class 2
class BikeRent(VehicleRent):

    def __init__(self, stock):
        super().__init__(stock)


# customer class
class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")
            try:
                bikes = int(bikes)
            except ValueError:
                print("You should enter a number")
                return -1
            if bikes < 1:
                print("Number of Bikes should be greater than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("How many cars would you like to rent?")

            try:
                cars = int(cars)
            except ValueError:
                print("You should enter a number")
                return -1
            if cars < 1:
                print("Number of Bikes should be greater than zero")
                return -1
            else:
                self.cars = cars
            return self.cars
        else:
            print("Request vehicle error")

    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b and self.rentalBasis_b and self.bikes
            else:
                return 0, 0, 0
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c and self.rentalBasis_c and self.cars
            else:
                return 0, 0, 0
        else:
            print("Return vehicle error")
