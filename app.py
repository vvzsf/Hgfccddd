
# Import Flask and create the app
from flask import Flask, render_template, Response, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    with open('uploaded_file.mp4', 'rb') as video_file:
        while True:
            data = video_file.read(1024)
            if not data:
                break
            yield data

@app.route('/video')
def video():
    return Response(generate(), mimetype='video/mp4')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'

    file.save('uploaded_file.mp4')
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
              
