import string
import random

class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, electric, catalogue_price) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    # Improving cohesion
    def calculate_tax(self):
        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Catalogue Price: {self.catalogue_price}")
        print(f"Payable tax: {self.calculate_tax()}")

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()

class VehicleRegistry:

    vehicle_info = {}

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def __init__(self) -> None:
        self.add_vehicle_info( "Tesla Model 3", True, 60000)
        self.add_vehicle_info( "Volkswagen ID3", True, 35000)
        self.add_vehicle_info( "BMW 5", False, 45000)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])

class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # generate a vehicle
        return registry.create_vehicle(brand)
        


app = Application()
vehicle = app.register_vehicle("Volkswagen ID3")
# print out the vehicle registration information
vehicle.print()
print("********")
vehicle2 = app.register_vehicle("BMW 5")
# print out the vehicle registration information
vehicle2.print()
print("********")
vehicle3 = app.register_vehicle("Tesla Model 3")
# print out the vehicle registration information
vehicle3.print()