__author__ = 'rex'

import csv
import users
import time

with open('../data/users_data.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    alert_collection = users.Collection()
    for row in reader:
        row["created"] = int(time.time())
        alert_collection.collection.insert(row)

