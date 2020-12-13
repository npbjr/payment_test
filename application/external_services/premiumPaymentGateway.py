import hashlib
import json
from flask import session
class PremiumPayment():
    def __init__(self, *args, **kwargs):
        pass

    def process(req):

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
            return 'retry exceed'
        # create cronjob to clear session
        return data
