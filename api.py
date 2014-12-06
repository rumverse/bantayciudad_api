import falcon
api = application = falcon.API()
from resources import alerts
from resources import users
from resources import location

api.add_route("/alerts", alerts.Collection())
api.add_route("/alerts/id/{idn}", alerts.Object())
api.add_route("/alerts/feeds/", alerts.Collection())
api.add_route("/users", users.Collection())
api.add_route("/users/id/{idn}", users.Object())
api.add_route("/location", location.Object())
api.add_route("/users/id/{idn}", users.Object())
