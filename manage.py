"""Resting manager script."""

from urllib.parse import unquote
from flask import url_for
from flask_script import Manager
from resting import create_app, init_db


app = create_app('development')  # pylint: disable=invalid-name
manager = Manager(app) # pylint: disable=invalid-name


@manager.command
def run_init_db(reset=False):
    """init db script"""
    init_db(reset)


@manager.command
def list_routes():
    """List routes."""
    output = list()
    for rule in app.url_map.iter_rules():
        options = dict()
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == "__main__":
    manager.run()
