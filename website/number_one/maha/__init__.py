import os
import pandas as pd

from flask import Flask, g, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # an About page
    @app.route('/about')
    def about():
        # call some text from a file which contains information like
        # EPFL, ADA, Data-Saviours, objective of the webpage, ...
        # return render_template(about.html)
        return 'one day this should be the About page'
    
    # a help page that shows how to use the website
    @app.route('/help')
    def helppage():
        # call some text, maybe images or videos from files to explain 
        # how to use the website
        # return render_template(help.html)
        return 'another day this will be the Help page'
    
    # the main page
    @app.route('/main') # maybe just '/' or '/index'
    def main():
        # from this page you should reach all other pages and this page
        # should be reachable from all other pages.
        # it does redirection
        return render_template("index.html")
        #return 'hopefully this will be the main page some day'
    
    @app.route('/project')
    def project():
        # in this page there should be the desired view of the databases,
        # the search bar and the graph depicting...
        # return render_template(project.html)
        return 'on this page there should be our project presentation'
    
    return app
