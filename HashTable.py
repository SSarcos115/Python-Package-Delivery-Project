from Package import Package

# Hash Table Creation
class HashTable:
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Hash function
    def hash_insert(self, key, object):
        hashbucket = hash(key) % len(self.table)
        num_of_buckets = self.table[hashbucket]
        for k in num_of_buckets:
            if k[0] == key:
                k[1] = object
                return True
        # Put item at end of the list if no bucket is found
        key_value = [key, object]
        num_of_buckets.append(key_value)
        return True

    # Searches for package by ID
    def lookup(self, package_id):
        index = hash(package_id) % len(self.table)
        num_of_buckets = self.table[index]
        # Return none if not found
        for k in num_of_buckets:
            if k[0] == package_id:
                return k[1]
        return None

    # Removes package
    def remove_item(self, package_id):
        index = hash(package_id) % len(self.table)
        num_of_buckets = self.table[index]
        if package_id in num_of_buckets:
            num_of_buckets.remove(package_id)

