from flask import Flask, render_template, request, jsonify, Response, session
import os
import io
import csv
import fitz  # PyMuPDF
from .information_extractor import extract_information

app = Flask(__name__)
app.secret_key = os.urandom(24)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        text = extract_text_from_pdf(filepath)
        session['threat_data'] = extract_information(text)
        return jsonify(session['threat_data'])

def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/download')
def download():
    threat_data = session.get('threat_data', [])
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Threat Name', 'Industry', 'Country', 'Threat Type', 'Severity'])
    for threat in threat_data:
        writer.writerow([threat['name'], threat['industry'], threat['country'], threat['threat_type'], threat['severity']])
    output.seek(0)
    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=threat_summary.csv"})

if __name__ == '__main__':
    app.run(debug=True)
