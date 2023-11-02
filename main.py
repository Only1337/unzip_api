from flask import Flask, jsonify, request
import io
import requests
import zipfile
import hashlib

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def list_files():
    remote_zip_url = request.args.get('get')
    response = requests.get(remote_zip_url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    file_list = zip_file.namelist()
    file_dict = {}
    for file_name in file_list:
        file_hash = hashlib.md5(file_name.encode()).hexdigest()
        file_dict[file_name] = file_hash
    return jsonify(file_dict)

@app.route('/download', methods=['GET'])
def download_file():
    remote_zip_url = request.args.get('get')
    file_hash = request.args.get('file')
    response = requests.get(remote_zip_url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    file_list = zip_file.namelist()
    for file_name in file_list:
        if hashlib.md5(file_name.encode()).hexdigest() == file_hash:
            file_content = zip_file.read(file_name)
            return file_content
    return "File not found"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
