import unittest
import json
from main import hello_next_gate_tech


class MockRequest:
    def __init__(self, json_data):
        self._json = json_data

    def get_json(self, silent=False):
        return self._json


class TestHelloNextGateTech(unittest.TestCase):
    @staticmethod
    def load_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def test_hello_next_gate_tech_with_message_from_json(self):
        json_data = self.load_json('message.json')
        message = json_data.get('message', '')
        response = hello_next_gate_tech(MockRequest(json_data))
        expected_response = 'Hello, Next Gate Tech!'
        if message:
            expected_response += ' ' + message
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
