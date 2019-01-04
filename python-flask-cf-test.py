"""Cloud Foundry test"""
from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def flask_test():
    return 'Python Flask test! I am running on port ' + str(port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
