
class Config():
    def __init__(self, app):
        self.app = app
        app.config['paymentmodes'] = {
            'expensive':True,
            'cheap':True,
            'premium':True,
        }
    @property
    def paymentModes(self):
        return self.app.config['paymentmodes']

    def setPaymentModes(self, data):
        import json
        data = json.loads(data)
        print(self.app.config['paymentmodes'])
        for key in data:
            if key in self.app.config['paymentmodes']:
                self.app.config['paymentmodes'][key] = data[key] == 'True'
                print(self.app.config['paymentmodes'][key])

        return self.app.config['paymentmodes']