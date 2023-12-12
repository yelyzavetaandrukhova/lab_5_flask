
import unittest
import requests
from app import app

class FlaskAppTest(unittest.TestCase):

    def test_index_endpoint(self):
        url = 'http://localhost:5000/index'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.content)

    def test_about_endpoint(self):
        url = 'http://localhost:5000/about'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.content)

    def test_add_endpoint(self):
        url = 'http://localhost:5000/add'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.content)

    def test_account_endpoint(self):
        url = 'http://localhost:5000/account'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.content)

    def test_addaccount_endpoint(self):
        url = 'http://localhost:5000/addaccount'
        data = {'customerName': 'John Doe', 'balance': 4500, 'currencyCode': 'USD'}
        response = requests.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        print(response.content)

    def test_transfer_endpoint(self):
        url = 'http://localhost:5000/addpost'
        data = {'currencyCode': 'UhhSD', 'amount': 4500, 'fromAccountId': 3, 'toAccountId': 2}
        response = requests.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        print(response.content)

    def test_transfer_endpoint1(self):
        url = 'http://127.0.0.1:5000/addpost'
        data = {'currencyCode': 'UyhSD', 'amount': 50000, 'fromAccountId': 3, 'toAccountId': 2}
        response = requests.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        print(response.content)

if __name__ == '__main__':
    unittest.main()
