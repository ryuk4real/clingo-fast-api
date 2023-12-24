# Clingo FastAPI

## Introduction

This Python application is designed to solve Answer Set Programming (ASP) problems and return the solutions as JSON-formatted answer sets. It leverages the power of [clingo-api](https://potassco.org/clingo/python-api/current/clingo/) to process the ASP code and [FastAPI](https://fastapi.tiangolo.com/) with [uvicorn](https://www.uvicorn.org/) to serve the API requests.

## Features

- **Post Method API**: Send your ASP problem as plain text, and receive a JSON list of all answer sets.
- **Easy to Run**: Launch the application from the main using

```bash
python3 -m clingo_fast_api
```

- **Built with Poetry**: Manage the project dependencies and settings with ease using Poetry.

## Quick Start

To get started with Clingo Fast API, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/ryuk4real/clingo-fast-api.git
```

2. Navigate to the project directory:

```bash
cd clingo_fast_api
```

3. Install dependencies using Poetry:

```bash
poetry install
```

4. Run the application:

```bash
python3 -m clingo-fast-api
```

## Usage

To make an API call to the POST method, use the following `curl` command:

```bash
curl -X ‘POST’
‘http://127.0.0.1:8000/answer-sets’
-H ‘accept: application/json’
-H ‘Content-Type: text/plain’
-d ‘Your ASP problem here’
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the GNU License - see the LICENSE file for details.
