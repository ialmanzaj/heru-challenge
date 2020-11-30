import unittest
#import pytest

from api.main import app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_empty_response(self):
        response = self.client.post('/parse')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {
            "message": "text is empty"
        })


if __name__ == "__main__":
    unittest.main()
