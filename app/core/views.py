from flask import Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def home():
    return "A simple homepage goes here"
