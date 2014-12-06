__author__ = 'onvolo'
import logging


def log(func):

    def inner(*args, **kwargs):
        ret = False

        try:
            ret = func(*args, **kwargs)
            if "level" in kwargs and kwargs["level"] == 'DEBUG':
                msg = "Arguments were: %s, %s" % (args, kwargs)
            else:
                msg = ""

        except Exception as e:

            msg = e.message
            if "level" not in kwargs:
                kwargs["level"] = 'ERROR'

        if msg is not "":
            logging.log(kwargs["level"], msg)

        return ret

    return inner