import json
import unittest

import main as backend


enterprise1 = {
    "Name": "Enterprise1",
    "Description": "Description1",
    "Country": "Country1",
}

enterprise2 = {
    "Name": "Enterprise2",
    "Description": "Description2",
    "Country": "Country2",
}

enterprise3 = {
    "Name": "Enterprise3",
    "Description": "Description3",
    "Country": "Country3",
}

enterprise4 = {
    "Name": "Enterprise4",
    "Description": "Description4",
    "Country": "Country4",
}

enterprise5 = {
    "Name": "Enterprise5",
    "Description": "Description5",
    "Country": "Country5",
}


class BackendTestCase(unittest.TestCase):

    def __init__(self, method_name='runTest'):
        super(BackendTestCase, self).__init__(method_name)
        backend.app.testing = True
        self.app = backend.app.test_client()

    def test_1_post_enterprises(self):
        rsp = self.app.post('/enterprise', data=json.dumps(enterprise1))
        self.assertTrue('id' in json.loads(rsp.data))

        rsp = self.app.post('/enterprise', data=json.dumps(enterprise2))
        self.assertTrue('id' in json.loads(rsp.data))

        rsp = self.app.post('/enterprise', data=json.dumps(enterprise3))
        self.assertTrue('id' in json.loads(rsp.data))

        rsp = self.app.post('/enterprise', data=json.dumps(enterprise4))
        self.assertTrue('id' in json.loads(rsp.data))

        rsp = self.app.post('/enterprise', data=json.dumps(enterprise5))
        self.assertTrue('id' in json.loads(rsp.data))

    def test_2_get_enterprises(self):
        rsp = self.app.get('/enterprises')
        enterprises = json.loads(rsp.data)
        self.assertEqual(len(enterprises), 5)


if __name__ == '__main__':
    unittest.main()
