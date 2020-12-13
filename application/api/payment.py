from flask import request, make_response
from flask.views import MethodView

from .util import validateCardNumber
from ..external_services import cheapPay, premiumPay, expensivePay
import json
from flask import make_response, jsonify

class PaymentView(MethodView):

    def post(self):
        from application.app import config
        if not validateCardNumber(request.args['creditCardNumber']):
            return make_response(jsonify(message='invalid card number',status=400, category='error'), 400)
        try:
            amount = int(request.args['amount'])
        except Exception as e:
            raise e
        if amount <= 20:
            print('cheap payment')
            return cheapPay.process(request)
        elif amount in range(21, 500):
            print('expensive payment')
            if config.paymentModes['espensive']:
                return expensivePay.process(request)
            else:
                # try once only once
                return cheapPay.process(request)
        elif amount > 500:
            return premiumPay.process(request)


class SetAvailability(MethodView):
    def post(self):
        from application.app import config
        try:
            paymentMode = request.args

        except Exception as e:
            raise e

        return config.setPaymentModes(json.dumps(paymentMode))


SET_AVAILABILITY = SetAvailability.as_view('availability')
PAYMENT_VIEW = PaymentView.as_view('payment')
