from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# login = LoginManager(app)
# login.login_view = 'login'

from app import routes  # noqa
