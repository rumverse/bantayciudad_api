import falcon
api = application = falcon.API()
from resources import alerts
from resources import users
from resources import location

api.add_route("/alerts", alerts.Collection())
api.add_route("/alerts/id/{idn}", alerts.Object())
