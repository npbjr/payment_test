from application.app import app
from flask import session
app.run()
session['paymentdata'] = 'aaa'