__author__ = 'rex'

import csv
import alerts
import time

with open('../data/alerts_data.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    alert_collection = alerts.Collection()
    for row in reader:
        row["created"] = int(time.time())
        row["username"] = row["userid"]
        alert_collection.collection.insert(row)

