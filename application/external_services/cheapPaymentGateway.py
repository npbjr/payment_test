from flask import request, make_response, jsonify
class CheapPayment():
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
        return make_response(jsonify(message='Payment Processed',status=200, category='Cheap Payment'), 200)
