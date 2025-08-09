from datetime import timedelta

# Truck Object Creation
class Truck:
    def __init__(self, packages, departure_time, speed, mileage, currentLocation):
        self.packages = packages
        self.departure_time = departure_time
        self.time = departure_time
        self.speed = speed
        self.mileage = mileage
        self.currentLocation = currentLocation

    def __str__(self):
        return f"Packages: {self.packages}, Depart Time: {self.departure_time}, Speed: {self.speed}, Mileage: {self.mileage}, Current Location: {self.currentLocation}, Current Time: {self.time}"

