# BPIQ Drug Data Fetcher

This Python script retrieves drug/catalyst data from the [BPIQ](https://www.bpiq.com/bpiq-api) API and saves the response to a local JSON file.


## 🔧 Features

- Authenticates using an API token stored securely in a `credentials.py` file.
- Makes a `GET` request to the `/api/v1/drugs/` endpoint.
- Pretty-prints the response to the console.
- Saves the full response to a file: `bpiq_response.json`.



## 🛠️ Requirements

- Python 3.6+
- [`requests`](https://pypi.org/project/requests/) library

Install it if needed:

```bash
pip install -r requirements.txt
```


## 🔐 Setup

1. Create a file named `credentials.py` in the same directory as your script:

    ```python
    # credentials.py
    API_TOKEN = "your_bpiq_api_key_here"
    ```

2. (Optional but strongly recommended) Add `credentials.py` to your `.gitignore` to avoid committing sensitive information:

    ```gitignore
    credentials.py
    ```

This keeps your API token secure while letting the script access it via import.


## 🚀 Usage

Run the script from the command line:

```bash
python script.py
```