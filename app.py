from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Finished"

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})

if __name__ == '__main__':
    app.run(host="0.0.0.0")