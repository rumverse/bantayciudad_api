import falcon
api = application = falcon.API()
from resources import events

api.add_route("/events", events.Collection())
api.add_route("/events/{idn}", events.Object())