import hashlib
import json
from flask import session
from flask import request, make_response, jsonify

class PremiumPayment():
    def __init__(self, *args, **kwargs):
        pass

    def process(req):
        from application.app import config
        creditCardNumber = req.args['creditCardNumber']
        cardHolder = req.args['cardHolder']
        expirationDate = req.args['expirationDate']
        securityCode = req.args['securityCode']
        amount = req.args['amount']
        data = {
            'creditCardNumber': creditCardNumber,
            'cardHolder': cardHolder,
            'expirationDate': expirationDate,
            'securityCode': securityCode,
            'amount': amount
        }

        result = hashlib.md5(json.dumps(data).encode("utf-8")).hexdigest()
        print(config.paymentModes['premium'])
        if not config.paymentModes['premium']:
            if not session.get('paymentdata', False):
                session['paymentdata'] = {}

            if result not in session['paymentdata']:
                session['paymentdata'] = {}
                session['paymentdata'][result] = 3

            elif result in session['paymentdata']:
                new_count = int(session['paymentdata'][result]) - 1
                session['paymentdata'] = {}
                session['paymentdata'][result] = new_count

            if int(session['paymentdata'][result]) < 1:
                return make_response(jsonify(message='Retry Exceed',status=500), 500)
            return make_response(jsonify(message='Payment did no proceed, please try again', status=500, category='Premium Payment'), 500)
        # create cronjob to clear session
        return make_response(jsonify(message='Payment Processed',status=200, category='Premium Payment'), 200)
