# Unzip API

This repository contains a Python Flask application that provides a REST API for handling zip files on the server side. The application has two main functionalities:

1. **Listing Files**: The `/list` endpoint accepts a GET request with a remote zip file URL as a parameter. It returns a JSON object containing the names of the files in the zip file and their corresponding MD5 hash values.

2. **Downloading Files**: The `/download` endpoint accepts a GET request with a remote zip file URL and an MD5 hash value as parameters. It returns the content of the file in the zip file that matches the provided MD5 hash value.

## Installation

To run this application, you need to have Python and Flask installed on your machine. You can install Flask using pip:

```bash
pip install flask
```

## Usage

You can start the application by running the following command in your terminal:

```bash
python main.py
```

The application will start running on `http://0.0.0.0:5000`.

## Example

To list the files in a remote zip file, you can send a GET request to the `/list` endpoint with the remote zip file URL as a parameter:

```bash
curl "http://0.0.0.0:5000/list?get=<remote_zip_url>"
```

To download a file from a remote zip file, you can send a GET request to the `/download` endpoint with the remote zip file URL and the MD5 hash value of the desired file as parameters:

```bash
curl "http://0.0.0.0:5000/download?get=<remote_zip_url>&file=<file_hash>"
```
