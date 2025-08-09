import datetime


# Creates Package Object
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, departure_time, delivery_time, truck_id=None):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        # Used to display truck number
        self.truck_id = truck_id

        # Sets status for packages delivered at 9:05
        if self.package_id in [6, 25, 28, 32]:
            self.delayed_until = datetime.timedelta(hours=9, minutes=5)
        else:
            self.delayed_until = None

    def __str__(self):
        return f"ID: {self.package_id}, Address: {self.address},{self.city},{self.state},{self.zip_code}, Deadline: {self.deadline}, Weight: {self.weight} kg, Status: {self.status}, Departed at: {self.departure_time}, Delivered at: {self.delivery_time}, Truck #: {self.truck_id}"


    # Returns a string of package status
    def package_status(self, time):
        if self.delayed_until and time < self.delayed_until:
            self.status = "Delayed"
        elif self.delivery_time is None:
            self.status = "At the hub"
        elif time < self.departure_time:
            self.status = "At the hub"
        elif time < self.delivery_time:
            self.status = "En route"
        else:
            self.status = "Delivered!"

        # Resolves package 9 address discrepancy
        if self.package_id == 9:
            if time > datetime.timedelta (hours=10, minutes=20):
                self.address = "410 S State St"
                self.zip_code = "84111"
            else:
                self.address = "300 State St"
                self.zip_code = "84103"



