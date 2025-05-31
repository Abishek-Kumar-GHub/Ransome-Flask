from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os
import stat  # For setting file permissions

load_dotenv()

app = Flask(__name__)
FOLDER_PATH = "simulation_data"

# Load Fernet key
with open("encryption.key", "rb") as key_file:
    encryption_key = key_file.read()

cipher = Fernet(encryption_key)

# Load encrypted password from env and decrypt it
encrypted_pass = os.getenv("PASS_ENC").encode()
PASSWORD = cipher.decrypt(encrypted_pass).decode()

# XOR encryption key (for demo purposes)
XOR_KEY = 123

def xor_encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

def lock_files():
    for filename in os.listdir(FOLDER_PATH):
        filepath = os.path.join(FOLDER_PATH, filename)
        if os.path.isfile(filepath) and not filename.endswith(".locked"):
            with open(filepath, "rb") as f:
                data = f.read()
            encrypted_data = xor_encrypt_decrypt(data, XOR_KEY)
            with open(filepath, "wb") as f:
                f.write(encrypted_data)
            os.rename(filepath, filepath + ".locked")
            # Restrict permissions to the file (no access for user, group, others)
            os.chmod(filepath + ".locked", 0)

def unlock_files():
    for filename in os.listdir(FOLDER_PATH):
        if filename.endswith(".locked"):
            filepath = os.path.join(FOLDER_PATH, filename)
            # Restore permissions to the file before unlocking
            os.chmod(filepath, stat.S_IRUSR | stat.S_IWUSR)  # Read & write for user
            with open(filepath, "rb") as f:
                data = f.read()
            decrypted_data = xor_encrypt_decrypt(data, XOR_KEY)
            with open(filepath, "wb") as f:
                f.write(decrypted_data)
            os.rename(filepath, filepath.replace(".locked", ""))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lock", methods=["POST"])
def lock():
    try:
        lock_files()
        return jsonify({"message": "Files locked successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/unlock", methods=["POST"])
def unlock():
    data = request.json
    if data and data.get("decryption_key") == PASSWORD:
        try:
            unlock_files()
            return jsonify({"message": "Files unlocked successfully!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid decryption key"}), 400

@app.route("/status", methods=["GET"])
def status():
    locked_files = [f for f in os.listdir(FOLDER_PATH) if f.endswith(".locked")]
    unlocked_files = [f for f in os.listdir(FOLDER_PATH) if not f.endswith(".locked")]
    return jsonify({"locked_files": locked_files, "unlocked_files": unlocked_files})

if __name__ == "__main__":
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
        with open(os.path.join(FOLDER_PATH, "example1.txt"), "w") as f:
            f.write("This is example file 1.")
        with open(os.path.join(FOLDER_PATH, "example2.txt"), "w") as f:
            f.write("This is example file 2.")
    app.run(debug=True)
