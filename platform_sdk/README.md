### README.md

# NTG SDK

## Overview

The NTG SDK provides a command-line tool to interact with the Hello Next Gate Tech Cloud Function. This SDK allows you to send POST requests with JSON payloads and verify the responses against expected outputs dynamically.

## Features

- **Send POST Requests**: Easily send POST requests to the Cloud Function with a specified JSON payload.
- **Sanity Check**: Automatically compare the function's response to the expected output.
- **Dynamic Expected Response**: Generate expected response dynamically by simulating the function call in `main.py`.

## Installation

1. **Install the SDK**:
   ```sh
   pip install -e platform_sdk/
   ```

## Usage

1. **Prepare JSON payload**:
   - Create a JSON file (e.g., `message.json`) with your message:
     ```json
     {
         "message": "Mark Here."
     }
     ```

2. **Run the SDK command**:
   ```sh
   ntg-sdk <URL> <JSON_FILE>
   ```
   - Example:
     ```sh
     ntg-sdk https://europe-west2-next-gate-tech-project.cloudfunctions.net/prod-hello_next_gate_tech message.json
     ```

## Command-Line Tool

- **Installation**: The `ntg-sdk` command-line tool is installed via the `setup.py` script.
- **Entry Point**: Defined in `setup.py` under `entry_points` as `ntg-sdk=platform_sdk.sdk:main`.

## Requirements

- **Python 3.6+**
- **Requests Library**
