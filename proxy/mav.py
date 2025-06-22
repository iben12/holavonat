from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='./static', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f"Script dir: {script_directory} Contents: ")
    print(os.listdir())
    app.run(host='0.0.0.0', port=8000)
