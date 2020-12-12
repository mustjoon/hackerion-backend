
from flask import Flask
import os
import json

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

    @app.route('/api/nmap', methods=['GET'])
    def nmapGET():
        ## tämä on vain testi, ei mitään järkevää
        x =  '{ "name":"John", "age":30, "city":"New York"}'
        y = json.loads(x)
        return y

    @app.route('/api/nmap', methods=['POST'])
    def nmapPOST():
        x =  '{ "name":"Poster", "age":30, "city":"New York"}'
        ## Tänne jotain järkevää kiitos
        ## Ehkä jotain soketti hommia ??? en tiedä
        y = json.loads(x)
        return y


    from . import db
    db.init_app(app)

    return app