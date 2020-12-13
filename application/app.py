from flask import Flask, request, session
from .config.payment_modes import Config
import json
from .api import blueprint
app = Flask(__name__)
app.config['DEBUG'] = True
config = Config(app)
app.secret_key = 'secret'
# Check Configuration section for more details
app.register_blueprint(blueprint, url_prefix='')
