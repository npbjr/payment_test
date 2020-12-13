from flask import Blueprint
from .payment import PAYMENT_VIEW
from .payment import SET_AVAILABILITY
API_BP = Blueprint('api_bp', __name__)
API_BP.add_url_rule('/processPayment', view_func=PAYMENT_VIEW)
API_BP.add_url_rule('/setAvailability', view_func=SET_AVAILABILITY)