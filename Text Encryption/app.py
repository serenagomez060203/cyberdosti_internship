from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text_to_encrypt = request.form['text']
    encrypted_text = cipher_suite.encrypt(text_to_encrypt.encode()).decode()
    return render_template('result.html', result=encrypted_text, action='Encrypted')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text_to_decrypt = request.form['text']
    decrypted_text = cipher_suite.decrypt(text_to_decrypt.encode()).decode()
    return render_template('result.html', result=decrypted_text, action='Decrypted')

if __name__ == '__main__':
    app.run(debug=True)
