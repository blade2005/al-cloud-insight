from hammock import Hammock

from tacoma import Tacoma

class CloudInsight(object):
    def __init__(self, username, password, host='https://api.cloudinsight.alertlogic.com'):
        pre_auth_ci = Hammock(host, auth=(username, password))
        resp = pre_auth_ci.aims.v1.authenticate.POST().json()
        self.account_id = resp['authentication']['account']['id']
        self.auth_token = resp['authentication']['token']
        headers = {
            'x-aims-auth-token': self.auth_token,
            'Accept-encoding': 'gzip'
        }
        self.ci = Hammock(host, headers=headers)
        
        self.tacoma = Tacoma(self)