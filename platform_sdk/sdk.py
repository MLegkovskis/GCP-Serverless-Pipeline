import requests
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# flake8: noqa: E402
from main import hello_next_gate_tech


def call_hello_next_gate_tech(url, json_data):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=json_data)
    response.raise_for_status()
    return response.text

def get_expected_response(json_data):
    # Simulate a call to the hello_next_gate_tech function
    class MockRequest:
        def __init__(self, json_data):
            self._json = json_data

        def get_json(self, silent=False):
            return self._json

    expected_response = hello_next_gate_tech(MockRequest(json_data))
    print(f"Debug: Generated expected response: {expected_response}")
    return expected_response

def print_in_box(message):
    lines = message.split('\n')
    width = max(len(line) for line in lines)
    print('+' + '-' * (width + 2) + '+')
    for line in lines:
        print(f'| {line.ljust(width)} |')
    print('+' + '-' * (width + 2) + '+')

def main():
    if len(sys.argv) != 3:
        print("Usage: sdk.py <URL> <JSON_FILE>")
        sys.exit(1)

    url = sys.argv[1]
    json_file_path = sys.argv[2]

    # Read JSON data from file
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    try:
        # Dynamically get the expected response from main.py
        expected_response = get_expected_response(json_data)
        print_in_box(f"Expected response from main.py:\n{expected_response}")

        print_in_box(f"Calling the Cloud Function at:\n{url}")
        result = call_hello_next_gate_tech(url, json_data)
        print_in_box(f"Function response:\n{result}")

        # Sanity check
        if result == expected_response:
            print_in_box("Sanity check passed: The function response matches the expected output.")
        else:
            print_in_box(f"Sanity check failed: The function response does not match the expected output.\nExpected: {expected_response}\nGot: {result}")
    except requests.exceptions.RequestException as e:
        print_in_box(f"An error occurred:\n{e}")
    except ValueError as e:
        print_in_box(f"Invalid JSON:\n{e}")

if __name__ == '__main__':
    main()