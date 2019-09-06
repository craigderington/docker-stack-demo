#!/usr/bin/python
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/", methods=["GET"])
def index():
    """ Return the homepage counter """
    counter = redis.incr("hits")
    return "This page has been accessed {} times.\n".format(
        str(counter)
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
