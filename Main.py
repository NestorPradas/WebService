from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Configurar carpeta para guardar archivos
UPLOAD_FOLDER = './Archivos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta para subir archivos
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró el archivo'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'El archivo no tiene nombre'}), 400
    
    # Guardar archivo
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    return jsonify({'mensaje': f'Archivo {file.filename} subido con éxito'}), 200

if __name__ == '__main__':
    app.run(debug=True)