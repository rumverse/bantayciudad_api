import falcon
api = application = falcon.API()
from resources import alerts
from resources import users
from resources import location
from resources import images

api.add_route("/alerts", alerts.Collection())
api.add_route("/alerts/id/{idn}", alerts.Object())
api.add_route("/alerts/feeds/", alerts.Collection())
api.add_route("/users", users.Collection())
api.add_route("/users/id/{idn}", users.Object())
api.add_route("/location", location.Object())
api.add_route("/users/id/{idn}", users.Object())
api.add_route("/getalert", alerts.Collection())

storage_path = '/tmp'

image_collection = images.Collection(storage_path)
image = images.Item(storage_path)

api.add_route('/images', image_collection)
api.add_route('/images/{name}', image)