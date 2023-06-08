from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from main import processImg
import os
from time import sleep
from threading import Thread

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_images():
    img1 = request.files['img1']
    img2 = request.files['img2']

    # Save uploaded images
    img1_path = save_uploaded_file(img1)
    img2_path = save_uploaded_file(img2)

    # Process images
    result = processImg(os.path.join(app.config['UPLOAD_FOLDER'], img1_path), os.path.join(app.config['UPLOAD_FOLDER'], img2_path))

    def delete_files():
        sleep(10)
        remove_uploaded_file(os.path.join(app.config['UPLOAD_FOLDER'], img1_path))
        remove_uploaded_file(os.path.join(app.config['UPLOAD_FOLDER'], img2_path))

    thread = Thread(target=delete_files)
    thread.start()
    return render_template('result.html', img1=img1_path, img2=img2_path, result=result)

def save_uploaded_file(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    return filename

def remove_uploaded_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == '__main__':
    app.run()
