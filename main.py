# Student ID: 011630470
import datetime
from datetime import timedelta
import csv

# Import files
from Package import Package
from Truck import Truck
from HashTable import HashTable

# Insert addresses and distance data from csv spreadsheets
with open("Data_Files/distance-matrix.csv") as distance, open("Data_Files/Addresses.csv") as address:
    distance_table = csv.reader(distance)
    distance_table = list(distance_table)
    address_table = csv.reader(address)
    address_table = list(address_table)

# Inserting package csv file into hashtable
def add_packages(file):
    with open(file) as packageList:
        packageFile = csv.reader(packageList, delimiter=',')

        for packageInfo in packageFile:
            ID = int(packageInfo[0])
            package_address = packageInfo[1]
            city = packageInfo[2]
            state = packageInfo[3]
            zip_code = packageInfo[4]
            deadline = packageInfo[5]
            weight = packageInfo[6]
            packageNote = packageInfo[7]
            status = 'At the Hub'
            departure_time = None
            delivery_time = None

            insert = Package(ID, package_address, city, state, zip_code, deadline, weight, packageNote, status, departure_time, delivery_time)
            package_table.hash_insert(ID, insert)

# Store hashtable variable
package_table = HashTable()

# Finds the shortest distance to next address
def address_index(address_string):
    for row in address_table:
        if address_string in row[2]:
            return int(row[0])

# Calculate distance between two points
def distance_between(point1, point2):
    distance_difference = distance_table[point1][point2]
    if distance_difference == '':
        distance_difference = distance_table[point2][point1]
    return float(distance_difference)

# Reads data from package file
add_packages('Data_Files/Packages.csv')

# Create truck objects
truck1 = Truck([4, 13, 14, 15, 16, 19, 20, 21, 22, 24, 26, 27, 34, 35, 40], timedelta(hours=8), 18, 0.0, "4001 South 700 East")
truck2 = Truck([1, 2, 3, 6, 7, 8, 10, 18, 25, 29, 30, 31, 36, 37, 38], timedelta(hours=9, minutes=10), 18, 0.0, "4001 South 700 East")
truck3 = Truck([5, 9, 11, 12, 17, 23, 28, 32, 33, 39], timedelta(hours=11), 18, 0.0, "4001 South 700 East")


# Assigns truck number to packages
for package_id in truck1.packages:
    package = package_table.lookup(package_id)
    package.truck_id = 1
for package_id in truck2.packages:
    package = package_table.lookup(package_id)
    package.truck_id = 2
for package_id in truck3.packages:
    package = package_table.lookup(package_id)
    package.truck_id = 3

''' 
Beginning of nearest-neighbor algorithm
'''

# Beginning of trucks delivering packages
def algorithm(truck):

    # Gathers packages for truck delivery
    packages_to_deliver = []
    for package_id in truck.packages:
        pkg = package_table.lookup(package_id)
        packages_to_deliver.append(pkg)
        if pkg is None:
            # If package is missing
            print(f"Warning: Package ID {package_id} not found in package_table.")

    while len(packages_to_deliver) > 0:
        nxt_pkg = None
        nxt_address = 100
        for package in packages_to_deliver:
            if package.package_id in [25, 6]:
                nxt_pkg = package
                nxt_address = distance_between(address_index(truck.currentLocation), address_index(package.address))
                break
            if distance_between(address_index(truck.currentLocation), address_index(package.address)) <= nxt_address:
                nxt_address = distance_between(address_index(truck.currentLocation), address_index(package.address))
                nxt_pkg = package

        truck.packages.append(nxt_pkg.package_id)
        packages_to_deliver.remove(nxt_pkg)
        truck.mileage += nxt_address
        truck.currentLocation = nxt_pkg.address
        truck.time += datetime.timedelta(hours=nxt_address / truck.speed)
        nxt_pkg.delivery_time = truck.time
        nxt_pkg.departure_time = truck.departure_time


# Insert trucks into algorithm function
algorithm(truck1)
algorithm(truck2)
algorithm(truck3)

# Begin interactive UI
print("WGUPS Routing Program Implementation")

# Get total miles for all trucks
print("Total mileage for all trucks:", (truck1.mileage + truck2.mileage + truck3.mileage))

while True:

    inputTime = input("What time would you like to see each package? (Write your time in H:M format): ")
    (h, m) = inputTime.split(":")
    changeTime = datetime.timedelta(hours=int(h), minutes=int(m))

    try:
        enterID = [int(input("Enter the package ID:"))]
    except ValueError:
            enterID = range(1,41)
    for packageID in enterID:
            package = package_table.lookup(packageID)
            package.package_status(changeTime)
            print(str(package))



