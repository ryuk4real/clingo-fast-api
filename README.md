# FastAPI Answer Set Programming API

## Introduction

This API is designed to process Answer Set Programming (ASP) code. Users can send their ASP program via the /answer-sets endpoint, and the API will return the computed answer sets.

## Requirements

- FastAPI
- Uvicorn

## Installation

To install the required packages, run the following command:

```
pip install fastapi uvicorn
```

## Usage

To start the API, use the following command:

```
uvicorn main:app
```

The --reload flag enables auto-reloading so the server will restart after code changes.

## API Endpoints

### POST /answer-sets

Send your ASP program as the request body to this endpoint. The API will return the answer sets for the given program. 

### Request Body

- A string containing your ASP program as plain text.

### Response

- A list of answer sets computed from the provided ASP program in JSON format.

### Example

Here’s an example of how to use the API with curl:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/answer-sets' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"program": "your_asp_program_here"}'
```

Replace your_asp_program_here with your actual ASP program.

## Development

For development purposes, you can run the API in reload mode to enable hot-reloading. This will restart the server after code changes.

```
uvicorn main:app --reload
```

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.



- - -
This README provides a basic overview of the API’s functionality. You can expand it with more detailed documentation, examples, and configuration options as needed for your API.
