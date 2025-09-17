# Ransome-Flask

A simple Flask application demonstrating basic encryption & ransomware simulation behavior. Useful for learning about file‐encryption workflows, securing secret keys, and how malicious encryption logic might operate in a controlled environment. **Not intended for malicious use.**

---

## 🚀 Features

- Key generation (`generate-key.py`) – creates a secure symmetric key to be used for file encryption/decryption  
- Encryption logic (`encrypt-key.py`) – uses the generated key to encrypt files in a designated folder  
- Flask app (`app.py`) – UI for interacting with the encryption functionality via the web  
- Minimal front-end (templates) to upload / encrypt / decrypt files  
- Demo simulation data included (`simulation_data`) for testing purposes  

---

## 🧰 Tech Stack

| Component        | Stack / Tools                                         |
|------------------|-------------------------------------------------------|
| Backend          | Flask (Python)                                        |
| Encryption       | Symmetric key cryptography (using Python cryptography libraries) |
| Front-end        | HTML templates                                       |
| File storage     | Local file system (for uploaded / encrypted data)     |

---

## 🔧 Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/Abishek-Kumar-GHub/Ransome-Flask.git
   cd Ransome-Flask
   ```

2. **Create a virtual environment (recommended)**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   _If **requirements.txt** isn’t present yet, ensure you install Flask and any encryption libraries you used (e.g. **cryptography**)._

4. **Generate encryption key**
   ```bash
   python generate-key.py
   ```
   _This will produce an **encryption.key** file._
5. **Run the app**
   ```bash
   flask run
   ```
   Or:
   ```bash
   python app.py
   ```
6. **Access in browser**
   Open http://localhost:5000 and use the interface to upload/encrypt/decrypt files.

---

# ⚠️ Warnings & Security Notes

- The app simulates ransomware-like behavior. **Do not use this for malicious purposes.**  
- The encryption key should be kept securely. If the `encryption.key` is lost, encrypted files cannot be decrypted.  
- File uploads should be validated properly before use in a production environment.  

---

# 📂 Project Structure
Ransome-Flask/
├── app.py
├── generate-key.py
├── encrypt-key.py
├── encryption.key
├── templates/
│ └── *.html
├── simulation_data/
│ └── sample files for testing
└── .gitignore
- **app.py** – main Flask application  
- **generate-key.py** – script to create the symmetric encryption key  
- **encrypt-key.py** – handles encrypting files using the key  
- **templates/** – HTML templates for UI  
- **simulation_data/** – dummy files for testing  

---

# 🎯 Possible Improvements / Next Steps

- Add user authentication (login/logout) so that only permitted users can encrypt/decrypt  
- Support for decryption workflow in web UI  
- Use safer file handling (limit file size, sanitize filenames)  
- Encrypt using more secure / varied algorithms (e.g., AES-GCM, RSA hybrid encryption)  
- Containerize the application (Docker) for easier deployment  

---

# 🤝 Contributions

Feel free to open issues or submit pull requests. If you have improvements or bug fixes, I’ll be happy to review them!  

---

# 📄 License

