__author__ = 'rex'

import csv
import alerts

with open('../data/alerts.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    alert_collection = alerts.Collection()
    for row in reader:
        alert_collection.collection.insert(row)

