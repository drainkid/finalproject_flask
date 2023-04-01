from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager(app)
import conrollers.index
import conrollers.doctors
import conrollers.date
import conrollers.docdate
import conrollers.confirm
import conrollers.hh
import conrollers.registration

if __name__ == '__main__':
    app.run()
