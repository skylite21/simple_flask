activate_this = '/var/www/flask_app.hu/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0,"/var/www/flask_app.hu/")
from app import app
application = app
