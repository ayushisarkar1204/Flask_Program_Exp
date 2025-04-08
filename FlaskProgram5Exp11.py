from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        f = request.files['file']
        if f.filename == '':
            return 'No selected file'
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return 'File uploaded!'
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
