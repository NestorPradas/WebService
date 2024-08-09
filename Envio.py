import requests
import yaml
import os
import time
import glob
import shutil

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def upload_file_to_server(file_path):
    url = 'http://127.0.0.1:5000/upload'
    
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
    
    return response.json()

def move_file_to_sent_folder(file_path):
    folder, filename = os.path.split(file_path)
    sent_folder = os.path.join(folder, 'enviados')
    os.makedirs(sent_folder, exist_ok=True)  # Crea la carpeta si no existe

    destination_path = os.path.join(sent_folder, filename)
    shutil.move(file_path, destination_path)  # Mueve el archivo a la carpeta "enviados"

def process_files():
    config = load_config()
    configurations = config.get('configurations', [])
    wait_time = config.get('wait_time', 10)

    while True:  # Ejecución continua
        for config in configurations:
            folder = config['folder']
            filename_pattern = config['filename'] or '*'
            extension_pattern = config['extension'] or '*'

            pattern = os.path.join(folder, f"{filename_pattern}.{extension_pattern}")
            files = glob.glob(pattern)
            
            for file_path in files:
                print(f"Subiendo archivo: {file_path}")
                result = upload_file_to_server(file_path)
                print(result)
                move_file_to_sent_folder(file_path)
            
            time.sleep(wait_time)  # Espera el tiempo especificado antes de continuar

if __name__ == '__main__':
    process_files()