#!/usr/bin/python
from flask import Flask, render_template
from redis import Redis
from datetime import datetime, timedelta

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """ Return the homepage counter """
    counter = redis.incr("hits")
    return render_template(
        "index.html",
         counter=counter,
         today=get_date()
    )


def get_date():
    """ return date as string """
    return datetime.now().strftime("%c")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
