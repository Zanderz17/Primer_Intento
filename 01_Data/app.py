from flask import Flask 

from config import config

app = Flask(__name__)


def page_not_found(error):
  return "<h1> Gaaaaa <h1", 404


if __name__ == "__main__":
  app.config.from_object
dsds
